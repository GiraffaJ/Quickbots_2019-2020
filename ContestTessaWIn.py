#!/usr/bin/env python3
from ev3dev.ev3 import *
import ev3dev.fonts as fonts
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank 
from time import sleep
# what does this do^^^^^^^^????????!!!!!!!!!!!!!???????????!!!!!!!?????????!!!!!!!!!!!!?????????
# "!/usr/bin/env python3" Tells your robot where to look to find the python package it should use (room in the house.)
# The things under it are import statements. Think of it when you download an app to your phone. Textually, that would
# be like saying "from App_Store import Game" and then after that, your phone has access to all of the 
# functions of that game. The import statements above download extensions to your Ev3 that give it access to 
# new functions. For example, "import ev3dev.fonts as fonts" gives you access to some fonts that don't come 
# originally installed on the Ev3. Let me know if this clears it up! 


def main():
    gy = GyroSensor()
    mB = LargeMotor('outB')
    mC = LargeMotor('outC')
    cl = ColorSensor()
    ts = TouchSensor()
    lcd = Screen()
    btn = Button()

    while not btn.any(): # While no (not any) button is pressed.
        sleep(0.01)  # Wait 0.01 second

        Sound.beep().wait()

    tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)

 # telling it what colors it can see
    cl.mode='COL-COLOR'
    colors=('', 'black','blue','green','yellow','red','white','brown')
    # always checking for color
    while True:
        print(colors[cl.value()])
        #what to do when color seen, when see blue it say on screen blue
        sleep(1)
        if colors[cl.value()] == "red":
            tank_drive.on_for_rotations(SpeedPercent(100), SpeedPercent(100), 10)
            tank_drive.on_for_rotations(SpeedPercent(-50), SpeedPercent(-50), 3)

#Poop poo poo poo pooooooooooo poop



if __name__ == "__main__":
    main()
