# AirMini Bluetooth Protocol Report (com.resmed.airmini v1.8.0.0.331)
Generated: Sat Mar 21 18:51:23 UTC 2026

## Bluetooth Type
BLE GATT files: 0
Classic SPP files: 8

## All UUIDs Found
00000000-0000-0000-0000-000000000000
00001101-0000-1000-8000-00805F9B34FB

## BLE-Related Files

## Therapy Data Files
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/DeviceSettingsEntry.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/RpcCommand.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/response/SettingsResponse.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/response/SetResponse.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/response/MachineMetrics.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/notification/SubscriptionNotification.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/notification/GetLoggedDataNotification.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/enums/Setting.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/enums/TherapyProfileType.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/enums/FlowGenState.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/enums/TherapyMode.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/request/EnterTherapyRpcRequest.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/request/RpcRequest.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/model/SetRpcParams.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/model/FeatureProfiles.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/model/ComfortFeature.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/model/SmartStartStopFeature.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/model/AutoRampFeature.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/model/EprFeature.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/model/TherapyProfiles.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/RMONFirmwareUpgradeNotification$UpgradePhase.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/query/CreateRecordTherapySessionQuery.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/query/AddLoggedDataQuery.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/query/StopTherapySessionQuery.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/query/CreateTherapySessionQuery.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/query/CreateRecordSleepRecordQuery.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/d1.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/n0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/m0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/v.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/a1.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/GetSettingsHandler$GetSettingsRpcParams.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/u.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/b1.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/q0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/u0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/k1.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/IpcCommand.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/local/RMON_TherapySession.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/local/RMON_FGDevice.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/local/RMON_SleepEventDao.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/local/RMON_SleepEvent.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/local/RMON_SleepRecordDao.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/local/DaoMaster.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/local/RMON_SleepRecord.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/local/RMON_ValueItemDao.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/local/RMON_TherapySessionDao.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/local/DaoSession.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/local/RMON_ValueItem.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/local/RMON_FGDeviceDao.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/local/RMON_UserProfileDao.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/local/RMON_UserProfile.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/score/a.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/score/SleepRecordStatsCalculator$PercentileType.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/json/TherapyProfile.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/json/RegistrationData.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/json/SleepEventType.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/machine/datamodel/TherapyStatusEvents.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/machine/datamodel/SettingProfiles.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/machine/datamodel/UsageEvents.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/machine/datamodel/TherapyOneMinutePeriodic.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/machine/datamodel/RespiratoryEvents.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/machine/datamodel/TherapyEvents.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/machine/datamodel/ActiveProfiles.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/machine/datamodel/MachineData.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/machine/datamodel/MeasurementProfilesCollection.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/machine/datamodel/TherapyEvent.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/controller/k.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/controller/h.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/controller/d.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/sync/DataSyncConfiguration.java
/tmp/airmini-real-src/sources/com/resmed/mon/utils/log/UploadFileLog$UploadDataType.java
/tmp/airmini-real-src/sources/com/resmed/mon/utils/analytics/enums/AnalyticsEvent.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/section/hme/r.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/section/hme/l.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/section/hme/RMONHmeBaseSettingsFragment.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/section/hme/j.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/RMONDashboardFragment.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/activity/o.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/activity/RMONFirmwareUpgradeActivity.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/activity/n.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/testdrive/RMONTestDriveFlowActivity.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/testdrive/a.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/testdrive/d.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/model/DashboardRow.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/sleep/SleepScreenView$RunningMode.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/sleep/RMONSleepActivity.java
/tmp/airmini-real-src/sources/j8/o.java
/tmp/airmini-real-src/sources/j8/j.java
/tmp/airmini-real-src/sources/j5/o1.java
/tmp/airmini-real-src/sources/j5/h0.java
/tmp/airmini-real-src/sources/p3/g.java
/tmp/airmini-real-src/sources/a9/b.java
/tmp/airmini-real-src/sources/t2/i.java
/tmp/airmini-real-src/sources/n8/o.java
/tmp/airmini-real-src/sources/n8/r.java
/tmp/airmini-real-src/sources/n8/s.java
/tmp/airmini-real-src/sources/n8/h.java
/tmp/airmini-real-src/sources/n8/u.java
/tmp/airmini-real-src/sources/n8/t.java
/tmp/airmini-real-src/sources/n8/j.java
/tmp/airmini-real-src/sources/androidx/activity/d.java
/tmp/airmini-real-src/sources/i8/o.java
/tmp/airmini-real-src/sources/i8/h1.java
/tmp/airmini-real-src/sources/i8/n0.java
/tmp/airmini-real-src/sources/i8/i.java
/tmp/airmini-real-src/sources/g6/j0.java
/tmp/airmini-real-src/sources/g6/v0.java
/tmp/airmini-real-src/sources/g6/g.java
/tmp/airmini-real-src/sources/net/sqlcipher/R.java
/tmp/airmini-real-src/sources/d8/a.java

