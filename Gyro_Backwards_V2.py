#!/usr/bin/env python3
from ev3dev.ev3 import *
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank, MediumMotor, OUTPUT_D, OUTPUT_A 
from time import sleep
from ev3dev2.motor import Motor
# this one works the best USE THIS ONE FOR GYRO STRAIGHT!!!!!!!!!!!
# if you don't understand anything then ask Sam since he coded it :)
# to say words put "Sound.speak.("whatever you want to say") "
# defining all variables
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
    gyro_adjust = 1
    # change this to whatever speed what you want 
    left_wheel_speed = -300
    right_wheel_speed = -300
# change the loop_gyro verses the defined value argument to however far you want to go
# if Gyro value is the same as the starting value, go straight, if more turn right, if less turn left
# change the value to how far you want the robot to go
    while MB.position > -160:
        if GY.value() == 0:
            left_wheel_speed = -300
            right_wheel_speed = -300
            MB.run_forever(speed_sp=left_wheel_speed)
            MC.run_forever(speed_sp=right_wheel_speed)
            gyro_adjust = 12
        else:
            if GY.value() > 0:
                correct_rate = abs (GY.value()) # This captures the gyro value at the beginning of the statement
                left_wheel_speed = left_wheel_speed + gyro_adjust 
                right_wheel_speed = right_wheel_speed - gyro_adjust 
                MB.run_forever(speed_sp=left_wheel_speed)
                MC.run_forever(speed_sp=right_wheel_speed)
                left_wheel_speed = -300
                right_wheel_speed = -300
                if abs (GY.value()) > correct_rate: # If gyro value has worsened despite the correction then change the adjust variable for next time
                    gyro_adjust = gyro_adjust + 1
            else:
                correct_rate = abs (GY.value()) # Same idea as the other if statement
                right_wheel_speed = right_wheel_speed + gyro_adjust 
                left_wheel_speed = left_wheel_speed - gyro_adjust
                MB.run_forever(speed_sp=left_wheel_speed)
                MC.run_forever(speed_sp=right_wheel_speed)
                left_wheel_speed = -300
                right_wheel_speed = -300
                if abs (GY.value()) > correct_rate:
                    gyro_adjust = gyro_adjust + 1

         
# stop all motors
    MB.stop(stop_action="hold")
    MC.stop(stop_action="hold")



if __name__ == "__main__":
    main()