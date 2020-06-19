import Adafruit_BBIO.ADC as ADC
ADC.setup()
from time import sleep
analogPin="P9_33"
while(1):
    potVal=ADC.read(analogPin)
    potVolt=potVal*1.8
    print("Potentiometer value (in volts) is: ",potVolt)
    sleep(0.5)

