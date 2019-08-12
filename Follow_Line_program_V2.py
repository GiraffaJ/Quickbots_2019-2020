#!/usr/bin/env python3
from ev3dev.ev3 import *
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank, MediumMotor, OUTPUT_D 
from time import sleep

def main():
    MA = MediumMotor("")
    MB = LargeMotor("outB")
    MC = LargeMotor("outC")
    MD = MediumMotor("outD")
    GY = GyroSensor("")
    C3 = ColorSensor("")
    C4 = ColorSensor("")

    # change color sensor to color and define colors
    C4.mode='COL-COLOR'
    colors=('','Black','Blue','Brown','Green','Yellow','Red','White')

    # turn on motors forever 
    MB.run_forever(speed_sp=75)
    MC.run_forever(speed_sp=75)
# while color sensor doesn't sense black. Wait until sensing black.
    while C4.value() != 1:
        print(colors[C4.value()])
        sleep(0.005)

# after loop ends, brake motor B and C
    MB.stop(stop_action="hold")
    MC.stop(stop_action="hold")

if __name__ == "__main__":
    main() 