import RPi.GPIO as GPIO
import time

import servo1
import bulb
import dc_motor1
import dc_motor2
import dht11
import rain_module

import json

def writeJSON(data):
    #print(data)
    file = open("data.json", 'w')
    json.dump(data, file)
    file.close()


dc_data=""
bulb_data=""


flag_dc=0
flag_bulb=0



rain=rain_module.rain()

if rain=="1" and flag_dc==0:
    dc_motor2.dc_motor_down()
    flag_dc = 1
elif rain=="1" and flag_dc==1:
    print("already down")

if rain=="0" and flag_dc==1:
    motor = dc_motor1.dc_motor_up()
    flag_dc = 0

elif rain=="0" and flag_dc==0:
    print("already up")





if dc_data=="down" and flag_dc==0:
    dc_motor2.dc_motor_down()
    flag_dc=1

elif dc_data=="down" and flag_dc==1:
    print("already down")


if dc_data=="up" and flag_dc==1:
    motor=dc_motor1.dc_motor_up()
    flag_dc=0
elif dc_data=="up" and flag_dc==0:
    print("already up")





if bulb=="on" and flag_bulb==0:
    bulb.bulb_on()
elif bulb=="on" and flag_bulb==1:
    print("Light already on")

if bulb=="off" and flag_bulb==1:
    bulb.bulb_off()
elif bulb=="off" and flag_bulb==0:
    print("Light already off")


servo1.servo1()
t,h=dht11.temp()

#---------------------------------------------------------------------------------------------------------------------------------
data = {
    "data" : [
        {
            "temp" : t,
            "humidty" : h,
            "flap" : flag_dc,
            "bulb": flag_bulb,
            "rain": rain
        }
    ]
}

writeJSON(data)


#----------------------------------------------------------------------------------------------------------------------------------


while True:
    rain = rain_module.rain()

    if rain == "1" and flag_dc == 0:
        dc_motor2.dc_motor_down()
        flag_dc = 1
    elif rain == "1" and flag_dc == 1:
        print("already down")

    if rain == "0" and flag_dc == 1:
        motor = dc_motor1.dc_motor_up()
        flag_dc = 0

    elif rain == "0" and flag_dc == 0:
        print("already up")

    if dc_data == "down" and flag_dc == 0:
        dc_motor2.dc_motor_down()
        flag_dc = 1

    elif dc_data == "down" and flag_dc == 1:
        print("already down")

    if dc_data == "up" and flag_dc == 1:
        motor = dc_motor1.dc_motor_up()
        flag_dc = 0
    elif dc_data == "up" and flag_dc == 0:
        print("already up")

    if bulb == "on" and flag_bulb == 0:
        bulb.bulb_on()
    elif bulb == "on" and flag_bulb == 1:
        print("Light already on")

    if bulb == "off" and flag_bulb == 1:
        bulb.bulb_off()
    elif bulb == "off" and flag_bulb == 0:
        print("Light already off")

    servo1.servo1()
    t, h = dht11.temp()


    data_2 = {
        "temp": t,
        "humidity": h,
        "flap": flag_dc,
        "bulb": flag_bulb,
        "rain": rain
    }

    if data["data"][0]["temp"] == data_2["temp"] and data["data"][0]["humidity"] == data_2["humidity"] and data["data"][0]["flap"] == data_2["flap"] and data["data"][0]["bulb"] == data_2["bulb"] and data["data"][0]["rain"] == data_2["rain"]:
        print("Inside If")
    else:
        print("Inside Else")
        data["data"][0]["temp"] = data_2["temp"]
        data["data"][0]["humidity"] = data_2["humidity"]
        data["data"][0]["flap"] = data_2["flap"]
        data["data"][0]["bulb"] = data_2["bulb"]
        data["data"][0]["rain"] = data_2["rain"]

        writeJSON(data)