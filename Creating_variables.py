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
  
  
## lists

names= ["James","Elli","MrHamsho","Adem","Aida"]
ages= [24, 25, 21, 48, 17]
print(names[5], ages[5] )

## list append

shoppingCart = ['Oranges', 'Milk', 'Almonds']

item = input("please enter the name of the product:")
shoppingCart.append(item)

item = input("please enter the name of the product:")
shoppingCart.append(item)

item = input("please enter the name of the product:")
shoppingCart.append(item)

print("Your items are:", shoppingCart)

shoppingCart = ['Oranges', 'Milk', 'Almonds']
shoppingCart.clear()
print(shoppingCart)

shoppingCart = ['Oranges', 'Milk', 'Almonds']
shoppingCart.remove("Almond")
print(shoppingCart)

shoppingCart = ['Oranges', 'Milk', 'Almonds']

shoppingCart.pop()
print(shoppingCart)

shoppingCart = ['Oranges', 'Milk', 'Almonds']

length = len(shoppingCart)
print(length)

shoppingCart.clear()

if len(shoppingCart) == 0:
    print("Your shopping cart is empty!")

database = [ ["John", "MrHamsho"]  , [25, 29] ]

print(database[0][1])
print(database[1][1])

while(1):
    userInput = input("Enter a letter")
    print(userInput)
    
    if userInput == 'exit':
        break 
    
t = ("A", "B", "C")

## finite machines

state=1
while(1):
    transit = input("Enter a letter: ")
    print("You have entered", state)
    
    if state == 1:
        if transit == 'W':
            state = 2

    elif state == 2:
    
        if transit == 'G':
            state = 3
        
        elif state == 2:
            if transit == 'G':
                state= 3
            
            elif transit == 'S':
                state=1
                
        elif state == 3:
            if transit == 'L':
                state=1
        print("Right NOw you are in state:", state)
        
        