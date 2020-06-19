import Adafruit_BBIO.GPIO as GPIO
outPin="P8_17"
GPIO.setup(outPin,GPIO.OUT)
from time import sleep
for i in range(5):
    GPIO.output(outPin,GPIO.HIGH)
    sleep(1)
    GPIO.output(outPin,GPIO.LOW)
    sleep(1)    
GPIO.cleanup()
