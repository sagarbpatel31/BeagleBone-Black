import Adafruit_BBIO.PWM as PWM
tLED="P9_14"
bLED="P9_22"
PWM.start(tLED,0,1000)
PWM.start(bLED,0,1000)
for i in range(5):
    tB=int(input("Brightness of Top LED? (0-7) "))
    bB=int(input("Brightness of Bottom LED? (0-7) "))
    tbdc=2**tB
    bbdc=2**bB
    if(tbdc>100):
        tbdc=100
    if(bbdc>100):
        bbdc=100
    PWM.set_duty_cycle(tLED,tbdc)
    PWM.set_duty_cycle(bLED,bbdc)
PWM.stop(tLED)
PWM.stop(bLED)
PWM.cleanup()
