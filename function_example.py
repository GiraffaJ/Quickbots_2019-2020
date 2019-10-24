# If you use the same kind of process multiple times, it can be more effective to use a function. 

# Think about the kitchen example, you make toast more than once in you're life, so you got a toaster. 
# you give the toaster bread, the toaster performs functions within itself and then returns toast.

# You can do the same thing in programming, too!
# You can make chunks of code that you can call to perform actions for you
# call just means that you're telling python to run the function 

# Here's what the basic formatting of a function looks like: 

def add_numbers(x, y):
	z = x + y
	return z

var = add_numbers(3, 4)
print(var)

# What do you think the code above does? 
# Think about it like a toaster: 
#		1) you give it something
#		2) it modifies what you gave it
# 		3) it gives you back the modified thing

# ANSWER: 7

# Let's go through each building block of a function 

def function_name(parameter1, parameter2):
	change1 = parameter1 + parameter2
	change2 = change1 * 2
	return change2

## def 
#	you have to put def before each function just to let 
#	python know that you are defining a function

## function_name
# 	you can put whatever you'd like here but make sure it
# 	is descriptive of what the function does
# 	Additionally, to call the function, you type the function 
#	name and the the parameters you would like the function
#	to work with inside of the parenthesis
#	Cool tip! You can assign a variable to the results of a function:
variable = function_name(1, 2)

## (parameter1, parameter2):
#	these are parameters, think of these as your bread in the toaster.
#	the names you put here can be whatever you like, just keep in mind, 
#	these variables are *local* to the function that they are with. This
#	means that you cannot use those variables outside of the function and
# 	that they only exist within the function, however, when you are 
#	calling a function, you can use whatever variables you want in the parameter
# 	slots because the parameter names within the functions are only placeholders.

## change1 = parameter1 + parameter2
#	this is simply one of the ways you're manipulating the parameters before
# 	you return them

## change2 = change1 * 2
#	this is just another way you're manipulating the parameters, functions
#	don't have a maximum length so you can change the parameters in as many
# 	ways you'd like. Also, you can call other functions within a function!
# 	Super cool! 

## return change2
#	if you want to keep the changes that a function makes on your parameters
#	you have to use a return statement, this is like when the toast pops out 
# 	of your toaster. This gives you back the changes you made. However, 
# 	a return statement is not required! 


# If you want to make a gyro lock function, here's what the shell could look like:

def gyro_lock(distance, gyro_adjust, speed):
	starting_value = current_gyro_value
	left_wheel_speed = speed
	right_wheel_speed = speed
	while motor_value <= distance:
		while current_gyro_value != starting_value:
			if current_gyro_value > starting_value:
				# adjust wheel speeds
				# adjust gryo_adjust if needed
			if current_gyro_value < starting_value:
				# adjust wheel speeds
				# adjust gyro adjust if needed

# Another cool thing you can do is use functions that you've created in other files
# for example, if you have a function called gyro_turn in a file called program3.py
# but you want to use your gyro_turn function in this file, you can import it just like
# you import different motor functions:

from program3 import gyro_turn

# Then you can use the gyro_turn function in the new file just as you'd use it normally
# super cool!

# Let me know if you all have any questions!