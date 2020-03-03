import RPi.GPIO as GPIO
import time
def bulb_on():
    in1=23

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(in1,GPIO.OUT)
    #GPIO.setup(in2,GPIO.OUT)


    GPIO.output(in1,GPIO.LOW)


def bulb_off():
    in1 = 23

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(in1, GPIO.OUT)
    # GPIO.setup(in2,GPIO.OUT)

    GPIO.output(in1, GPIO.HIGH)


#GPIO.output(in2,False)

#time.sleep(5)

#GPIO.output(in1,GPIO.HIGH)

#time.sleep(4)

#GPIO.output(in1,GPIO.LOW)