#!/usr/bin/env python3
from ev3dev.ev3 import *
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank, MediumMotor, OUTPUT_D, OUTPUT_A 
from time import sleep
# importing everything. ^
#defining all variables, sensors, and motors. V
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
    starting_value = GY.value()
# change this to whatever speed what you want. V
    left_wheel_speed = -300
    right_wheel_speed = -300
# if Gyro value is the same as the starting value, go straigt. if more turn right. if less turn left. V
# FIX THIS VALUE!!!!!!!!!! V
    while MB.position >= -500: # consider adjusting the wheel speeds only if your current gyro value doesn't equal the starting value
        if GY.value() == 0:
            left_wheel_speed = -300 
            right_wheel_speed = -300
            MB.run_forever(speed_sp=left_wheel_speed)
            MC.run_forever(speed_sp=right_wheel_speed)
            gyro_adjust = 1
        else:
            if GY.value() > starting_value:
                correct_rate = abs (GY.value()) # This captures the gyro value at the beginning of the statement
                left_wheel_speed = left_wheel_speed - gyro_adjust 
                right_wheel_speed = right_wheel_speed + gyro_adjust 
                MB.run_forever(speed_sp=left_wheel_speed)
                MC.run_forever(speed_sp=right_wheel_speed)
                left_wheel_speed = -300
                right_wheel_speed = -300
                if abs (GY.value()) > correct_rate:
                    gyro_adjust = gyro_adjust + 1 # If gyro value has worsened despite the correction then change the adjust variable for next time
            else:
                correct_rate = abs (GY.value()) # Same idea as the other if statement
                right_wheel_speed = right_wheel_speed - gyro_adjust 
                left_wheel_speed = left_wheel_speed + gyro_adjust
                MB.run_forever(speed_sp=left_wheel_speed)
                MC.run_forever(speed_sp=right_wheel_speed)
                left_wheel_speed = -300
                right_wheel_speed = -300
                if abs (GY.value()) > correct_rate:
                    gyro_adjust = gyro_adjust + 1

# wait for the block to drop. V
    sleep(3)                
# pulling away from the crane. V
    tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(50), 0.25)
# Unlocking attachment. V
    MD.on_for_degrees(SpeedPercent(50), 600)
# pulling away from unlocked attachment. V
    tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(50), 1)
# gyro 90 degree spin turn
    while GY.value() <= 45:
        MB.run_forever(speed_sp=300)
        MC.run_forever(speed_sp=-300)   
# drive into home
    tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(50), 4)

if __name__ == "__main__":
    main()