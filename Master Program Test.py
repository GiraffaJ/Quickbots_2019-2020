#!/usr/bin/env python3
from ev3dev.ev3 import *
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank, MediumMotor, OUTPUT_D, OUTPUT_A 
from time import sleep
from ev3dev2.motor import Motor
# to say words put "Sound.speak("whatever you want to say") "
#turns out you don't need to do anything special for a global python variable, you just have to treat it like a normal variable
program_running = 0



def main():

        
    def program1():
        program_running = 1
        print("Program1")
        Sound.speak("Program one")
        program_running = 0
        Launchrun()

    def program2():
        program_running = 1
        print("Program2")
        Sound.speak("Program two")
        program_running = 0
        Launchrun()  


    def Launchrun():
        btn = Button()
        def left(state):
            if state:
                sleep(1)
                Sound.beep()
                if state:
                    program1()
                else:
                    program2()
        btn.on_left = left   
        while program_running == 0:
            btn.process()

    Launchrun()
if __name__ == "__main__":
    main()    