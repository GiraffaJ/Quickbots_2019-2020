#!/usr/bin/env python3
from ev3dev.ev3 import *
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank, MediumMotor, OUTPUT_D, OUTPUT_A 
from time import sleep
from ev3dev2.motor import Motor, Button

def main():

    def LineFollow():
        MA = MediumMotor("")
        MB = LargeMotor("outB")
        MC = LargeMotor("outC")
        MD = MediumMotor("outD")
        GY = GyroSensor("")
        C3 = ColorSensor("")
        C4 = ColorSensor("")
        lcd = Screen()
        tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)

# V  Adjust the number after the C to choose the port it's sensing from. V
# V  Setting the Color and Gyro sensor mode and telling it what colors it can see. V
        GY.mode='GYRO-ANG'
        GY.mode='GYRO-RATE'
        GY.mode='GYRO-ANG'
        C3.mode = 'COL-COLOR'
        colors = ('', 'black','blue','green','yellow','red','white','brown')

# Adjust this value to make  VVVV  it go closer or farther
        while MB.position > -1270:
            
# if senses black, turn a little to the left
            if colors[C3.value()] == "black":
                tank_drive.on_forever(SpeedPercent(-90), SpeedPercent(-100))

# if senses white, turn a little to the right
            elif colors[C3.value()] == "white":
                tank_drive.on_forever(SpeedPercent(-100), SpeedPercent(-90))
# if senses anything else, go back to the line

            else:
                if GY.value < -5:
                    tank_drive.on_forever(SpeedPercent(-100), SpeedPercent(-90))  
                    
                elif GY.value > 5:
                    tank_drive.on_forever(SpeedPercent(-90), SpeedPercent(-100))
                    
LineFollow()