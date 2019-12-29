import datetimeString

date = datetimeString.dateString()
nullSensor = {
    "Date": date,
    "DeviceID": int(date)+00+00,
    "Device Type": 00
}
deviceList = [nullSensor]

def idCreator(devicetype=None):
    """
    :param devicetype:
    :type string:
    :return:
    """
    lastDevice = deviceList[-1]
    lastDeviceDay = lastDevice["Date"]
    lastDeviceDay = lastDeviceDay[4:]


idCreator()