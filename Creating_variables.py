## string manipulation

a = 1
b = 2.5
c = "MyString"

y= a + b
print(y)
print(c)

## user input

Name = input('Enter Your Name:')
Age = input("Enter Your Age:")

print("My Name is:", Name)
print("My Age is:", Age)

## math operators

a = 100
b = 20

z = a + b 
print("z value is", z)

z = a - b
print("z value is", z)

z = a/b
print("z value is", z)

z = a * b
print("z value is", z)

## random number generator

import random

x =random.randint(0,2)
print("random number is:", x)

## Projct Names and Random Score

import random

Name1 = input("Enter First Name:")
Name1RandomNumber = random.randint(0, 10)

Name2 = input("Enter Second Name:")
Name2RandomNumber = random.randint(0, 10)

Name3 = input("Enter Third Name:")
Name3RandomNumber = random.randint(0, 10)

print(Name1, "Got a value of:", Name1RandomNumber)
print(Name2, "Got a valule of:", Name2RandomNumber)
print(Name3, "Got a value of:", Name3RandomNumber)

## if statements

skillpoints = 15

if skillpoints < 15:
    print("Welcome to city 1. THis is the easy part.")
    
  ## if elif else
  
forwardButton = True
  
backwardButton = True 

#0 : no rotation
#1 : clockwise rotation FW
#2 : anti-clockwise rotation BW

motorstatus = 0

if forwardButton == True:
    motorStatus = 1
    print("Car is moving forward")

elif backwardButton == True:
    motorstatus = 2
    print("Car is moving Backward")
    
else:
    motorstatus = 0
    print("Car is not moving")
    
## project grade

grade = int(input("Enter the Grade: "))

if grade>90:
    print("You Got an AA! Congrats!")

elif grade>85:
    print("You Got an BA! Congrats!")

elif grade>80:
    print("You Got an BB! Congrats!")

elif grade>75:
    print("You Got an CB! Congrats!") 
    
elif grade>70:
    print("You Got an CC! Congrats!") 
    
elif grade>65:
    print("You Got an CD! Congrats!")
    
elif grade>60:
    print("You Got an DC!")
    
elif grade>55:
    print("You Got an F! You suck!")
  
  
  