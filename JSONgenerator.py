import json
import datetimeString
import random

IDS =   {
    "HUB_ID" : 2019091901001,
    "PRESSURE_STATION_ID": 2019091902001,
    "WEATHER_STATION_ID": 2019091903001,
    "SOIL_SENSOR_ID": 2019091904001,
    "SOIL_SENSOR_ID2": 2019091904001,
    "SOIL_SENSOR_ID3": 2019091904001,
}
sensors =   {
    "Weather Station" : 1,
    "Soil Sensor" : 2
}

def sensordata(sensorD):
    """
    :param sensor :
    :type int:
    :return sensordatagenerate:
    """
    sensor = {"ID": "1234"}
    for i in sensors.values():
        if sensorD == i:
            sensor["A_Q"] = random.randrange(0, 1001)
            sensor["A_T"] = random.randrange(-45, 65)
            sensor["A_H"] = random.randrange(0, 101)
            sensor["RAIN"] = random.randrange(0, 5)
        if sensorD == i:
            sensor["S30M"] = random.randrange(0,101)
            sensor["S60M"] = random.randrange(0,101)
            sensor["S90M"] = random.randrange(0,101)
            sensor["SD_T"] = random.randrange(-45,65)
            sensor["SU_T"] = random.randrange(-45,65)
        sensor["B_L"] = random.randrange(0, 4)
        sensor["RF_Q"] = random.randrange(0, 4)
        sensor["ERR"] = random.randrange(0, 4)
    return sensor

sensorslist = [sensordata(1), sensordata(2), sensordata(2)]

sendData = {
    "HUB_ID": "123456",
    "SENSORS": sensorslist,
    "B_AC": 1,
    "DATE": datetimeString.dateString(),
    "TIME": datetimeString.timeString()
}

def sensorDataJSON():
    jsonSendData = json.dumps(sendData)
    return jsonSendData