## ResMed Package Files
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/api/BluetoothConnectionStatus.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/receivers/BluetoothDeviceReconnectingAppReceiver.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/receivers/BluetoothDeviceReconnectingReceiver$ReconnectionType.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/DeviceSettingsEntry.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/RpcCommand.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/SettingValue.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/enums/AppState.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/enums/AutoSetComfort.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/enums/EprType.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/enums/FlowGenState.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/enums/GldStatus.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/enums/PressureUnits.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/enums/RampEnable.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/enums/RampSetting.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/enums/Setting.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/enums/SettingsHistoryStatus.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/enums/StreamType.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/enums/TherapyMode.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/enums/TherapyProfileType.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/enums/Toggle.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/enums/Tube.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/model/AutoRampFeature.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/model/BluetoothModule.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/model/ComfortFeature.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/model/EprFeature.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/model/FeatureProfiles.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/model/Firmware.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/model/FlowGenerator.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/model/Hardware.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/model/IdentificationProfiles.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/model/PatientComfortSettings.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/model/Product.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/model/SetRpcParams.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/model/SmartStartStopFeature.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/model/Software.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/model/SupportedRpcs.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/model/TherapyProfiles.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/notification/EraseDataNotification.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/notification/GetLoggedDataNotification.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/notification/GetSettingsHistoryNotification.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/notification/NotificationRpc.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/notification/StreamDataNotification.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/notification/SubscriptionNotification.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/request/DiscardPairKeyRpcRequest.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/request/DisconnectRpcRequest.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/request/EnterMaskFitRpcRequest.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/request/EnterStandbyRpcRequest.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/request/EnterTherapyRpcRequest.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/request/EraseDataRpcRequest.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/request/FirmwareUpgradeRpcRequest.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/request/GenerateAuthCodeRpcRequest.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/request/GetDateTimeRpcRequest.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/request/GetLoggedDataRpcRequest.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/request/GetPairKeyRpcRequest.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/request/GetRpcRequest.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/request/GetSessionKeyRpcRequest.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/request/GetSettingsHistoryRpcRequest.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/request/GetVersionRpcRequest.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/request/RpcRequest.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/request/SetRpcRequest.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/request/StreamRpcRequest.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/request/SubscriptionNotificationRpcRequest.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/response/ApplyUpgradeResponseRpc.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/response/AuthCodeResult.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/response/EnterMaskFitResponse.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/response/EraseDataResponse.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/response/ErrorRpc.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/response/FgStateResponse.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/response/GetDateTimeResponse.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/response/GetLoggedDataResponse.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/response/GetResponse.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/response/GetSettingsHistoryResponse.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/response/GetVersionExtraInfoResponse.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/response/KeyExchangeResult.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/response/MachineMetrics.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/response/MachineMetricsResponse.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/response/ResponseRpc.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/response/SetResponse.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/response/SettingsResponse.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/response/StreamResponse.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/response/SubscriptionResponse.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/response/TransferBlockSizeRpc.java
/tmp/airmini-real-src/sources/com/resmed/mon/bluetooth/rpc/response/VersionRpc.java
/tmp/airmini-real-src/sources/com/resmed/mon/fig/FigWrapper.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/api/IpcInterface$ResponseError.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/api/IpcRequest$ProcessName.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/api/a.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/api/b.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/api/c.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/api/d.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/api/e.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/api/f.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/api/g.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/api/h.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/api/i.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/api/j.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/IpcCommand.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/IpcNotification.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/RMONDataNotification$DataNotificationResult.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/RMONDatabaseService.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/RMONEraseDataNotification$DataNotificationType.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/RMONFirmwareUpgradeNotification$UpgradePhase.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/RMONServiceIpcManager.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/RMONSubscriptionNotification$SubscriptionNotificationType.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/AppSettingsHandler$ValueType.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/ConnectHandler$ConnectAndPairStatusValues.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/DiscoverPermissionHandler$PermissionError.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/FirmwareUpgradeHandler$FirmwareUpgradeFailure.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/GetSettingsHandler$GetSettingsRpcParams.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/GldActivityErrorLogsHandler$GLD_LOG_TYPE.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/UpdateSmartStartHandler$SmartStartAction.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/UploadMachineDataManager$Step.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/UploadMachineDataManager$Trigger.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/a.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/a0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/a1.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/b.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/b0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/b1.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/c.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/c0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/c1.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/d.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/d0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/d1.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/e.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/e0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/e1.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/f.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/f0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/f1.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/g.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/g0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/g1.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/h.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/h0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/h1.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/i.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/i0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/i1.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/j.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/j0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/j1.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/k.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/k0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/k1.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/l.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/l0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/l1.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/m.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/m0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/n.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/n0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/o.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/o0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/p.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/p0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/q.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/q0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/r.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/r0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/s.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/s0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/t.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/t0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/u.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/u0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/v.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/v0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/w.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/w0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/x.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/x0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/y.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/y0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/z.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/handler/z0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/query/AddLoggedDataQuery.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/query/AddSettingsHistoryQuery.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/query/ClearAllDataQuery.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/query/CreateRecordSleepRecordQuery.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/query/CreateRecordTherapySessionQuery.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/query/CreateTherapySessionQuery.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/query/GetDataSyncDatesQuery.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/query/GetFirmwareUpgradePostConditionQuery.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/query/GetRedirectUrlQuery.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/query/GetVersionRpcQuery.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/query/ScheduleAnalyticsServiceQuery.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/query/ScheduleImmediateUploadQuery.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/query/SerialNumberQuery.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/query/StopTherapySessionQuery.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/query/SyncSmartStartQuery.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/query/UpdateAboutAirMiniQuery.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/query/UpdateErrorActivityLogDateQuery.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/query/UpdateFirmwareUpgradePostConditionQuery.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/query/UpdateGetVersionExtraInfoQuery.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/query/UpdateLastAuthenticatedConnectionTimeQuery.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/query/UpdateMachineMetricsQuery.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/query/UpdateSigningKeyOrTokenQuery.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/query/UpdateTimeDifferenceWithPhoneQuery.java
/tmp/airmini-real-src/sources/com/resmed/mon/ipc/rmon/query/VersionQuery.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/controller/RMONDatabaseController$DropDbReason.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/controller/RMONRegistrationController$MaskType.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/controller/a.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/controller/b.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/controller/c.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/controller/d.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/controller/e.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/controller/f.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/controller/g.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/controller/h.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/controller/i.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/controller/j.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/controller/k.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/json/AuthorizationResponse.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/json/DataSyncDates.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/json/FirmwareUpgradeInformation.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/json/FirmwareUpgradeSpec.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/json/HeaderResponse.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/json/MaskModels.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/json/PolicyResponse.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/json/RegistrationData.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/json/SleepEventType.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/json/SuccessResponse.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/json/TestDrive.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/json/TherapyProfile.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/local/DaoMaster.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/local/DaoOpenHelper.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/local/DaoSession.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/local/RMON_DaoUtil.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/local/RMON_DataSyncDates.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/local/RMON_DataSyncDatesDao.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/local/RMON_FGCapabilities.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/local/RMON_FGCapabilitiesDao.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/local/RMON_FGDevice.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/local/RMON_FGDeviceCloudInfo.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/local/RMON_FGDeviceCloudInfoDao.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/local/RMON_FGDeviceDao.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/local/RMON_FGSettingsHistory.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/local/RMON_FGSettingsHistoryDao.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/local/RMON_Mask.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/local/RMON_MaskDao.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/local/RMON_SleepEvent.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/local/RMON_SleepEventDao.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/local/RMON_SleepRecord.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/local/RMON_SleepRecordDao.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/local/RMON_TherapySession.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/local/RMON_TherapySessionDao.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/local/RMON_User.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/local/RMON_UserDao.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/local/RMON_UserProfile.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/local/RMON_UserProfileDao.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/local/RMON_UserSettings.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/local/RMON_UserSettingsDao.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/local/RMON_ValueItem.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/local/RMON_ValueItemDao.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/machine/datamodel/ActiveProfiles.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/machine/datamodel/ActivityErrorLogData.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/machine/datamodel/Attributes.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/machine/datamodel/BluetoothProfile.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/machine/datamodel/MachineData.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/machine/datamodel/MeasurementProfilesCollection.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/machine/datamodel/MobileDevice.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/machine/datamodel/PeriodicValue.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/machine/datamodel/RedirectData.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/machine/datamodel/RespiratoryEvents.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/machine/datamodel/SettingProfiles.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/machine/datamodel/TherapyEvent.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/machine/datamodel/TherapyEvents.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/machine/datamodel/TherapyOneMinutePeriodic.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/machine/datamodel/TherapyStatusEvents.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/machine/datamodel/UsageEvents.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/score/SleepRecordStatsCalculator$PercentileType.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/score/a.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/service/RMONAnalyticsAgentWorker.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/service/RMONCleanupDatabaseWorker.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/service/RMONUploadDataImmediateWorker.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/service/a.java
/tmp/airmini-real-src/sources/com/resmed/mon/model/sync/DataSyncConfiguration.java
/tmp/airmini-real-src/sources/com/resmed/mon/net/http/HttpConnector$Verb.java
/tmp/airmini-real-src/sources/com/resmed/mon/net/portal/machine/FgUploadInfo.java
/tmp/airmini-real-src/sources/com/resmed/mon/net/portal/machine/RMONGetPolicyDataTask.java
/tmp/airmini-real-src/sources/com/resmed/mon/net/portal/machine/RMONUploadMachineDataTask.java
/tmp/airmini-real-src/sources/com/resmed/mon/net/portal/machine/SslErrorReceiver.java
/tmp/airmini-real-src/sources/com/resmed/mon/net/response/AppIdentifier.java
/tmp/airmini-real-src/sources/com/resmed/mon/net/response/ConfigurationProfiles.java
/tmp/airmini-real-src/sources/com/resmed/mon/net/response/ErrorResponse.java
/tmp/airmini-real-src/sources/com/resmed/mon/net/response/HttpConnectorResponse.java
/tmp/airmini-real-src/sources/com/resmed/mon/net/response/RedirectActivity.java
/tmp/airmini-real-src/sources/com/resmed/mon/net/response/RedirectResponse.java
/tmp/airmini-real-src/sources/com/resmed/mon/net/response/SigningToken.java
/tmp/airmini-real-src/sources/com/resmed/mon/net/response/SigningTokenResponse.java
/tmp/airmini-real-src/sources/com/resmed/mon/net/rmon/RMONServiceConnectorAPI$RequestHeaders.java
/tmp/airmini-real-src/sources/com/resmed/mon/net/rmon/RMONServiceConnectorAPI$ResponseHeaders.java
/tmp/airmini-real-src/sources/com/resmed/mon/net/rmon/URLResolver$Params.java
/tmp/airmini-real-src/sources/com/resmed/mon/net/rmon/URLResolver$Request.java
/tmp/airmini-real-src/sources/com/resmed/mon/net/rmon/URLResolver$Section.java
/tmp/airmini-real-src/sources/com/resmed/mon/net/rmon/URLResolver$SubSection.java
/tmp/airmini-real-src/sources/com/resmed/mon/net/rmon/a.java
/tmp/airmini-real-src/sources/com/resmed/mon/net/rmon/b.java
/tmp/airmini-real-src/sources/com/resmed/mon/net/rmon/c.java
/tmp/airmini-real-src/sources/com/resmed/mon/net/rmon/d.java
/tmp/airmini-real-src/sources/com/resmed/mon/net/rmon/e.java
/tmp/airmini-real-src/sources/com/resmed/mon/net/rmon/f.java
/tmp/airmini-real-src/sources/com/resmed/mon/net/rmon/g.java
/tmp/airmini-real-src/sources/com/resmed/mon/net/rmon/h.java
/tmp/airmini-real-src/sources/com/resmed/mon/net/rmon/i.java
/tmp/airmini-real-src/sources/com/resmed/mon/net/rmon/j.java
/tmp/airmini-real-src/sources/com/resmed/mon/response/RMONResponse.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/activity/RMONAuthenticationActivity.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/activity/RMONDashboardActivity.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/activity/RMONDateNavigatorActivity.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/activity/RMONFGStatusActivity.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/activity/RMONFirmwareUpgradeActivity.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/activity/RMONFirmwareUpgradeCompletedActivity.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/activity/RMONGuidedSetupActivity.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/activity/RMONLaunchActivity.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/activity/RMONMoreActivity.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/activity/RMONMoreDetailsActivity.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/activity/RMONRegulatoryActivity.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/activity/RMONSelectMaskActivity.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/activity/RMONTermsOfUseActivity.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/activity/RMONTermsPrivacyChangedActivity.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/activity/RMONWebViewActivity.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/activity/RMONWelcomeActivity.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/activity/a.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/activity/a0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/activity/b.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/activity/b0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/activity/c.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/activity/d.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/activity/e.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/activity/f.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/activity/g.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/activity/h.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/activity/i.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/activity/j.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/activity/k.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/activity/l.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/activity/m.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/activity/n.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/activity/o.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/activity/p.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/activity/q.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/activity/r.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/activity/s.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/activity/t.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/activity/u.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/activity/v.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/activity/w.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/activity/x.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/activity/y.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/activity/z.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/adapter/LayoutType.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/adapter/SettingsAdapter$LayoutType.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/adapter/SupportModel$ItemType.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/adapter/SupportModel$Type.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/base/BaseActivity$NavigationType.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/base/BaseBluetoothActivity$TimeoutDialog.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/base/BaseBluetoothViewModel$SyncDialog.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/base/RMONApplication.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/base/ViewBindingPropertyDelegate.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/chart/BarChart$Position.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/decorator/BluetoothIconStatus$State.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/decorator/a.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/RMONDashboardFragment.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/RMONDateNavigatorFragment.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/a.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/a0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/a1.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/b.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/b0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/b1.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/c.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/c0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/c1.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/d.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/d0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/d1.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/e.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/e0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/e1.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/f.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/f0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/f1.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/g.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/g0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/g1.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/h.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/h0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/h1.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/i.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/i0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/i1.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/j.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/j0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/j1.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/k.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/k0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/k1.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/l.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/l0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/l1.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/m.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/m0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/m1.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/n.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/n0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/n1.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/o.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/o0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/p.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/p0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/q.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/q0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/r.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/s.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/s0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/t.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/t0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/u.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/u0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/v.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/v0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/w.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/w0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/x.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/x0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/y.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/y0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/z.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/fragment/z0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/model/ComfortSettingRow.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/model/DashboardRow.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/model/EprPressure.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/model/Guide.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/model/Help.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/model/MaskGuide.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/navigation/NavigationDrawerFragment.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/navigation/NavigationDrawerSection$GLOBAL_SECTION_INDEX.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/navigation/NavigationDrawerSection$HME_SECTION_INDEX.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/section/hme/RMONHmeBaseSettingsFragment.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/section/hme/RMONHmeConnectActivity.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/section/hme/RMONHmeConnectedActivity.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/section/hme/RMONHmeCurrentSettingsActivity.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/section/hme/RMONHmeDeviceSettingsActivity.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/section/hme/RMONHmeSupportActivity.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/section/hme/RMONHmeWelcomeActivity.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/section/hme/a.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/section/hme/a0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/section/hme/b.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/section/hme/b0.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/section/hme/c.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/section/hme/d.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/section/hme/e.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/section/hme/f.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/section/hme/g.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/section/hme/h.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/section/hme/i.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/section/hme/j.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/section/hme/k.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/section/hme/l.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/section/hme/m.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/section/hme/n.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/section/hme/o.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/section/hme/p.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/section/hme/q.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/section/hme/r.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/section/hme/s.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/section/hme/t.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/section/hme/u.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/section/hme/v.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/section/hme/w.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/section/hme/x.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/section/hme/y.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/section/hme/z.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/sleep/RMONSleepActivity.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/sleep/SleepScreenView$RunningMode.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/sleep/SleepScreenView$UserMode.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/testdrive/RMONTestDriveCompletedActivity.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/testdrive/RMONTestDriveController$LeakCheck.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/testdrive/RMONTestDriveController$MaskModelTypeIds.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/testdrive/RMONTestDriveController$State.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/testdrive/RMONTestDriveFlowActivity.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/testdrive/RMONTestDriveFlowViewModel$GaugeButtonState.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/testdrive/RMONTestDriveLeakActivity.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/testdrive/RMONTestDriveLeakFixedActivity.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/testdrive/RMONTestDriveLeakTroubleshootActivity.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/testdrive/RMONTestDriveLeakTroubleshootFinalActivity.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/testdrive/a.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/testdrive/b.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/testdrive/c.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/testdrive/d.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/testdrive/e.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/testdrive/f.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/testdrive/g.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/testdrive/h.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/testdrive/i.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/testdrive/j.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/testdrive/k.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/testdrive/l.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/testdrive/m.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/testdrive/n.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/testdrive/o.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/testdrive/p.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/testdrive/q.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/testdrive/r.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/testdrive/s.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/testdrive/t.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/testdrive/u.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/testdrive/v.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/testdrive/w.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/testdrive/x.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/testdrive/y.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/testdrive/z.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/tools/ObservableScrollView.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/view/GaugeProgressBar.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/view/LoadingProgressBar.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/view/ProgressBar$ProgressType.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/view/RMONBarCodeFrameView.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/view/RMONBarCodeView.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/view/RMONCheckbox.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/view/RMONCheckedTextView.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/view/RMONSteperView.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/view/RMONSwitchCompat.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/view/ScoreProgressBar.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/workflow/appupdate/AppUpdateActivity.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/workflow/appupdate/AppUpdateViewModel$EventId.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/workflow/connectionhelp/ConnectionHelpActivity.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/workflow/firmwareupgrade/failed/FirmwareUpgradeFailedActivity.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/workflow/firmwareupgrade/failed/FirmwareUpgradeFailedViewModel$Event.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/workflow/firmwareupgrade/interrupted/FirmwareUpgradeInterruptedViewModel$Event.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/workflow/guidedsetup/help/GuidedSetupHelpActivity.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/workflow/guidedsetup/help/GuidedSetupHelpViewModel$Event.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/workflow/guidedsetup/intro/GuidedSetupIntroActivity.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/workflow/guidedsetup/intro/GuidedSetupIntroViewModel$Event.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/workflow/whatsnew/WhatsNewActivity.java
/tmp/airmini-real-src/sources/com/resmed/mon/ui/workflow/whatsnew/WhatsNewViewModel$Event.java
/tmp/airmini-real-src/sources/com/resmed/mon/utils/Consts$JobSchedulerId.java
/tmp/airmini-real-src/sources/com/resmed/mon/utils/analytics/enums/AnalyticsErrorParam.java
/tmp/airmini-real-src/sources/com/resmed/mon/utils/analytics/enums/AnalyticsEvent.java
/tmp/airmini-real-src/sources/com/resmed/mon/utils/log/AppFileLog$LogType.java
/tmp/airmini-real-src/sources/com/resmed/mon/utils/log/UploadFileLog$UploadDataType.java
/tmp/airmini-real-src/sources/com/resmed/mon/utils/log/UploadFileLog$UploadLogHeader.java
/tmp/airmini-real-src/sources/com/resmed/mon/utils/log/UploadFileLog$UploadNetwork.java
/tmp/airmini-real-src/sources/com/resmed/mon/utils/log/UploadFileLog$UploadStatus.java
/tmp/airmini-real-src/sources/com/resmed/mon/utils/log/UploadFileLog$UploadTag.java
/tmp/airmini-real-src/sources/com/resmed/mon/utils/log/UploadFileLog$UploadTrigger.java
/tmp/airmini-real-src/sources/com/resmed/mon/utils/log/a.java
/tmp/airmini-real-src/sources/com/resmed/mon/utils/log/b.java
/tmp/airmini-real-src/sources/com/resmed/mon/utils/log/c.java
/tmp/airmini-real-src/sources/com/resmed/mon/utils/log/d.java
/tmp/airmini-real-src/sources/com/resmed/mon/utils/log/e.java
/tmp/airmini-real-src/sources/com/resmed/mon/utils/log/f.java
/tmp/airmini-real-src/sources/com/resmed/mon/utils/log/g.java
/tmp/airmini-real-src/sources/com/resmed/mon/utils/text/a.java
/tmp/airmini-real-src/sources/com/resmed/mon/utils/text/b.java
/tmp/airmini-real-src/sources/com/resmed/mon/utils/text/c.java

