#!/usr/bin/env python3
from ev3dev.ev3 import *
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank, MediumMotor, OUTPUT_D, OUTPUT_A 
from time import sleep
from ev3dev2.motor import Motor
# defining all variables. V
def main():
    MA = MediumMotor("outA")
    MB = LargeMotor("outB")
    MC = LargeMotor("outC")
    MD = MediumMotor("outD")
    GY = GyroSensor("")
    C3 = ColorSensor("")
    C4 = ColorSensor("")

#Setting the Gyro. V
    GY.mode='GYRO-ANG'
    GY.mode='GYRO-RATE'
    GY.mode='GYRO-ANG'
    tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
    loop_gyro = 0
    gyro_adjust = 1
    starting_value = GY.value()
    gyro_correct_loops = 0
    straight_correct_loops = 0
    gyro_correct_straight = 0
    # change this to whatever speed what you want. V
    left_wheel_speed = 100
    right_wheel_speed = 100
    # change the loop_gyro verses the defined value argument to however far you want to go
    # if Gyro value is the same as the starting value, go straight, if more turn right, if less turn left
# Wheel alignment. VVVV
    tank_drive.on_for_rotations(SpeedPercent(100), SpeedPercent(100), 0.01)

    #Pulling out of Launch area. V
    tank_drive.on_for_rotations(SpeedPercent(-30), SpeedPercent(-30), 1.625)

    #Gyro Turn toowards the red circle. V
    while GY.value() < 80: 
        left_wheel_speed = 100
        right_wheel_speed = -100

        #MB is left wheel & MC is right wheel
        MB.run_forever(speed_sp=left_wheel_speed)
        MC.run_forever(speed_sp=right_wheel_speed)
    MB.stop(stop_action="hold")
    MC.stop(stop_action="hold")

    #Driving forward towards the red circle. V
    while MB.position > -1700: #was -2550, Joshua is changing it to -2300
        if GY.value() == 90:
            left_wheel_speed = -500
            right_wheel_speed = -500
            MB.run_forever(speed_sp=left_wheel_speed)
            MC.run_forever(speed_sp=right_wheel_speed)
            gyro_adjust = 8
            gyro_correct_loops = 0
            gyro_correct_straight = 0
            straight_correct_loops = 0
        else:
            if GY.value() < 90:
                correct_rate = abs (GY.value()) # This captures the gyro value at the beginning of the statement
                right_wheel_speed = right_wheel_speed - gyro_adjust 
                left_wheel_speed = left_wheel_speed + gyro_adjust 
                MB.run_forever(speed_sp=left_wheel_speed)
                MC.run_forever(speed_sp=right_wheel_speed)
                left_wheel_speed = -500
                right_wheel_speed = -500
                if abs (GY.value()) >= correct_rate: # If gyro value has worsened despite the correction then change the adjust variable for next time
                    gyro_adjust = gyro_adjust + 1
                gyro_correct_loops = gyro_correct_loops + 1
                if GY.value() == 0 and gyro_correct_straight == 0:
                    while straight_correct_loops < gyro_correct_loops + 1:
                        right_wheel_speed = right_wheel_speed - gyro_adjust 
                        left_wheel_speed = left_wheel_speed + gyro_adjust    
                        straight_correct_loops = straight_correct_loops + 1
                    gyro_correct_straight = 1
                    gyro_correct_loops = 0
                    straight_correct_loops = 0                                  
                
            else:
                correct_rate = abs (GY.value()) # Same idea as the other if statement
                left_wheel_speed = left_wheel_speed - gyro_adjust 
                right_wheel_speed = right_wheel_speed + gyro_adjust
                MB.run_forever(speed_sp=left_wheel_speed)
                MC.run_forever(speed_sp=right_wheel_speed)
                left_wheel_speed = -500
                right_wheel_speed = -500
                gyro_correct_loops = gyro_correct_loops + 1
                if abs (GY.value()) >= correct_rate:
                    gyro_adjust = gyro_adjust + 1
                if GY.value() == 0 and gyro_correct_straight == 0: #this code corrects the gyro back to the right line
                    while straight_correct_loops < gyro_correct_loops + 1: #runs this loop until it makes the gyro the opposite of what it was when it was wrong in the first place
                        left_wheel_speed = left_wheel_speed - gyro_adjust 
                        right_wheel_speed = right_wheel_speed + gyro_adjust
                        straight_correct_loops = straight_correct_loops + 1
                    gyro_correct_straight = 1 #makes sure that when the gyro is corrected to both straight and the line it was on that gyro is not messed up again
                    gyro_correct_loops = 0
                    straight_correct_loops = 0  

    # stop all motors
    MB.stop(stop_action="hold")
    MC.stop(stop_action="hold")

#unlocking arm to get elevator
    MD.on_for_degrees(SpeedPercent(-50), 176.26)

#pushing down the beams from safety factor
    tank_drive.on_for_rotations(SpeedPercent(-50), SpeedPercent(-50), 2.75)

#going back to home
    tank_drive.on_for_rotations(SpeedPercent(100), SpeedPercent(100), 6)
    tank_drive.on_for_rotations(SpeedPercent(40), SpeedPercent(40), 3)

if __name__ == "__main__":
    main()