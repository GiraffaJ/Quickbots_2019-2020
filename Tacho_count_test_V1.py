#!/usr/bin/env python3
from ev3dev.ev3 import *
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank, MediumMotor, OUTPUT_D, OUTPUT_A 
from time import sleep
#IF YOU'RE USING MB.POSITION IMPORT from ev3dev2.motor import Motor
from ev3dev2.motor import Motor
# defining all variables
#the average tacho count is 374 counts per rotation
def main():
    Sound.speak("").wait()
    MA = MediumMotor("")
    MB = LargeMotor("outB")
    MC = LargeMotor("outC")
    MD = MediumMotor("")
    GY = GyroSensor("")
    C3 = ColorSensor("")
    C4 = ColorSensor("")

    tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
# speaks "before" tacho count
    Sound.speak(MB.position).wait()
    tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(0), 1)
# speaks "after" tacho count    
    Sound.speak(MB.position).wait()



if __name__ == "__main__":
    main()