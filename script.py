from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import configparser as conf
import json
from datetime import datetime
import random as r
import time
import serial

config = conf.ConfigParser()
CLIENT = "RPi1"
config.read("config")
HOST_NAME = config["HOST"]["NAME"]
ROOT_CA = config["CERTI"]["ROOT"]
PRIVATE_KEY = config["CERTI"]["PRIVATE_KEY"]
CERT_FILE = config["CERTI"]["CERT_FILE"]
SHADOW_HANDLER = "RPi1"


ser = serial.Serial("/dev/ttyUSB0", 115200)

myShadowClient = AWSIoTMQTTClient(CLIENT)
myShadowClient.configureEndpoint(HOST_NAME, 8883)
myShadowClient.configureCredentials(ROOT_CA, PRIVATE_KEY, CERT_FILE)
myShadowClient.configureConnectDisconnectTimeout(10)
myShadowClient.configureMQTTOperationTimeout(5)
myShadowClient.connect()
'''a = {
        "deviceID": CLIENT,
        "timestamp": datetime.timestamp(datetime.now()),
        "data": {
            "temperature": r.uniform(10.5, 1000.5),
            "co": float(ser.readline()),
            #"co": r.uniform(10.5, 1000.5),
            "sox": r.uniform(10.5, 1000.5),
            "o3": r.uniform(10.5, 1000.5),
            "nox": r.uniform(10.5, 1000.5),
            "pm25": r.uniform(10.5, 1000.5),
            "pm10": r.uniform(10.5, 1000.5)
        }'''
while True:
    print("sending")
    a = {
        "deviceID": CLIENT,
        "timestamp": datetime.timestamp(datetime.now()),
        "data": {
            "temperature": r.uniform(10.5, 1000.5),
            "co": float(ser.readline()),
            #"co": r.uniform(10.5, 1000.5),
            "sox": r.uniform(10.5, 1000.5),
            "o3": r.uniform(10.5, 1000.5),
            "nox": r.uniform(10.5, 1000.5),
            "pm25": r.uniform(10.5, 1000.5),
            "pm10": r.uniform(10.5, 1000.5)
        }
    }
    myShadowClient.publish("data", json.dumps(a), 0)
    time.sleep(10)

