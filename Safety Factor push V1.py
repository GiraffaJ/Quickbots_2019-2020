#!/usr/bin/env python3
from ev3dev.ev3 import *
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank, MediumMotor, OUTPUT_D, OUTPUT_A 
from time import sleep
from ev3dev2.motor import Motor
def main():
    MA = MediumMotor("")
    MB = LargeMotor("outB")
    MC = LargeMotor("outC")
    MD = MediumMotor("outD")
    GY = GyroSensor("")
    C3 = ColorSensor("")
    C4 = ColorSensor("")
    tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
    def Safety_factor():
        tank_drive.on_for_rotations(SpeedPercent(100), SpeedPercent(100), 1)

    Safety_factor ()
if __name__ == "__main__":
    main()