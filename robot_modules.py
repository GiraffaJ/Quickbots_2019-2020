#!/usr/bin/env python3
from ev3dev.ev3 import *
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank, MediumMotor, OUTPUT_D, OUTPUT_A 
from time import sleep

#to say words put "Sound.speak.("whatever you want to say") "
def main():
    Sound.speak("").wait()
    MA = MediumMotor("outA")
    MB = LargeMotor("outB")
    MC = LargeMotor("outC")
    MD = MediumMotor("outD")
    GY = GyroSensor("")
    C3 = ColorSensor("")
    C4 = ColorSensor("")

#drive forward program lines 18-19
tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
tank_drive.on_for_rotations(SpeedPercent(20), SpeedPercent(20), 1)
# Insert needed amounts here:             ^                 ^   ^
# Also change tank_drive.on_for_rotations to tank_drive.on_for_degrees if you want degrees instead of rotations


# Gyro turn program lines 25-39
    GY.mode='GYRO-ANG'
    GY.mode='GYRO-RATE'
    GY.mode='GYRO-ANG'

#change speeds here:         v (make sure one is positive and one is negative to make the robot turn)
    MB.run_forever(speed_sp=75)
    MC.run_forever(speed_sp=-75)

# change angle  here:     v
    while GY.value() >= -90:
        sleep(0.005)
# change (0.005) to how often you want to check. If the robot doesn't stop turning, change the angle value to it's opposite.

    MB.stop(stop_action="hold")
    MC.stop(stop_action="hold")

# cange C4. to C3. if you want it to sense on the other color sensor 
    C4.mode='COL-COLOR'

    colors=('white','Black'
    while colors != Black:
# if you want a straigh line make sure they are both the same number        
# put speed (Speed_sp=insertspeedhere)

        MB.run_forever(speed_sp=75)
        MC.run_forever(speed_sp=75)
    
    MB.stop(stop_action="hold")
    MC.stop(stop_action="hold")


# lines 57-78 is a line follower
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
            tank_drive.on_for_degrees(SpeedPercent(-15), SpeedPercent(-20), 5)
            sleep(0.5)
        elif C4.value() != 7:
            tank_drive.on_for_degrees(SpeedPercent(-20), SpeedPercent(-15), 5)
            sleep(0.5)
            #this makes the robot move right when sensing white
        else:
            tank_drive.on_for_degrees(SpeedPercent(-20), SpeedPercent(-20), 5)
            sleep(0.5)
            #this makes the robot move forward when anything else happens

# after loop ends, brake motor B and C
    MB.stop(stop_action="hold")
    MC.stop(stop_action="hold")


if __name__ == "__main__":
    main()
