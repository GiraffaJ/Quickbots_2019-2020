#!/usr/bin/env python3
from ev3dev.ev3 import *
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank, MediumMotor, OUTPUT_D, OUTPUT_A 
from time import sleep
from ev3dev2.motor import Motor
# defining all variables. 
# don't delete anything, comment out!!!
def main():
    Sound.speak("").wait()
    MA = MediumMotor("")
    MB = LargeMotor("outB")
    MC = LargeMotor("outC")
    MD = MediumMotor("")
    GY = GyroSensor("")
    C3 = ColorSensor("")
    C4 = ColorSensor("")
    T1 = TouchSensor("")


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
# change this to whatever speed what you want 
    left_wheel_speed = 100
    right_wheel_speed = 100
    # change the loop_gyro verses the defined value argument to however far you want to go
# if Gyro value is the same as the starting value, go straight, if more turn right, if less turn left
# change the value to how far you want the robot to go
    tank_drive.on_for_rotations(SpeedPercent(-30), SpeedPercent(-30), 1) #the robot starts out from base
    
    while GY.value() < 85: #gyro turns 85 degrees and faces towards the swing
        left_wheel_speed = 100
        right_wheel_speed = -100
        #MB is left wheel & MC is right wheel
        MB.run_forever(speed_sp=left_wheel_speed)
        MC.run_forever(speed_sp=right_wheel_speed)
    MB.stop(stop_action="hold")
    MC.stop(stop_action="hold")
    
    while MB.position > -2326: #this is the gyro program, the first line tells the bot to continue loop until it reaches a defined position
        if GY.value() == 90: #this runs if the gyro is OK and already straight, sets a lot of variables as well
            left_wheel_speed = -300
            right_wheel_speed = -300
            MB.run_forever(speed_sp=left_wheel_speed)
            MC.run_forever(speed_sp=right_wheel_speed)
            gyro_adjust = 8
            gyro_correct_loops = 0
            gyro_correct_straight = 0
            straight_correct_loops = 0
        else: #if the gyro is off it runs this section of code
            if GY.value() < 90:
                correct_rate = abs (GY.value()) # This captures the gyro value at the beginning of the statement
                right_wheel_speed = right_wheel_speed - gyro_adjust #changes the wheel speeds accordingly
                left_wheel_speed = left_wheel_speed + gyro_adjust 
                MB.run_forever(speed_sp=left_wheel_speed)
                MC.run_forever(speed_sp=right_wheel_speed)
                left_wheel_speed = -300
                right_wheel_speed = -300
                if abs (GY.value()) >= correct_rate: # If gyro value has worsened despite the correction then change the adjust variable for next time
                    gyro_adjust = gyro_adjust + 1
                gyro_correct_loops = gyro_correct_loops + 1
                if GY.value() == 0 and gyro_correct_straight == 0: #runs only if bot isn't already on the original line it started from
                    while straight_correct_loops < gyro_correct_loops + 1: #Basically this messes up the gyro again so the bot can correct back to the line it was orignally on
                        right_wheel_speed = right_wheel_speed - gyro_adjust 
                        left_wheel_speed = left_wheel_speed + gyro_adjust    
                        straight_correct_loops = straight_correct_loops + 1
                    gyro_correct_straight = 1 #sets this to 1 so that it doesn't go off the line again
                    gyro_correct_loops = 0
                    straight_correct_loops = 0                                  
                
            else:
                correct_rate = abs (GY.value()) # Same idea as the other if statement, just reversed
                left_wheel_speed = left_wheel_speed - gyro_adjust 
                right_wheel_speed = right_wheel_speed + gyro_adjust
                MB.run_forever(speed_sp=left_wheel_speed)
                MC.run_forever(speed_sp=right_wheel_speed)
                left_wheel_speed = -300
                right_wheel_speed = -300
                gyro_correct_loops = gyro_correct_loops + 1
                if abs (GY.value()) >= correct_rate:
                    gyro_adjust = gyro_adjust + 1
                if GY.value() == 0 and gyro_correct_straight == 0: 
                    while straight_correct_loops < gyro_correct_loops + 1: 
                        left_wheel_speed = left_wheel_speed - gyro_adjust 
                        right_wheel_speed = right_wheel_speed + gyro_adjust
                        straight_correct_loops = straight_correct_loops + 1
                    gyro_correct_straight = 1 
                    gyro_correct_loops = 0
                    straight_correct_loops = 0  

         
# stop all motors
    MB.stop(stop_action="hold")
    MC.stop(stop_action="hold")

    while GY.value() < 120: #this turns the blocks into the circle
        left_wheel_speed = 100
        right_wheel_speed = -100
        #MB is left wheel & MC is right wheel
        MB.run_forever(speed_sp=left_wheel_speed)
        MC.run_forever(speed_sp=right_wheel_speed)
    MB.stop(stop_action="hold")
    MC.stop(stop_action="hold")
    tank_drive.on_for_rotations(SpeedPercent(-30), SpeedPercent(-30), 0.25) #goes forward slightly to move the blocks all the way into the circle

    tank_drive.on_for_rotations(SpeedPercent(30), SpeedPercent(30), 1) #drives back a bit

    while GY.value() > 110: #turns to face the launch area backwards
        left_wheel_speed = -100 #originaly 200
        right_wheel_speed = 100 #originaly 200
        MB.run_forever(speed_sp=left_wheel_speed)
        MC.run_forever(speed_sp=right_wheel_speed)
    MB.stop(stop_action="hold")
    MC.stop(stop_action="hold")
# Returning to home. V
    tank_drive.on_for_rotations(SpeedPercent(75), SpeedPercent(75), 8.5) #drives back to base. 


if __name__ == "__main__":
    main()