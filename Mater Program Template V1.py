#!/usr/bin/env python3
from ev3dev.ev3 import *
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank, MediumMotor, OUTPUT_D, OUTPUT_A 
from time import sleep
from ev3dev2.motor import Motor, Button
# to say words put "Sound.speak.("whatever you want to say") "
#turns out you don't need to do anything special for a global python variable, you just have to treat it like a normal variable

program_running = 0

def Program1():
    program_running = 0
    Sound.speak.("program one")
    Launchrun()  

def Program2():
    program_running = 0
    Sound.speak.("program two")
    Launchrun()  

def Program3():
    program_running = 0
    Sound.speak.("program three")
    Launchrun()  


def Program4():
    program_running = 0
    Sound.speak.("program four")
    Launchrun()  

def Program5():
    program_running = 0
    Sound.speak.("program five")
    Launchrun()  

def Program6():
    program_running = 0
    Sound.speak.("program six")
    Launchrun()  

def Program7():
    program_running = 0
    Sound.speak.("program seven")
    Launchrun()  


def Program8():
    program_running = 0
    Sound.speak.("program eight")
    Launchrun()  

def Launchrun():
    btn = Button()
#if the button is pressed, wait a quarter of a second and then if the button is pressed again run option 1 if else run option 2
    def up(state):
        if state:
            sleep(0.25)
            if state:
            Sound.beep().wait         
                Program1()
                program_running = 1
            else:
                Sound.beep().wait
                Program2()
    def enter(state):
        if state:
            sleep(0.25)
            if state:
            Sound.beep().wait
                Program3()
                program_running = 1
            else:
                Sound.beep().wait
                Program4()
    def down(state):
        if state:
            sleep(0.25)
            if state:
            Sound.beep().wait      
                Program5()
                program_running = 1
            else:
                Sound.beep().wait
                Program6()

    def left(state):
        if state:
            sleep(0.25)
            if state:
            Sound.beep().wait       
                Program7()
                program_running = 1
            else:
                Sound.beep().wait
                Program8()

    def right(state):
        if state:
            sleep(0.25)
            if state:
            Sound.beep().wait      
                Program7()
                program_running = 1
            else:
                Sound.beep().wait
                Program8()


    btn.on_left = left   
    btn.on_right = right 
    btn.on_up = up 
    btn.on_down = down 
    btn.on_enter = enter
    while program running == 0:
        btn.process()