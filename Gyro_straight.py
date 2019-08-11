#!/usr/bin/env python3
from ev3dev.ev3 import *
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank, MediumMotor, OUTPUT_D, OUTPUT_A 
from time import sleep

#to say words put "Sound.speak.("whatever you want to say") "
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
# change 50 to whatever speed what you want 
    left_wheel_speed = 50
    right_wheel_speed = 50
# change 999999999999 to however you want to go
# if Gyro value is the same as the starting value, go straigt. if more turn right. if less turn left
    while loop_gyro <999999999999:
        if GY.value() == starting_value:
            left_wheel_speed = 20
            right_wheel_speed = 20
            tank_drive.on_for_degrees(SpeedPercent(left_wheel_speed), SpeedPercent(right_wheel_speed), 180)
            sleep(0.1)
        else:
            if GY.value() >= starting_value:
                left_wheel_speed += 1
                tank_drive.on_for_degrees(SpeedPercent(left_wheel_speed), SpeedPercent(right_wheel_speed), 180)
                sleep(0.1)
            else:
                right_wheel_speed += 1
                tank_drive.on_for_degrees(SpeedPercent(left_wheel_speed), SpeedPercent(right_wheel_speed), 180)
                sleep(0.1)

# stop all motors
    MB.stop(stop_action="hold")
    MC.stop(stop_action="hold")



if __name__ == "__main__":
    main()    