#!/usr/bin/env python3
from ev3dev.ev3 import *
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank, MediumMotor, OUTPUT_D, OUTPUT_A 
from time import sleep
from ev3dev2.motor import Motor
from ev3dev2.button import Button
# to say words put "Sound.speak("whatever you want to say") "
#turns out you don't need to do anything special for a global python variable, you just have to treat it like a normal variable.
def main():
#defining each program
    def Gyro_straight():
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
        tank_drive.on_for_rotations(SpeedPercent(100), SpeedPercent(100), 0.01)
    # change this to whatever speed what you want 
        while MB.position > -2000: # this is the gyro program, the first line tells the bot to continue loop until it reaches a defined position
            if GY.value() == 0: #this runs if the gyro is OK and already straight, sets a lot of variables as well
                left_wheel_speed = -300
                right_wheel_speed = -300
                MB.run_forever(speed_sp=left_wheel_speed)
                MC.run_forever(speed_sp=right_wheel_speed)
                gyro_adjust = 8
                gyro_correct_loops = 0
                gyro_correct_straight = 0
                straight_correct_loops = 0
            else: #if the gyro is off it runs this section of code
                if GY.value() < 0:
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
                        while straight_correct_loops < gyro_correct_loops: #Basically this messes up the gyro again so the bot can correct back to the line it was orignally on
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
                        while straight_correct_loops < gyro_correct_loops: 
                            left_wheel_speed = left_wheel_speed - gyro_adjust 
                            right_wheel_speed = right_wheel_speed + gyro_adjust
                            straight_correct_loops = straight_correct_loops + 1
                        gyro_correct_straight = 1 
                        gyro_correct_loops = 0
                        straight_correct_loops = 0              
    
        Launchrun()  

    def Program5():
        Sound.speak("program five")

    def Program6():
        Sound.speak("program six")

    def Program7():
        Sound.speak("program seven")

    def Program8():
        Sound.speak("program eight")

    def Launchrun():
        Sound.speak("ready to go")
        btn = Button()
#adjust the while statement for however long you want it to go.
        while True:
# V if up button is pressed, wait 1 second. if button is still pressed run program 1 if else run program 2 (repeat for each button)
            if btn.up:
                sleep(1)
                if btn.up:
                    Gyro_straight()
                else:
                    Gyro_straight()

            if btn.down:
                sleep(1)
                if btn.down:
                    Crane()
                else:
                    Crane()

            if btn.left:
                sleep(1)
                if btn.left:
                    Bulldozer()
                else:
                    Bulldozer()

            if btn.right:
                sleep(1)
                if btn.right:
                    Redcircle()
                else:
                    Redcircle()

            if btn.enter:
                sleep(1)
                if btn.enter:
                    Program2()
                else:
                    Program1()
#running launchrun
    Launchrun()
if __name__ == "__main__":
    main()