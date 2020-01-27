#!/usr/bin/env python3
from ev3dev.ev3 import *
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank, MediumMotor, OUTPUT_D, OUTPUT_A 
from time import sleep
from ev3dev2.motor import Motor
from ev3dev2.button import Button
# to say words put "Sound.speak("whatever you want to say") "
#turns out you don't need to do anything special for a global python variable, you just have to treat it like a normal variable.
def main():
    program_running = 0
#defining each program
    def Program1():
        Sound.speak("program one")

    def Program2():
        Sound.speak("program two")

    def Program3():
        Sound.speak("program three")

    def Program4():
        Sound.speak("program four")

    def Program5():
        Sound.speak("program five")

    def Program6():
        Sound.speak("program six")

    def Program7():
        Sound.speak("program seven")

    def Program8():
        Sound.speak("program eight")

    def Launchrun():
        btn = Button
#adjust the while statement for however long you want it to go.
        while True:
# V if up button is pressed, wait 1 second. if button is still pressed run program 1 if else run program 2 (repeat for each button)
            if btn.up:
#adjust the sleep for how long you want it to wait for.
                sleep(1)
                if btn.up:
                    Program1()
                else:
                    Program2()

            if btn.down:
                sleep(1)
                if btn.up:
                    Program3()
                else:
                    Program4()

            if btn.left:
                sleep(1)
                if btn.up:
                    Program5()
                else:
                    Program6()

            if btn.right:
                sleep(1)
                if btn.up:
                    Program7()
                else:
                    Program8()
#running launchrun
    Launchrun()
if __name__ == "__main__":
    main()