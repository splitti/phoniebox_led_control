#!/usr/bin/python3

import signal
import os
#import time
from time import sleep
from subprocess import check_output
from gpiozero import PWMLED, Button, LED, LEDBoard

led_prev=PWMLED(5)
led_play=PWMLED(6)
led_next=PWMLED(22)
led_volup=PWMLED(24)
led_voldown=PWMLED(23)

def sigterm_handler(signal, frame):
    led_prev.off()
    sleep(0.1)
    led_play.off()
    sleep(0.1)
    led_next.off()
    sleep(0.1)
    led_voldown.off()
    sleep(0.1)
    led_volup.off()
    sleep(0.1)
    os._exit(0)

def getshell():
    process = check_output("/bin/ps -ef | grep mpd | grep -v grep | awk '{print $2}'", shell=True)
    process = process.decode()
    return process

signal.signal(signal.SIGTERM, sigterm_handler)

def ledon(ledname):
    for x in range(100):
        ledname.value = x * 0.001
        sleep(0.02)

def ledoff(ledname):
    for x in range(100,-1,-1):
        ledname.value = x * 0.001
        sleep(0.02)

process=""
pos = 1
direction = 0
while process == "":
    print( process )
    if pos == 1:
        #ledon(led_prev)
        led_prev.pulse(n=1,fade_in_time=0.2,fade_out_time=0.5)
        #if direction == 1:
        sleep(0.2)
        direction = 0
    elif pos == 2:
        led_play.pulse(n=1,fade_in_time=0.2,fade_out_time=0.4)
    elif pos == 3:
        led_next.pulse(n=1,fade_in_time=0.2,fade_out_time=0.3)
    elif pos == 4:
        led_voldown.pulse(n=1,fade_in_time=0.2,fade_out_time=0.4)
    elif pos == 5:
        led_volup.pulse(n=1,fade_in_time=0.2,fade_out_time=0.5)
        process=getshell()
        #pos = 0
        direction = 1
        sleep(0.2)
    if direction == 0:
        pos += 1
    else:
        pos -= 1
    sleep(0.09)

led_prev.on()
sleep(0.1)
led_play.on()
sleep(0.1)
led_next.on()
sleep(0.1)
led_voldown.on()
sleep(0.1)
led_volup.on()

signal.pause()