## onCharacteristicChanged Occurrences

## Command/Opcode Patterns
/tmp/airmini-real-src/sources/net/sqlcipher/R.java:557:        public static final int gcm_defaultSenderId = 0x7f10010e;
/tmp/airmini-real-src/sources/net/sqlcipher/R.java:773:        public static final int hme_test_connection_sending = 0x7f10017a;
/tmp/airmini-real-src/sources/net/sqlcipher/R.java:1431:        public static final int test_drive_mask_request_dialog = 0x7f1002cc;
/tmp/airmini-real-src/sources/net/sqlcipher/R.java:6330:        public static final int hme_sending = 0x7f0800d6;
/tmp/airmini-real-src/sources/net/sqlcipher/R.java:6332:        public static final int hme_sending_1 = 0x7f0800d7;
/tmp/airmini-real-src/sources/net/sqlcipher/R.java:6334:        public static final int hme_sending_2 = 0x7f0800d8;
/tmp/airmini-real-src/sources/net/sqlcipher/R.java:6336:        public static final int hme_sending_3 = 0x7f0800d9;
/tmp/airmini-real-src/sources/net/sqlcipher/R.java:6340:        public static final int hme_settings_send = 0x7f0800db;
/tmp/airmini-real-src/sources/net/sqlcipher/R.java:6524:        public static final int sending_loading_icon = 0x7f080140;
/tmp/airmini-real-src/sources/net/sqlcipher/R.java:7492:        public static final int honorRequest = 0x7f0901b9;
/tmp/airmini-real-src/sources/net/sqlcipher/R.java:7510:        public static final int ignoreRequest = 0x7f0901c2;
/tmp/airmini-real-src/sources/net/sqlcipher/R.java:8066:        public static final int send_token_to_FG_button = 0x7f0902d8;


