#!/usr/bin/python3

import signal
import os
#import time
from time import sleep
from subprocess import check_output
from gpiozero import PWMLED, Button, LED, LEDBoard

prev=PWMLED(5)
play=PWMLED(6)
next=PWMLED(22)
volup=PWMLED(24)
voldown=PWMLED(23)

def sigterm_handler(signal, frame):
    prev.off()
    sleep(0.1)
    play.off()
    sleep(0.1)
    next.off()
    sleep(0.1)
    voldown.off()
    sleep(0.1)
    volup.off()
    sleep(0.1)
    os._exit(0)

def GetShell():
    process = check_output("/bin/ps -ef | grep mpd | grep -v grep | awk '{print $2}'", shell=True)
    process = process.decode()
    return process

signal.signal(signal.SIGTERM, sigterm_handler)

def LedOn(ledname):
    for x in range(100):
        ledname.value = x * 0.001
        sleep(0.02)

def LedOff(ledname):
    for x in range(100,-1,-1):
        ledname.value = x * 0.001
        sleep(0.02)

process=""
pos = 1
direction = 0
while process == "":
    print( process )
    if pos == 1:
        #LedOn(prev)
        prev.pulse(n=1,fade_in_time=0.2,fade_out_time=0.5)
        #if direction == 1:
        sleep(0.2)
        direction = 0
    elif pos == 2:
        play.pulse(n=1,fade_in_time=0.2,fade_out_time=0.4)
    elif pos == 3:
        next.pulse(n=1,fade_in_time=0.2,fade_out_time=0.3)
    elif pos == 4:
        voldown.pulse(n=1,fade_in_time=0.2,fade_out_time=0.4)
    elif pos == 5:
        volup.pulse(n=1,fade_in_time=0.2,fade_out_time=0.5)
        process=GetShell()
        #pos = 0
        direction = 1
        sleep(0.2)
    if direction == 0:
        pos += 1
    else:
        pos -= 1
    sleep(0.09)

prev.on()
sleep(0.1)
play.on()
sleep(0.1)
next.on()
sleep(0.1)
voldown.on()
sleep(0.1)
volup.on()

signal.pause()
