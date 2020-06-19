import Adafruit_BBIO.PWM as PWM
servoPin="P9_14"
PWM.start(servoPin,2,50)
while(1):
    desiredAngle=int(input("What angle do you want? "))
    dutyCycle=((1./15)*desiredAngle)+1
    PWM.set_duty_cycle(servoPin,dutyCycle)
