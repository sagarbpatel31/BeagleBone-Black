import Adafruit_BBIO.PWM as PWM
myPWM="P8_13"
PWM.start(myPWM,0,1000)
from time import sleep
for i in range(5):
    dc=float(input("What voltage would you like? "))
    dc=(dc/3.365)*100
    if (dc>100):
        dc=100
    PWM.set_duty_cycle(myPWM,dc)
PWM.stop(myPWM)
PWM.cleanup()
