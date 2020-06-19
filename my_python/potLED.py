import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.PWM as PWM
from time import sleep
LED="P9_14"
pot="P9_33"
ADC.setup()
PWM.start(LED,0,1000)
while(1):
    analogRead=ADC.read(pot)
    dutyCycle=(101**analogRead)-1
    print(dutyCycle)
    PWM.set_duty_cycle(LED,dutyCycle)
    sleep(0.2)
