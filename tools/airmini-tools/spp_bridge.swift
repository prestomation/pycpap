// spp_bridge.swift
// Publishes SPP SDP record on macOS, accepts incoming RFCOMM from AirMini,
// bridges all data to a Unix socket where Python handles the NCP/SRP protocol.
//
// Build:  swiftc -o spp_bridge spp_bridge.swift -framework IOBluetooth -framework AppKit
// Sign:   codesign --force --sign - --entitlements bt.entitlements spp_bridge
// Run:    ./spp_bridge
// Then:   python3 airmini_pair.py  (in another terminal)

import Foundation
import IOBluetooth

let SOCKET_PATH = "/tmp/airmini_bridge.sock"

class BridgeServer {
    var clientFD: Int32 = -1
    var serverFD: Int32 = -1

    func start() -> Bool {
        unlink(SOCKET_PATH)
        serverFD = socket(AF_UNIX, SOCK_STREAM, 0)
        guard serverFD >= 0 else {
            print("ERROR: socket() failed (errno=\(errno))")
            return false
        }

        // Allow address reuse
        var one: Int32 = 1
        setsockopt(serverFD, SOL_SOCKET, SO_REUSEADDR, &one, socklen_t(MemoryLayout<Int32>.size))

        var addr = sockaddr_un()
        addr.sun_family = sa_family_t(AF_UNIX)
        withUnsafeMutablePointer(to: &addr.sun_path) { ptr in
            SOCKET_PATH.withCString { src in
                _ = strcpy(UnsafeMutableRawPointer(ptr).assumingMemoryBound(to: CChar.self), src)
            }
        }

        let bindRet = withUnsafePointer(to: &addr) {
            $0.withMemoryRebound(to: sockaddr.self, capacity: 1) {
                bind(serverFD, $0, socklen_t(MemoryLayout<sockaddr_un>.size))
            }
        }
        guard bindRet == 0 else {
            print("ERROR: bind() failed (errno=\(errno))")
            return false
        }
        listen(serverFD, 1)
        chmod(SOCKET_PATH, 0o666)
        print("Bridge socket ready at \(SOCKET_PATH)")
        return true
    }

    func waitForClient() -> Bool {
        print("Waiting for Python client to connect...")
        clientFD = accept(serverFD, nil, nil)
        guard clientFD >= 0 else {
            print("ERROR: accept() failed (errno=\(errno))")
            return false
        }
        print("Python client connected!")
        return true
    }

    func send(_ data: Data) {
        guard clientFD >= 0 else { return }
        _ = data.withUnsafeBytes { ptr in
            Foundation.send(clientFD, ptr.baseAddress!, data.count, 0)
        }
    }

    func recv() -> Data? {
        guard clientFD >= 0 else { return nil }
        var buf = [UInt8](repeating: 0, count: 4096)
        let n = read(clientFD, &buf, buf.count)
        guard n > 0 else { return nil }
        return Data(buf[0..<n])
    }
}

let bridge = BridgeServer()

class RFCOMMDelegate: NSObject, IOBluetoothRFCOMMChannelDelegate {
    var channel: IOBluetoothRFCOMMChannel?
    var connected = false

    func rfcommChannelOpenComplete(_ rfcommChannel: IOBluetoothRFCOMMChannel!, status error: IOReturn) {
        if error == 0 {
            self.channel = rfcommChannel
            self.connected = true
            let dev = rfcommChannel.getDevice()
            print("✅ RFCOMM connected from: \(dev?.name() ?? "unknown") ch\(rfcommChannel.getChannelID())")
            // Signal Python that connection is established
            bridge.send(Data([0xFF, 0xFE, 0xFD, 0xFC]))
        } else {
            print("❌ RFCOMM open failed: \(error)")
        }
    }

    func rfcommChannelData(_ rfcommChannel: IOBluetoothRFCOMMChannel!, data dataPointer: UnsafeMutableRawPointer!, length dataLength: Int) {
        let data = Data(bytes: dataPointer, count: dataLength)
        print("  [BT→Python] \(dataLength) bytes")
        bridge.send(data)
    }

