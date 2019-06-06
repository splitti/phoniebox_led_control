#!/usr/bin/python3

import signal
import os
#import time
from time import sleep
import RPi.GPIO as GPIO
from subprocess import check_output


prev=5
play=6
next=22
volup=24
voldown=23

def sigterm_handler(signal, frame):
    GPIO.output(volup,GPIO.LOW)
    sleep(0.1)
    GPIO.output(voldown,GPIO.LOW)
    sleep(0.1)
    GPIO.output(next,GPIO.LOW)
    sleep(0.1)
    GPIO.output(play,GPIO.LOW)
    sleep(0.1)
    GPIO.output(prev,GPIO.LOW)
    os._exit(0)

def GetShell():
    process = check_output("/bin/ps -ef | grep mpd | grep -v grep | awk '{print $2}'", shell=True)
    process = process.decode()
    return process

signal.signal(signal.SIGTERM, sigterm_handler)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(next,GPIO.OUT)
GPIO.setup(volup,GPIO.OUT)
GPIO.setup(voldown,GPIO.OUT)
GPIO.setup(prev,GPIO.OUT)
GPIO.setup(play,GPIO.OUT)

process=""
pos = 1
while process == "":
    print( process )
    if pos == 1:
        GPIO.output(prev,GPIO.HIGH)
    elif pos == 2:
        GPIO.output(play,GPIO.HIGH)
    elif pos == 3:
        GPIO.output(next,GPIO.HIGH)
    elif pos == 4:
        GPIO.output(voldown,GPIO.HIGH)
    elif pos == 5:
        GPIO.output(volup,GPIO.HIGH)
        process=GetShell()
    elif pos == 6:
        GPIO.output(prev,GPIO.LOW)
    elif pos == 7:
        GPIO.output(play,GPIO.LOW)
    elif pos == 8:
        GPIO.output(next,GPIO.LOW)
    elif pos == 9:
        GPIO.output(voldown,GPIO.LOW)
    elif pos == 10:
        GPIO.output(volup,GPIO.LOW)    
        pos = 0
    pos += 1
    sleep(0.05)
dummy = ""
while dummy == "":
    dummy = ""
    sleep(3600)
