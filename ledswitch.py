#!/usr/bin/env python
# refference code:
#  https://www.sunfounder.com/learn/super_kit_v2_for_raspberrypi/lesson-2-contr$
# coral enviromental sensor board 08-22-2019 
# sample python code to  use onboard LED and switch
import RPi.GPIO as GPIO
import time

LedPin = 40    # pin40 Not gpio --- led
BtnPin = 16    # pin16 Not gpio --- button

Led_status = 1

def setup():
        GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
        GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
        GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's$
        GPIO.output(LedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to off led

def swLed(ev=None):
        global Led_status
        Led_status = not Led_status
        GPIO.output(LedPin, Led_status)  # switch led status(on-->off; off-->on)
        if Led_status == 1:
                print 'led off...'
        else:
                print '...led on'

def loop():
        GPIO.add_event_detect(BtnPin, GPIO.FALLING, callback=swLed, bouncetime=$
        while True:
                time.sleep(1)   # Don't do anything

def destroy():
        GPIO.output(LedPin, GPIO.HIGH)     # led off
        GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
        setup()
        try:
                loop()
        except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child progra$
                destroy()

