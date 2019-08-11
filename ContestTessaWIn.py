#!/usr/bin/env python3
from ev3dev.ev3 import *
import ev3dev.fonts as fonts
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank 
from time import sleep
# what does this do^^^^^^^^????????!!!!!!!!!!!!!???????????!!!!!!!?????????!!!!!!!!!!!!?????????
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