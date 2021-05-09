import serial
from flask import *
import pymongo
import datetime
import time



#ser = serial.Serial("/dev/ttyUSB0",9600)
ser = serial.Serial("COM27",9600)
# client = pymongo.MongoClient("mongodb://kunal:sahni1@ds125578.mlab.com:25578/ietmakeathon")

client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.uxhm5.mongodb.net/capstone?retryWrites=true&w=majority")
# db = client['ietmakeathon']
db = client['capstone']


raindb = db.rain_sensor
tempdb = db.dht_sensor
radiation_db = db.light_sensor
firedb = db.fire_sensor
moistdb = db.moisture_sensor

while True:
    if (ser.in_waiting > 0):
        line = ser.readline()
        status = list(line.decode().rstrip().split(","))
        print(status)
        # [LDR, Moisture, rain, flame, temp, humidity]

        glow = status[0]
        moist = status[1]
        rain_status = status[2]
        heat = status[3]
        temp = status[4]
        humidity = status[5]

        tempdb.insert({
         "time" : str(datetime.datetime.now().strftime("%d-%m-%Y : %I:%M:%S")),
         "temp" : temp,
         "humidity" : humidity,
        })


        raindb.insert({
         "time":str(datetime.datetime.now().strftime("%d-%m-%Y : %I:%M:%S")),
          "status" : rain_status,
         })


        firedb.insert({
          "time":str(datetime.datetime.now().strftime("%d-%m-%Y : %I:%M:%S")),
            "status" : heat,
        })

        radiation_db.insert({
          "time":str(datetime.datetime.now().strftime("%d-%m-%Y : %I:%M:%S")),
            "status" : glow,
        })

        moistdb.insert({
          "time":str(datetime.datetime.now().strftime("%d-%m-%Y : %I:%M:%S")),
            "status" : moist,
        })

        time.sleep(3)