## RpcCommand Enum (RPC method names)
package com.resmed.mon.bluetooth.rpc;

import com.resmed.mon.bluetooth.rpc.response.ApplyUpgradeResponseRpc;
import com.resmed.mon.bluetooth.rpc.response.AuthCodeResult;
import com.resmed.mon.bluetooth.rpc.response.EnterMaskFitResponse;
import com.resmed.mon.bluetooth.rpc.response.EraseDataResponse;
import com.resmed.mon.bluetooth.rpc.response.FgStateResponse;
import com.resmed.mon.bluetooth.rpc.response.GetDateTimeResponse;
import com.resmed.mon.bluetooth.rpc.response.GetLoggedDataResponse;
import com.resmed.mon.bluetooth.rpc.response.GetResponse;
import com.resmed.mon.bluetooth.rpc.response.GetSettingsHistoryResponse;
import com.resmed.mon.bluetooth.rpc.response.GetVersionExtraInfoResponse;
import com.resmed.mon.bluetooth.rpc.response.KeyExchangeResult;
import com.resmed.mon.bluetooth.rpc.response.SetResponse;
import com.resmed.mon.bluetooth.rpc.response.SettingsResponse;
import com.resmed.mon.bluetooth.rpc.response.StreamResponse;
import com.resmed.mon.bluetooth.rpc.response.SubscriptionResponse;
import com.resmed.mon.bluetooth.rpc.response.TransferBlockSizeRpc;
import com.resmed.mon.bluetooth.rpc.response.VersionRpc;
import com.resmed.mon.utils.log.g;
import java.io.Serializable;
import java.util.Map;
/* loaded from: classes.dex */
public enum RpcCommand {
    APPLY_AUTH_UPGRADE("ApplyAuthenticatedUpgrade", "Applying authenticated upgrade", ApplyUpgradeResponseRpc.class, 30000),
    DISCONNECT("BtDisconnect", "Disconnecting", null, 5000),
    CHECK_UPGRADE_FILE("CheckUpgradeFile", "Checking upgrade file", Boolean.class, 30000),
    DISCARD_PAIR_KEY("DiscardPairKey", "Discarding device", Boolean.class, 5000),
    ENTER_MASK_FIT("EnterMaskFit", "Starting Mask Fit", EnterMaskFitResponse.class, 5000),
    ENTER_STANDBY("EnterStandby", "Stopping Therapy", FgStateResponse.class, 5000),
    ENTER_THERAPY("EnterTherapy", "Starting Therapy", FgStateResponse.class, 5000),
    ERASE_DATA("EraseData", "Erasing Data", EraseDataResponse.class, 5000),
    GENERATE_AUTH_CODE("GenerateAuthCode", "Getting Signing Key", AuthCodeResult.class, 5000),
    GET_VERSION_EXTRA_INFO("Get", "Getting Serial Number", GetVersionExtraInfoResponse.class, 5000),
    GET("Get", "Generic Get", GetResponse.class, 5000),
    GET_SETTINGS("Get", "Getting Settings", SettingsResponse.class, 5000),
    GET_DATE_TIME("GetDateTime", "Getting current date", GetDateTimeResponse.class, 5000),
    GET_HISTORY("GetHistory", "Getting Setting History", GetSettingsHistoryResponse.class, 5000),
    GET_LOGGED_DATA("GetLoggedData", "Getting Logged Data", GetLoggedDataResponse.class, 5000),
    GET_PAIR_KEY("GetPairKey", "Getting Pair Key", KeyExchangeResult.class, 10000),
    GET_SESSION_KEY("GetSessionKey", "Getting Session Key", KeyExchangeResult.class, 5000),
    GET_VERSION("GetVersion", "Getting Version", VersionRpc.class, 5000),
    INITIATE_UPGRADE("InitiateUpgrade", "Initiating upgrade", TransferBlockSizeRpc.class, 30000),
    SET("Set", "Setting", SetResponse.class, 5000),
    START_STREAM("StartStream", "Starting Stream Data", StreamResponse.class, 5000),
    SUBSCRIBE("SubscribeEvent", "Subscribing", SubscriptionResponse.class, 5000),
    UPGRADE_DATA_BLOCK("UpgradeDataBlock", "Upgrading data block", Boolean.class, 30000);
    
