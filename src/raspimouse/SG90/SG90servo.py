'''
SG90 servo controller for raspberry pi mouse
'''

import RPi.GPIO as GPIO

class SG90servo():
    def __init__(self,motorport=2):
        self.port = motorport
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.port, GPIO.OUT)
        self.servo = GPIO.PWM(self.port, 50)

        self.servo.start(0.0) # set duty cicle to 0-100
        self.minlim = -90
        self.maxlim = 90

    def servo_deg(self,deg):

        if deg > self.maxlim:
            print("Exceed max degree!")
            return
        elif deg < self.minlim:
            print("Exceed min degree!")
            return
        
        cycle = 7.25+4.75*deg/90.0
        self.servo.ChangeDutyCycle(cycle)

    def stop(self):
        self.servo.start(0.0)
