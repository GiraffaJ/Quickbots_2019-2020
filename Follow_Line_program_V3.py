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

    tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)

    # change color sensor to color and define colors
    C4.mode='COL-COLOR'
    colors=('','Black','Blue','Brown','Green','Yellow','Red','White')

    # turn on motors forever 
    MB.run_forever(speed_sp=75)
    MC.run_forever(speed_sp=75)
# while color sensor doesn't sense black. Wait until sensing black. vice versa for white
    while C4.value() == 0 or 2 or 3 or 4 or 5 or 6:
        if C4.value() != 1:
            #this makes the robot move left when sensing black
            tank_drive.on_for_degrees(SpeedPercent(-5), SpeedPercent(-20), 20)
            sleep(0.5)
        elif C4.value() != 7:
            tank_drive.on_for_degrees(SpeedPercent(-20), SpeedPercent(-5), 20)
            sleep(0.5)
            #this makes the robot move right when sensing white
        else:
            tank_drive.on_for_degrees(SpeedPercent(-20), SpeedPercent(-20), 20)
            sleep(0.5)
            #this makes the robot move forward when anything else happens

# after loop ends, brake motor B and C
    MB.stop(stop_action="hold")
    MC.stop(stop_action="hold")

if __name__ == "__main__":
    main() 