    private static final Map<String, RpcCommand> byMethod = g.E(RpcCommand.class, "getMethod");
    private final String description;
    private final String method;
    private final Class<? extends Serializable> resultClass;
    public final long timeout;

    RpcCommand(String str, String str2, Class cls, long j10) {
        this.method = str;
        this.description = str2;
        this.resultClass = cls;
        this.timeout = j10;
    }

    public static RpcCommand fromMethod(String str) {
        return byMethod.get(str);
    }

    public String getDescription() {
        return this.description;
    }

    public String getMethod() {
        return this.method;
    }

    public Class<? extends Serializable> getResultClass() {
        return this.resultClass;
    }

    public long getTimeout() {
        return this.timeout;
    }

    public boolean isLoggable() {
        return (this == GET_PAIR_KEY || this == GET_SESSION_KEY) ? false : true;
    }
}

## Setting Enum (all setting keys)
package com.resmed.mon.bluetooth.rpc.enums;

import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
/* loaded from: classes.dex */
public enum Setting {
    MODE("TherapyMode"),
    TUBE("Tube"),
    MASK("MaskPressure"),
    EPR_TYPE("EprType"),
    RAMP_ENABLE("RampEnable"),
    RAMP_TIME("RampSetting"),
    SMART_START("SmartStart"),
    SMART_STOP("SmartStop"),
    EPR_ENABLE("EprEnable"),
    PRESSURE("CPAP-SetPressure"),
    START_PRESSURE("CPAP-StartPressure"),
    AUTOSET_START_PRESSURE("AutoSet-StartPressure"),
    MINIMUM_PRESSURE("AutoSet-MinPressure"),
    MAXIMUM_PRESSURE("AutoSet-MaxPressure"),
    EPR_LEVEL("EprPressure"),
    FLOWGEN_STATE("FGState"),
    COMFORT("AutoSetComfort");
    
