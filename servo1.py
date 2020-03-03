import RPi.GPIO as GPIO
import time




    
def servo1():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(17,GPIO.OUT)
    servo1=GPIO.PWM(17,50)

    servo1.start(1)
        #time.sleep(1)
    servo1.ChangeDutyCycle(1)
    time.sleep(0.6)
        #servo1.ChangeDutyCycle(2.5)
        #time.sleep(1)
    servo1.ChangeDutyCycle(12.5)
    time.sleep(0.6)
    servo1.stop()
        


    

#while True:
#servo1()
    

#GPIO.cleanup()
#print('done')