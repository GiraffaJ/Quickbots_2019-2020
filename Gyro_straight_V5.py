#!/usr/bin/env python3

# start import of all actions for EV3
from ev3dev.ev3 import *
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank, MediumMotor, OUTPUT_D, OUTPUT_A 
# end import of all actions for EV3

# start import of appliance
from time import sleep
# end import of appliance

# to say words put "Sound.speak.("whatever you want to say") "

# start definition all input and output parameters
def main():

# start sensor and motor definitions
    Sound.speak("").wait()
    MA = MediumMotor("")
    MB = LargeMotor("outB")
    MC = LargeMotor("outC")
    MD = MediumMotor("")
    GY = GyroSensor("")
    C3 = ColorSensor("")
    C4 = ColorSensor("")
# end sensor and motor definitions

# start calibration
    GY.mode='GYRO-ANG'
    GY.mode='GYRO-RATE'
    GY.mode='GYRO-ANG'
# end calibration

# The following line would be if we used tank_drive
#    tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)

# start definition of driving parameters
    loop_gyro = 0
    starting_value = GY.value()
# end definition of driving parameters

# set initial speed parameters 
    speed = 20
    adjust = 1

# change 999999999999 to however you want to go
    while loop_gyro <999999999999:

# while Gyro value is the same as the starting value, then go straigt.
        while GY.value() == starting_value:
            left_wheel_speed = speed
            right_wheel_speed = speed
            MB.run_forever(speed_sp=left_wheel_speed)
            MC.run_forever(speed_sp=right_wheel_speed)
            return

# while greater than starting value, then go left.
        while GY.value() > starting_value:
            left_wheel_speed = speed - adjust
            right_wheel_speed = speed
            MB.run_forever(speed_sp=left_wheel_speed)
            MC.run_forever(speed_sp=right_wheel_speed)
            return

# while less than starting value, then go right.
        while GY.value() < starting_value:
            left_wheel_speed = speed + adjust
            right_wheel_speed = speed
            MB.run_forever(speed_sp=left_wheel_speed)
            MC.run_forever(speed_sp=right_wheel_speed)
            return
        return

# stop all motors
#    MB.stop(stop_action="hold")
#    MC.stop(stop_action="hold")

if __name__ == "__main__":
    main()    