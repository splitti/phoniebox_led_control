#!/usr/bin/python3

import signal
import sys
from subprocess import check_output
from time import sleep

from gpiozero import PWMLED


LED_VOLDOWN = PWMLED(5)
LED_PREV = PWMLED(6)
LED_PLAY = PWMLED(23)
LED_NEXT = PWMLED(22)
LED_VOLUP = PWMLED(24)

#ALL_GPIO = [LED_PREV, LED_PLAY, LED_NEXT, LED_VOLUP, LED_VOLDOWN]

def sigterm_handler(*_):
    LED_VOLDOWN.off()
    LED_VOLUP.off()
    LED_VOLDOWN.close()
    LED_VOLUP.close()
    sleep(0.1)
    LED_PREV.off()
    LED_NEXT.off()
    LED_PREV.close()
    LED_NEXT.close()
    sleep(0.1)
    LED_PLAY.off()
    LED_PLAY.close()
#    for device in ALL_GPIO:
#        device.off()
#        device.close()
    sys.exit(0)


def getshell():
    process = check_output("/bin/ps -ef | grep mopidy | grep -v grep | awk '{print $2}'", shell=True)
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
            LED_PLAY.pulse(n=1, fade_in_time=0.2, fade_out_time=0.8)
            sleep(0.2)
        elif pos == 2:
            LED_PREV.pulse(n=1, fade_in_time=0.2, fade_out_time=0.8)
            LED_NEXT.pulse(n=1, fade_in_time=0.2, fade_out_time=0.8)
            sleep(0.2)
        elif pos == 3:
            LED_VOLUP.pulse(n=1, fade_in_time=0.2, fade_out_time=0.8)
            LED_VOLDOWN.pulse(n=1, fade_in_time=0.2, fade_out_time=0.8)
            process = getshell()
            sleep(0.8)
            pos=0
        pos += 1
        sleep(0.04)

def leds_on():
    LED_PLAY.on()
    sleep(0.1)
    LED_PREV.on()
    LED_NEXT.on()
    sleep(0.1)
    LED_VOLDOWN.on()
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