    protected static final List<Setting> orderedSettings;
    private final String key;

    /* loaded from: classes.dex */
    public static class SettingComparator implements Comparator<Setting> {
        @Override // java.util.Comparator
        public int compare(Setting setting, Setting setting2) {
            List<Setting> list = Setting.orderedSettings;
            return Integer.compare(list.indexOf(setting), list.indexOf(setting2));
        }
    }

    static {
        Setting setting;
        Setting setting2;
        Setting setting3;
        Setting setting4;
        Setting setting5;
        Setting setting6;
        Setting setting7;
        Setting setting8;
        Setting setting9;
        Setting setting10;
        Setting setting11;
        Setting setting12;
        Setting setting13;
        Setting setting14;
        Setting setting15;
        orderedSettings = Arrays.asList(setting3, setting4, setting12, setting8, setting11, setting10, setting9, r0, r0, setting, setting2, setting5, setting6, setting7, setting13, setting15, setting14);
    }

    Setting(String str) {
        this.key = str;
    }

    public String getKey() {
        return this.key;
    }
}

## RpcRequest (JSON-RPC 2.0 over BT SPP)
package com.resmed.mon.bluetooth.rpc.request;

import com.resmed.mon.bluetooth.rpc.RpcCommand;
import com.resmed.mon.bluetooth.rpc.response.ErrorRpc;
import com.resmed.mon.bluetooth.rpc.response.ResponseRpc;
import com.resmed.mon.utils.log.AppFileLog$LogType;
import com.resmed.mon.utils.text.c;
import j6.b;
import java.io.Serializable;
import net.sqlcipher.database.SQLiteDatabase;
/* loaded from: classes.dex */
public abstract class RpcRequest implements Serializable {
    public static final int NO_ID = -1;
    private transient RpcCallback callback;
    @b("method")
    private final String method;
    private transient ResponseRpc response;
    private transient int tag;
    @b("jsonrpc")
    private String jsonrpc = "2.0";
    @b("id")
    private int id = -1;

