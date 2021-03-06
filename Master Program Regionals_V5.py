#!/usr/bin/env python3
from ev3dev.ev3 import *
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank, MediumMotor, OUTPUT_D, OUTPUT_A 
from time import sleep
from ev3dev2.motor import Motor
# to say words put "Sound.speak.("whatever you want to say") "
#turns out you don't need to do anything special for a global python variable, you just have to treat it like a normal variable

def main():
    program_running = 0
    MA = MediumMotor("")
    MB = LargeMotor("outB")
    MC = LargeMotor("outC")
    MD = MediumMotor("outD")
    GY = GyroSensor("")
    C3 = ColorSensor("")
    C4 = ColorSensor("")
    def Redcircle():#Setting the Gyro. V
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
        tank_drive.on_for_rotations(SpeedPercent(100), SpeedPercent(100), 0.01) #wheel alignment
        # change the loop_gyro verses the defined value argument to however far you want to go
    # if Gyro value is the same as the starting value, go straight, if more turn right, if less turn left
    # change the value to how far you want the robot to go. V
    #Pulling out of Launch area. V
        tank_drive.on_for_rotations(SpeedPercent(-30), SpeedPercent(-30), 1.5)
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
        while MB.position > -1270: #was -1280, tessa is changing it to 1270 to stay in circle better
            if GY.value() == 90:
                left_wheel_speed = -300
                right_wheel_speed = -300
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
                    left_wheel_speed = -300
                    right_wheel_speed = -300
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
                    left_wheel_speed = -300
                    right_wheel_speed = -300
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
    #Pulling away from the Red circle and driving into home. V
        tank_drive.on_for_rotations(SpeedPercent(65), SpeedPercent(65), 6) #originally 5 rotations.
        MB.stop(stop_action="coast")
        MC.stop(stop_action="coast")
        program_running = 0
        Launchrun()  

    def Bulldozer():
        GY.mode='GYRO-ANG'
        GY.mode='GYRO-RATE'
        GY.mode='GYRO-ANG'
        tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
        loop_gyro = 0
        gyro_adjust = 12
        # change this to whatever speed what you want 
        left_wheel_speed = -300
        right_wheel_speed = -300
        tank_drive.on_for_rotations(SpeedPercent(100), SpeedPercent(100), 0.01) #wheel alignment
    # change the loop_gyro verses the defined value argument to however far you want to go
    # if Gyro value is the same as the starting value, go straight, if more turn right, if less turn left
    # change the value to how far you want the robot to go. V
        while MB.position > -750:
            if GY.value() == 0:
                left_wheel_speed = -300
                right_wheel_speed = -300
                MB.run_forever(speed_sp=left_wheel_speed)
                MC.run_forever(speed_sp=right_wheel_speed)
                gyro_adjust = 9
            else:
                if GY.value() < 0:
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


    # pulling away from stacks. V
        tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(50), 1.75)
    # gyro 90 degree spin turn
        while GY.value() < 50:
            MB.run_forever(speed_sp=300)
            MC.run_forever(speed_sp=-300)   
    # drive into home
        tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(50), 4)
        MB.stop(stop_action="coast")
        MC.stop(stop_action="coast")

        program_running = 0
        Launchrun()  

    def Crane():
        GY.mode='GYRO-ANG'
        GY.mode='GYRO-RATE'
        GY.mode='GYRO-ANG'
        tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
        loop_gyro = 0
        gyro_adjust = 12
        # change this to whatever speed what you want 
        left_wheel_speed = -300
        right_wheel_speed = -300
        tank_drive.on_for_rotations(SpeedPercent(100), SpeedPercent(100), 0.01) #wheel alignment
    # change the loop_gyro verses the defined value argument to however far you want to go
    # if Gyro value is the same as the starting value, go straight, if more turn right, if less turn left
    # change the value to how far you want the robot to go. V
        while MB.position > -900:
            if GY.value() == 0:
                left_wheel_speed = -300
                right_wheel_speed = -300
                MB.run_forever(speed_sp=left_wheel_speed)
                MC.run_forever(speed_sp=right_wheel_speed)
                gyro_adjust = 9
            else:
                if GY.value() < 0:
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

    # wait for the block to drop. V
        sleep(1.5)                
    # pulling away from the crane. V
        tank_drive.on_for_rotations(SpeedPercent(20), SpeedPercent(10), 0.50)
    # Unlocking attachment. V
        MD.on_for_degrees(SpeedPercent(50), 360)
    # pulling away from unlocked attachment. V
        tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(50), 1)
    # gyro 90 degree spin turn
        while GY.value() < 91:
            MB.run_forever(speed_sp=300)
            MC.run_forever(speed_sp=-300)   
    # drive into home
        tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(50), 4)
        MB.stop(stop_action="coast")
        MC.stop(stop_action="coast")

        program_running = 0
        Launchrun()  

    def Spider():
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
        tank_drive.on_for_rotations(SpeedPercent(100), SpeedPercent(100), 0.01) #wheel alignment
        # change the loop_gyro verses the defined value argument to however far you want to go
    # if Gyro value is the same as the starting value, go straight, if more turn right, if less turn left
    # change the value to how far you want the robot to go
        tank_drive.on_for_rotations(SpeedPercent(-30), SpeedPercent(-30), 0.95) # Originally 0.9. he robot starts out from base
        
        while GY.value() < 85: #gyro turns 85 degrees and faces towards the swing
            left_wheel_speed = 100
            right_wheel_speed = -100
            #MB is left wheel & MC is right wheel
            MB.run_forever(speed_sp=left_wheel_speed)
            MC.run_forever(speed_sp=right_wheel_speed)
        MB.stop(stop_action="hold")
        MC.stop(stop_action="hold")
        
        while MB.position > -2326: # this is the gyro program, the first line tells the bot to continue loop until it reaches a defined position
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
        tank_drive.on_for_rotations(SpeedPercent(-30), SpeedPercent(-30), 0.18) #Originally 0.2. goes forward slightly to move the blocks all the way into the circle

        tank_drive.on_for_rotations(SpeedPercent(30), SpeedPercent(30), 1) #drives back a bit

        while GY.value() > 110: #turns to face the launch area backwards
            left_wheel_speed = -100 #originaly 200
            right_wheel_speed = 100 #originaly 200
            MB.run_forever(speed_sp=left_wheel_speed)
            MC.run_forever(speed_sp=right_wheel_speed)
        MB.stop(stop_action="hold")
        MC.stop(stop_action="hold")
    # Returning to home. V
        tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(50), 9) #drives back to base. originally 8.5 rotations. keep speed at 50
        MB.stop(stop_action="coast")
        MC.stop(stop_action="coast")
        program_running = 0
        Launchrun()  

    def Launchrun():
        Sound.speak("ready to go")
        btn = Button()
        def up(state):
            if state:
                Sound.speak("run spider").wait()
                Spider()
                program_running = 1
        def right(state):
            if state:
                Sound.speak("run red circle").wait()
                Redcircle()
                program_running = 1
        def left(state):
            if state:
                Sound.speak("run bulldozer").wait()
                Bulldozer()
                program_running = 1
        def down(state):
            if state:
                Sound.speak("run crane").wait()
                Crane()
                program_running = 1
    
        btn.on_left = left   
        btn.on_up = up 
        btn.on_down = down 
        btn.on_right = right
        while program_running == 0:
            btn.process()

    Launchrun()

if __name__ == "__main__":
    main()    
#THIS
#IS
#ONLY
#FOR 420