import Adafruit_BBIO.PWM as PWM
servoPin="P9_14"
PWM.start(servoPin,5,50)
while(1):
    dutyCycle=float(input("What duty cycle? "))
    PWM.set_duty_cycle(servoPin,dutyCycle)
