# policeLights.py
from machine import Pin
import utime

sleepBetween = 0.3
blinkTime = 0.1

blueLED = Pin(28, Pin.OUT)
redLED = Pin(5, Pin.OUT)

blueLED.high()
redLED.low()

while True:
    for i in range(3):
        redLED.low()
        blueLED.toggle()
        utime.sleep(blinkTime)

    utime.sleep(sleepBetween)
    for i in range(3):
        blueLED.low()
        redLED.toggle()
        utime.sleep(blinkTime)
    utime.sleep(sleepBetween)
    
 