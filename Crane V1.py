#!/usr/bin/env python3
from ev3dev.ev3 import *
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank, MediumMotor, OUTPUT_D, OUTPUT_A 
from time import sleep
# this one works the best USE THIS ONE FOR GYRO STRAIGHT!!!!!!!!!!!
#to say words put Sound.speak.("whatever you want to say") 
#defining all variables
def main():
    Sound.speak("").wait()
    MA = MediumMotor("")
    MB = LargeMotor("outB")
    MC = LargeMotor("outC")
    MD = MediumMotor("")
    GY = GyroSensor("")
    C3 = ColorSensor("")
    C4 = ColorSensor("")


    GY.mode='GYRO-ANG'
    GY.mode='GYRO-RATE'
    GY.mode='GYRO-ANG'
    tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
    loop_gyro = 0
    starting_value = GY.value()
# change 20 to whatever speed what you want 
    left_wheel_speed = 100
    right_wheel_speed = 100
# change 999999999999 to however you want to go
# if Gyro value is the same as the starting value, go straigt. if more turn right. if less turn left
    while loop_gyro <999:
        if GY.value() == starting_value:
            left_wheel_speed = -300
            right_wheel_speed = -300
            MB.run_forever(speed_sp=left_wheel_speed)
            MC.run_forever(speed_sp=right_wheel_speed)
        else:
            if GY.value() > starting_value:
                left_wheel_speed = left_wheel_speed - GY.value() / 2 
                right_wheel_speed = right_wheel_speed + GY.value() * -1 / 2 
                MB.run_forever(speed_sp=left_wheel_speed)
                MC.run_forever(speed_sp=right_wheel_speed)
                left_wheel_speed = -300
                right_wheel_speed = -300
            else:
                right_wheel_speed = right_wheel_speed + GY.value() / 2 
                left_wheel_speed = left_wheel_speed - GY.value() / 2 
                MB.run_forever(speed_sp=left_wheel_speed)
                MC.run_forever(speed_sp=right_wheel_speed)
                left_wheel_speed = -300
                right_wheel_speed = -300
        loop_gyro + 1
# stop all motors
    MB.stop(stop_action="hold")
    MC.stop(stop_action="hold")



if __name__ == "__main__":
    main()    