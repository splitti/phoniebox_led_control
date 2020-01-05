#!/usr/bin/python3

import signal
import sys
from subprocess import check_output
from time import sleep

from gpiozero import PWMLED

LED_PREV = PWMLED(5)
LED_PLAY = PWMLED(6)
LED_NEXT = PWMLED(22)
LED_VOLUP = PWMLED(24)
LED_VOLDOWN = PWMLED(23)

#ALL_GPIO = [LED_PREV, LED_PLAY, LED_NEXT, LED_VOLUP, LED_VOLDOWN]

def sigterm_handler(*_):
    LED_PREV.off()
    LED_PREV.close()
    sleep(0.1)
    LED_PLAY.off()
    LED_PLAY.close()
    sleep(0.1)
    LED_NEXT.off()
    LED_NEXT.close()
    sleep(0.1)
    LED_VOLDOWN.off()
    LED_VOLDOWN.close()
    sleep(0.1)
    LED_VOLUP.off()
    LED_VOLUP.close()
#    for device in ALL_GPIO:
#        device.off()
#        device.close()
    sys.exit(0)


def getshell():
    process = check_output("/bin/ps -ef | grep mpd | grep -v grep | awk '{print $2}'", shell=True)
    process = process.decode()
    return process


#def ledon(ledname):
#    for x in range(100):
#        ledname.value = x * 0.001
#        sleep(0.02)


#def ledoff(ledname):
#    for x in range(100, -1, -1):
#        ledname.value = x * 0.001
#        sleep(0.02)

def initiate_animation():
    process = ""
    pos = 1
    direction = 0
    while process == "":
        print(process)
        if pos == 1:
            LED_PREV.pulse(n=1, fade_in_time=0.2, fade_out_time=0.5)
            sleep(0.1)
            direction = 0
        elif pos == 2:
            LED_PLAY.pulse(n=1, fade_in_time=0.2, fade_out_time=0.4)
            sleep(0.05)
        elif pos == 3:
            LED_NEXT.pulse(n=1, fade_in_time=0.2, fade_out_time=0.3)
        elif pos == 4:
            LED_VOLDOWN.pulse(n=1, fade_in_time=0.2, fade_out_time=0.4)
            sleep(0.05)
        elif pos == 5:
            LED_VOLUP.pulse(n=1, fade_in_time=0.2, fade_out_time=0.5)
            process = getshell()
            direction = 1
            sleep(0.1)
        if direction == 0:
            pos += 1
        else:
            pos -= 1
        sleep(0.07)

def leds_on():
    LED_PREV.on()
    sleep(0.1)
    LED_PLAY.on()
    sleep(0.1)
    LED_NEXT.on()
    sleep(0.1)
    LED_VOLDOWN.on()
    sleep(0.1)
    LED_VOLUP.on()

def main():
    dummy = ""
    while dummy == "":
        sleep(5)


if __name__ == "__main__":
    initiate_animation()
    leds_on()
    signal.signal(signal.SIGTERM, sigterm_handler)
    main()
