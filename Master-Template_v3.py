#!/usr/bin/env python3
from ev3dev.ev3 import *
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank, MediumMotor, OUTPUT_D, OUTPUT_A 
from time import sleep
from ev3dev2.motor import Motor
# to say words put "Sound.speak("whatever you want to say") "
#turns out you don't need to do anything special for a global python variable, you just have to treat it like a normal variable

program_running = 0

def main():
    def Launchrun():
        btn = Button()
#if the button is pressed, wait a quarter of a second and then if the button is pressed again run option 1 if else run option 2
        def up(state):
            if state:
                sleep(0.25)
                Sound.beep().wait         
                if state:
                    Program1()
                    program_running = 1
                else:
                    Program2()
                    program_running = 1
        def enter(state):
            if state:
                sleep(0.25)
                Sound.beep().wait
                if state:
                    Program3()
                    program_running = 1
                else:
                    Program4()
                    program_running = 1
        def down(state):
            if state:
                sleep(0.25)
                Sound.beep().wait      
                if state:    
                    Program5()
                    program_running = 1
                else:
                    Program6()
                    program_running = 1
        def left(state):
            if state:
                sleep(0.25)
                Sound.beep().wait
                if state:           
                    Program7()
                    program_running = 1
                else:
                    Program8()
                    program_running = 1
        def right(state):
            if state:
                sleep(0.25)
                Sound.beep().wait 
                if state:
                    Program7()
                    program_running = 1
                else:
                    Program8()
                    program_running = 1
#while a program is not running check the button state
        btn.on_left = left   
        btn.on_right = right 
        btn.on_up = up 
        btn.on_down = down 
        btn.on_enter = enter
        while program_running == 0:
            btn.process()
#defining each program
    def Program1():
        Sound.speak("program one")
        program_running = 0
        Launchrun()  

    def Program2():
        Sound.speak("program two")
        program_running = 0
        Launchrun()  

    def Program3():
        Sound.speak("program three")
        program_running = 0
        Launchrun()  


    def Program4():
        Sound.speak("program four")
        program_running = 0
        Launchrun()  

    def Program5():
        Sound.speak("program five")
        program_running = 0
        Launchrun()  

    def Program6():
        Sound.speak("program six")
        program_running = 0
        Launchrun()  

    def Program7():
        Sound.speak("program seven")
        program_running = 0
        Launchrun()  


    def Program8():
        Sound.speak("program eight")
        program_running = 0
        Launchrun()  
# Defining launchrun
if __name__ == "__main__":
    main()    #!/usr/bin/env python3
from ev3dev.ev3 import *
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank, MediumMotor, OUTPUT_D, OUTPUT_A 
from time import sleep
from ev3dev2.motor import Motor
# to say words put "Sound.speak("whatever you want to say") "
#turns out you don't need to do anything special for a global python variable, you just have to treat it like a normal variable

program_running = 0

def main():
    def Launchrun():
        btn = Button()
#if the button is pressed, wait a quarter of a second and then if the button is pressed again run option 1 if else run option 2
        def up(state):
            if state:
                sleep(0.25)
                Sound.beep().wait   
                btn.process()      
                if state:
                    Program1()
                    program_running = 1
                else:
                    Program2()
                    program_running = 1
        def enter(state):
            if state:
                sleep(0.25)
                Sound.beep().wait
                btn.process()
                if state:
                    Program3()
                    program_running = 1
                else:
                    Program4()
                    program_running = 1
        def down(state):
            if state:
                sleep(0.25)
                Sound.beep().wait      
                btn.process()
                if state:    
                    Program5()
                    program_running = 1
                else:
                    Program6()
                    program_running = 1
        def left(state):
            if state:
                sleep(0.25)
                Sound.beep().wait
                btn.process()
                if state:           
                    Program7()
                    program_running = 1
                else:
                    Program8()
                    program_running = 1
        def right(state):
            if state:
                sleep(0.25)
                Sound.beep().wait 
                btn.process()
                if state:
                    Program7()
                    program_running = 1
                else:
                    Program8()
                    program_running = 1
#while a program is not running check the button state
        btn.on_left = left   
        btn.on_right = right 
        btn.on_up = up 
        btn.on_down = down 
        btn.on_enter = enter
        while program_running == 0:
            btn.process()
#defining each program
    def Program1():
        Sound.speak("program one")
        program_running = 0
        Launchrun()  

    def Program2():
        Sound.speak("program two")
        program_running = 0
        Launchrun()  

    def Program3():
        Sound.speak("program three")
        program_running = 0
        Launchrun()  


    def Program4():
        Sound.speak("program four")
        program_running = 0
        Launchrun()  

    def Program5():
        Sound.speak("program five")
        program_running = 0
        Launchrun()  

    def Program6():
        Sound.speak("program six")
        program_running = 0
        Launchrun()  

    def Program7():
        Sound.speak("program seven")
        program_running = 0
        Launchrun()  


    def Program8():
        Sound.speak("program eight")
        program_running = 0
        Launchrun()  
# Defining launchrun
if __name__ == "__main__":
    main()    