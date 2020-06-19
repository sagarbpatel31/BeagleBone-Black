import Adafruit_BBIO.GPIO as GPIO
LEDTop="P9_12"
LEDBottom="P9_11"
GPIO.setup(LEDTop,GPIO.OUT)
GPIO.setup(LEDBottom,GPIO.OUT)
delay=float(input("How Long to Delay? "))
noblinks=int(input("How many blinks do you want? "))
from time import sleep
for i in range(noblinks):
    GPIO.output(LEDTop,GPIO.HIGH)
    GPIO.output(LEDBottom,GPIO.LOW)
    sleep(delay)
    GPIO.output(LEDTop,GPIO.LOW)
    GPIO.output(LEDBottom,GPIO.HIGH)
    sleep(delay)
GPIO.output(LEDBottom,GPIO.LOW)
GPIO.cleanup()
