#!/usr/bin/env python3
from ev3dev.ev3 import *
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank, MediumMotor, OUTPUT_D, OUTPUT_A 
from time import sleep
from ev3dev2.motor import Motor
from ev3dev2.button import Button
program_running = 0
def main():
#defining each program
    def Redcircle():
        program_running = 1
        Sound.speak("red circle").wait
        program_running = 0
        Launchrun()  

    def Bulldozer():
        program_running = 1
        Sound.speak("black circle").wait
        program_running = 0
        Launchrun()  

    def Crane():
        program_running = 1
        Sound.speak("crane").wait
        program_running = 0
        Launchrun()  

    def Spider():
        program_running = 1
        Sound.speak("spider").wait
        program_running = 0
        Launchrun()  

    def Traffic():
        program_running = 1
        Sound.speak("traffic").wait
        program_running = 0
        Launchrun()
        
    def Krab():
        program_running = 1
        Sound.speak("crab").wait
        program_running = 0
        Launchrun()

    def Launchrun():
        Sound.speak("ready to go")
        btn = Button()
#adjust the while statement for however long you want it to go.
        while True:
            Leds.all_off()
# V if up button is pressed, wait 1 second. if button is still pressed run program 1 if else run program 2 (repeat for each button)
            if btn.up:
                sleep(1) 
                if btn.up:
                    Leds.all_off()
                    Krab()
                else:
                    Leds.all_off()
                    Krab()

            if btn.down:
                sleep(1)
                if btn.down:
                    Leds.all_off()
                    Spider()
                else:
                    Leds.all_off()
                    Spider()

            if btn.left:
                sleep(1)
                if btn.left:
                    Leds.all_off()
                    Crane()
                else:
                    Leds.all_off()
                    Crane()

            if btn.right:
                sleep(1)
                if btn.right:
                    Leds.all_off()
                    Bulldozer()
                else:
                    Leds.all_off()
                    Bulldozer()

            if btn.enter:
                Leds.set_color(Leds.LEFT, Leds.RED)
                Leds.set_color(Leds.RIGHT, Leds.RED)
                sleep(1)
                if btn.enter:
                    Leds.set_color(Leds.LEFT, Leds.GREEN)
                    Leds.set_color(Leds.RIGHT, Leds.GREEN)
                    while btn.enter:
                        sleep(0.01)
                        Leds.set_color(Leds.RIGHT, Leds.GREEN)
                        Leds.set_color(Leds.LEFT, Leds.GREEN)
                    Leds.all_off()
                    Traffic()
                else:
                    Leds.all_off()
                    Redcircle()
            else:
                Leds.all_off()

            if program_running == 0:
                Leds.set_color(Leds.LEFT, Leds.AMBER)
                Leds.set_color(Leds.RIGHT, Leds.AMBER)
            if program_running == 1:
                Leds.all_off()

#running launchrun
    Launchrun()
if __name__ == "__main__":
    main()