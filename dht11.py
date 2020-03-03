import sys
import Adafruit_DHT

def temp():
    h,t=Adafruit_DHT.read_retry(11,4)
    #print('temp:{0:0.1f} C Humidity:{1:0.1f} %'.format(t,h))
    return(t,h)
