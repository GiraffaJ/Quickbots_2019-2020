#!/usr/bin/env python3
from ev3dev.ev3 import *
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank, MediumMotor, OUTPUT_D, OUTPUT_A 
from time import sleep
from ev3dev2.motor import Motor
# to say words put "Sound.speak.("whatever you want to say") "
#turns out you don't need to do anything special for a global python variable, you just have to treat it like a normal variable

def main():
    program_running = 0
    MA = MediumMotor("")
    MB = LargeMotor("outB")
    MC = LargeMotor("outC")
    MD = MediumMotor("outD")
    GY = GyroSensor("")
    C3 = ColorSensor("")
    C4 = ColorSensor("")

    MA.on_for_degrees(SpeedPercent(50), 9000)

if __name__ == "__main__":
    main()    