    /* renamed from: com.resmed.mon.bluetooth.rpc.request.RpcRequest$1  reason: invalid class name */
    /* loaded from: classes.dex */
    public static /* synthetic */ class AnonymousClass1 {
        static final /* synthetic */ int[] $SwitchMap$com$resmed$mon$bluetooth$rpc$RpcCommand;

        static {
            int[] iArr = new int[RpcCommand.values().length];

## BT Connection Layer (w7/c.java - AcceptConnectThread)
- UUID: 00001101-0000-1000-8000-00805F9B34FB (Classic SPP)
- Uses listenUsingRfcommWithServiceRecord("BluetoothConnection", ...)
- This is server-side (phone listens for device to connect)

## BT I/O Thread (w7/e.java - ConnectedThread)
- Raw byte stream over BluetoothSocket InputStream/OutputStream
- 2048-byte read buffer
- Received bytes are dispatched to j2/f.java (JSON-RPC parser)

## Key Findings Summary

### Transport Layer
- **Protocol**: Classic Bluetooth SPP (Serial Port Profile)
- **UUID**: `00001101-0000-1000-8000-00805F9B34FB`
- **Connection model**: Phone acts as SERVER (listenUsingRfcommWithServiceRecord) — device connects TO the phone
- **Framing**: NCP (Network Control Protocol) over serial — handled by native `libfiglib.so`
  - NCP has header with vcid (virtual channel ID) and CRC
  - Has encrypted and unencrypted modes (AES/CBC/NoPadding, 16-byte IV prepended)

### Application Layer
- **Protocol**: JSON-RPC 2.0 over NCP/SPP
- **Format**: `{"jsonrpc": "2.0", "method": "<method>", "id": <int>, "params": {...}}`
- **Serialization**: Google GSON
- **Spec file**: `assets/AppRpcSpec.json` maps method names to versions

### RPC Methods (all v1.0 unless noted)
| Method | Purpose | Key Params |
|--------|---------|------------|
| `GetVersion` v2.0 | Get firmware info | none |
| `Get` | Get settings | `params: ["SettingKey"]` |
| `Set` | Set settings | `params: {key: value}` |
| `GetPairKey` | Pairing exchange | `params.passKey: string` → returns `masterPairKey` |
| `GetSessionKey` | Auth exchange | `params.masterPairKey: string` → returns `sessionKey` |
| `GetDateTime` | Get device datetime | none |
| `GetLoggedData` | Request logged therapy data | `params: [{dataId, fromTime}]` → returns `logStreamId` |
| `GetHistory` | Get settings history | params with setting key |
| `EnterTherapy` | Start CPAP therapy | none |
| `EnterStandby` | Stop therapy | none |
| `EnterMaskFit` | Start mask fit mode | `params: float (pressure)` |
| `SubscribeEvent` | Subscribe to live events | subscription id |
| `StartStream` | Start 25Hz data stream | params |
| `EraseData` | Erase device data | params |
| `BtDisconnect` | Graceful disconnect | none |
| `GenerateAuthCode` v1.1 | Auth code for firmware | params |
| `InitiateUpgrade`, `UpgradeDataBlock`, `ApplyAuthenticatedUpgrade`, `CheckUpgradeFile` | OTA firmware | - |
| `DiscardPairKey` | Unpair device | none |

### Settings Keys (from Setting enum)
| Enum | JSON Key | Description |
|------|---------|-------------|
| MODE | `TherapyMode` | CPAP/AutoSet mode |
| TUBE | `Tube` | Tube type |
| MASK | `MaskPressure` | Mask pressure |
| EPR_TYPE | `EprType` | EPR type |
| RAMP_ENABLE | `RampEnable` | Ramp on/off |
| RAMP_TIME | `RampSetting` | Ramp duration |
| SMART_START | `SmartStart` | Smart start |
| SMART_STOP | `SmartStop` | Smart stop |
| EPR_ENABLE | `EprEnable` | EPR on/off |
| PRESSURE | `CPAP-SetPressure` | Fixed CPAP pressure |
| START_PRESSURE | `CPAP-StartPressure` | CPAP start pressure |
| AUTOSET_START_PRESSURE | `AutoSet-StartPressure` | AutoSet start pressure |
| MINIMUM_PRESSURE | `AutoSet-MinPressure` | AutoSet min pressure |
| MAXIMUM_PRESSURE | `AutoSet-MaxPressure` | AutoSet max pressure |
| EPR_LEVEL | `EprPressure` | EPR pressure level |
| FLOWGEN_STATE | `FGState` | Flow generator state |
| COMFORT | `AutoSetComfort` | AutoSet comfort mode |

### Logged Data Types (from DataType enum — used with GetLoggedData)
| dataId string | Description | Container |
|--------------|-------------|-----------|
| `UsageEvents-TherapyStatusEvent` (MASK) | Mask on/off events | EVENTS |
| `TherapyEvents-RespiratoryEvent` (RESPIRATORY) | Apnea/hypopnea events | EVENTS |
| `TherapyOneMinutePeriodic-InspiratoryPressure` (IPAP) | Pressure every 1 min | PERIODIC |
| `TherapyOneMinutePeriodic-Leak` (LEAK) | Leak every 1 min | PERIODIC |
| `Diagnostic25HzPeriodic-BlowerFlow` (FLOW_25Hz) | Flow at 25Hz | PERIODIC |
| `Diagnostic25HzPeriodic-BlowerPressure` (PRESS_25Hz) | Pressure at 25Hz | PERIODIC |
| `DiagnosticExceptionEvents-AppError` | App errors | EVENTS |
| `DiagnosticExceptionEvents-FatalError` | Fatal errors | EVENTS |
| `DiagnosticExceptionEvents-ErrorLogInfo` | Error log info | EVENTS |
| `DiagnosticExceptionEvents-ResettableError` | Resettable errors | EVENTS |
| `SystemExceptionEvents-RecoverableError` | Recoverable errors | EVENTS |
| `SystemExceptionEvents-SystemError` | System errors | EVENTS |
| `SystemActivityEvents-SporadicActivityEvent` | Sporadic activity | EVENTS |
| `SystemActivityEvents-FrequentActivityEvent` | Frequent activity | EVENTS |

### Sleep Event Types (mapped in GetLoggedDataNotification.EventType)
APNEA, HYPOPNEA, CENTRAL_APNEA, OBSTRUCTIVE_APNEA, AROUSAL, CSR_START, CSR_END
(plus many system/error events)

### Periodic Data Format
- `startTime`: ISO datetime
- `interval`: Float (seconds between samples — 60 for 1-min, 0.04 for 25Hz)
- `values`: Float[] array of measurements

### Event Data Format
- `time`: ISO datetime
- `event`: EventType string
- `durationSeconds`: Integer
- `backdateSeconds`: Integer

### Authentication/Pairing Flow
1. Phone connects to device via SPP
2. `GetPairKey({passKey})` → returns `{masterPairKey, sessionKey}`
3. `GetSessionKey({masterPairKey})` → returns new `sessionKey`
4. Session key used for AES/CBC encryption via FigWrapper

### MachineMetrics Fields
- `LastTherapyUseDateTime`
- `LastEraseDataDateTime`
- `TherapyRunMeter` (ISO 8601 Period string, e.g. "PT324H")
- `MotorRunMeter`
- `MotorRunSinceLastServiceMeter`
- `MachineRunMeter`

### Sync Triggers
Data synced after: Stop, OnAuthentication, Heartbeat, OnDemand, Manual, HeartbeatAtMidnight
Data types: MeasurementProfiles, FGLogs, Settings, MachineMetrics

---

## Python Implementation Path

**Use PyBluez or pybluetooth (classic BT SPP):**
```python
import bluetooth
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((device_address, 1))  # channel 1 for SPP
```

**Or socket directly:**
```python
import socket
sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
sock.connect((mac_address, 1))
```

**Framing challenge**: Data goes through `libfiglib.so` NCP framing (native C++).
The NCP layer adds/removes framing bytes (header + CRC). This is **not trivially reversible** without reverse-engineering `libfiglib.so`.

**Options**:
1. **Sniffer approach**: Use Wireshark + Bluetooth sniffer to capture raw SPP packets between phone and device, then reverse-engineer NCP framing empirically
2. **RE libfiglib.so**: Use Ghidra/IDA to decompile the native library and extract NCP frame format
3. **OSCAR project**: Check if openSleep/OSCAR already has this protocol documented (they may have done this work)
4. **Man-in-the-middle**: Use Python to act as a BT proxy between phone and device

**Minimal PoC (without NCP framing)**:
```python
# JSON-RPC 2.0 payload structure (before NCP wrapping):
import json
request = {
    "jsonrpc": "2.0",
    "method": "GetVersion",
    "id": 1
}
payload = json.dumps(request)
# Then encode through NCP (unknown format)
```

---

## Gaps Requiring Hardware / Further Analysis

1. **NCP frame format**: libfiglib.so handles framing — exact byte structure unknown from static analysis alone. Need hardware sniffing or libfiglib.so RE.
2. **passKey for pairing**: What value/format the passKey takes (PIN from device display? Fixed?)
3. **Session key usage**: Whether the sessionKey must be re-exchanged each connection, or if masterPairKey is stored persistently
4. **Encryption toggle**: When encrypted vs unencrypted FigWrapper is used
5. **Channel assignment**: Which vcid (virtual channel) carries RPC vs data vs control
6. **BluetoothSocket channel**: SPP typically uses RFCOMM channel from SDP lookup, not hardcoded channel 1
7. **Device name format**: AirMini device BT name format for discovery (e.g. "AirMini-XXXXXX")
