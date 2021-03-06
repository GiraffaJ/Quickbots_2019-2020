#!/usr/bin/env python3
from ev3dev.ev3 import *
import ev3dev.fonts as fonts
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank 
from time import sleep

#everything so far is copied from Tessa's program.
def main():
    gy = GyroSensor()
    mB = LargeMotor('outB')
    mC = LargeMotor('outC')
    cl = ColorSensor()
    lcd = Screen()

    tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
    
    
    #telling it what colors it can see
    cl.mode='COL-COLOR'
    colors=('', 'black','blue','green','yellow','red','white','brown')

    Sound.beep


    # always checking for color
    while True:
        print(colors[cl.value()])
        #what to do when color seen, when see blue it say on screen blue
        sleep(1)

        if colors[cl.value()] == "red":
            lcd.draw.text((10,10), 'Red', font=fonts.load('luBS24'))# tried 24, trying bigger must use 24 other dont work
            lcd.update()
            sleep(3.75)
        #everything below is still Tessa's, but I change what it said
        elif colors[cl.value()] == "Blue":
            lcd.draw.text((10,10), 'Blue', font=fonts.load('luBS24'))
            lcd.update()
            sleep(3.75)
            if ts.value():
                sound.speak("Blue").wait()

        elif colors[cl.value()] == "green":
            lcd.draw.text((10,10), 'Green', font=fonts.load('luBS24'))
            lcd.update()
            sleep(3.75)
            if ts.value == True:
                sound.speak("Green")
            
        elif colors[cl.value()] == "Black":
            lcd.draw.text((10,10), 'Black', font=fonts.load('luBS24'))
            lcd.update()
            sleep(3.75)
            
        elif colors[cl.value()] == "white":
            lcd.draw.text((10,10), 'White', font=fonts.load('luBS24'))
            lcd.update()
            sleep(3.75)
            
        elif colors[cl.value()] == "Brown":
            lcd.draw.text((10,10), 'Brown', font=fonts.load('luBS24'))
            lcd.update()
            sleep(3.75)
           
        elif colors[cl.value()] == "yellow":
            lcd.draw.text((10,10), 'Yellow', font=fonts.load('luBS24'))
            lcd.update()
            sleep(3.75)
            while ts.value():
                count = 0
                while count <4:
                    tank_drive.on_for_rotations(SpeedPercent(30), SpeedPercent(30), 1)
                    # put gyro sensor into ANGLE mode
                    gy.mode='GYRO-ANG'
                    gy.mode='GYRO-RATE'
                    gy.mode='GYRO-ANG'

                    mB.run_forever(speed_sp=-75)
                    mC.run_forever(speed_sp=75)
                    # never use == with gyro
                    while gy.value() >=-86: #-90, -87, 86 no posotive 
                        sleep(0.2)
                        mB.stop(stop_action="hold")
                        mC.stop(stop_action="hold")
                        count += 1

"""while not ts.value():
    pass"""



if __name__ == "__main__":
    main()