#!/usr/bin/env python3
import tinytuya
from time import sleep
import RPi.GPIO as GPIO

ledPin = 12 # define ledPin
sensorPin = 11 # define sensorPin

DEVICE_ID_HERE = "bfc42a284525d9d92d6tx0"
IP_ADDRESS = "192.168.0.144"
LOCAL_KEY = "8d3d84ef517b3338"


def setup():
        GPIO.setmode(GPIO.BOARD) # use PHYSICAL GPIO Numbering
        GPIO.setup(ledPin, GPIO.OUT) # set ledPin to OUTPUT mode
        GPIO.setup(sensorPin, GPIO.IN) # set sensorPin to INPUT mode
        d = tinytuya.OutletDevice(DEVICE_ID_HERE, IP_ADDRESS, LOCAL_KEY, 'device22')
        d.set_version(3.3)
        d.set_dpsUsed({"1": None})
        data = d.status()  # NOTE this does NOT require a valid key vor version 3.1
        data = d.set_status(False) # socket is off
        return d

def loop(d):
        while True:
                if GPIO.input(sensorPin)==GPIO.HIGH:
                        GPIO.output(ledPin,GPIO.HIGH) # turn on led
                        data = d.set_status(True) # socket is off
                        print ('plug is on')
                        sleep(60)
                        data = d.set_status(False)
                        print ('plug is off')
                else :
                        GPIO.output(ledPin,GPIO.LOW) # turn off led
#                        print ('led turned off <<<')