    func rfcommChannelClosed(_ rfcommChannel: IOBluetoothRFCOMMChannel!) {
        print("RFCOMM channel closed")
        self.connected = false
        bridge.send(Data([0xFF, 0xFE, 0xFD, 0xFB]))
    }

    func write(_ data: Data) {
        guard let ch = channel else {
            print("⚠ Cannot write: no channel")
            return
        }
        var mutable = data
        mutable.withUnsafeMutableBytes { ptr in
            let result = ch.writeSync(ptr.baseAddress!, length: UInt16(data.count))
            if result != kIOReturnSuccess {
                print("⚠ RFCOMM write failed: \(result)")
            }
        }
    }
}

let delegate = RFCOMMDelegate()

@objc func incomingChannel(_ note: IOBluetoothUserNotification!, channel ch: IOBluetoothRFCOMMChannel!) {
    let dev = ch.getDevice()
    print("📞 Incoming RFCOMM from \(dev?.name() ?? "?") (\(dev?.addressString ?? "??"))")
    ch.setDelegate(delegate)
    ch.openChannel()
}

func main() {
    guard bridge.start() else { exit(1) }

    // Try publishing SPP SDP record
    print("Publishing SPP SDP service record...")
    if let sdpRecord = IOBluetoothSDPServiceRecord.publishedServiceRecord(withDictionary: [
        "0001": ["DataElementType": "sequence", "DataElement": [
            ["DataElementType": "uuid", "DataElement": "00001101-0000-1000-8000-00805F9B34FB"]
        ]],
        "0004": ["DataElementType": "sequence", "DataElement": [
            ["DataElementType": "sequence", "DataElement": [
                ["DataElementType": "uuid", "DataElement": "00000100-0000-1000-8000-00805F9B34FB"]
            ]],
            ["DataElementType": "sequence", "DataElement": [
                ["DataElementType": "uuid", "DataElement": "00000003-0000-1000-8000-00805F9B34FB"],
                ["DataElementType": "uint8", "DataElement": 1]
            ]]
        ]],
        "0005": ["DataElementType": "sequence", "DataElement": [
            ["DataElementType": "uuid", "DataElement": "00001002-0000-1000-8000-00805F9B34FB"]
        ]],
        "0100": ["DataElementType": "string", "DataElement": "AirMini SPP"]
    ] as NSDictionary) {
        print("✅ SDP record published")
        if let ch = sdpRecord.rfcommChannelID() {
            print("   RFCOMM channel: \(ch.pointee)")
        }
    } else {
        print("⚠️ SDP publish failed — trying register-only mode")
        // Fallback: just register for incoming connections without SDP
    }

    // Register for incoming RFCOMM connections on any channel
    let notification = IOBluetoothRFCOMMChannel.register(
        forChannelOpenNotifications: delegate,
        selector: #selector(RFCOMMDelegate.incomingChannel(_:channel:)),
        withChannelID: 0,
        direction: kIOBluetoothUserNotificationChannelDirectionIncoming
    )
    if notification != nil {
        print("✅ Registered for incoming RFCOMM (handle=\(String(describing: notification)))")
    } else {
        print("❌ Failed to register for incoming RFCOMM")
    }

    // Wait for Python client
    guard bridge.waitForClient() else { exit(1) }

    // Forward data from Python → RFCOMM in background
    DispatchQueue.global(qos: .userInteractive).async {
        while true {
            if let data = bridge.recv(), data.count > 0 {
                // Check for control messages from Python
                if data.count == 4 && data == Data([0xDE, 0xAD, 0xBE, 0xEF]) {
                    print("Python requested disconnect")
                    if delegate.channel != nil {
                        delegate.channel?.closeChannel()
                    }
                    continue
                }
                print("  [Python→BT] \(data.count) bytes")
                delegate.write(data)
            }
        }
    }

    print("")
    print("=" * 50)
    print("READY — put AirMini in pairing mode:")
    print("  Hold power button until PIN shows + BT blinks")
    print("=" * 50)
    print("")

    RunLoop.main.run()
}

main()