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
        
        ## Enumerate
        
    cars = ["BMW", "Hyundai", "Toyota", "Jaguar"]
    
    for i, items in enumerate(cars):
        print(items)
        print(i)
        
l = ["apples", "bananas", "strawberries"]
 
for element in l:
    print(element)
    
a = [1,3,5,7,9]

for element in a:
    element= element+2
    print(element)
    
for i in range (0, len(a) ):
    a[1] = a[i] + 2
    
print(a)

shapes = ["square", "circle", "triangle"]
centers = [ (10,10), (50,50), (100,100)]
colors = ["red", "blue", "yellow"]

#for i in range (0, len(shapes)):
#   print(shapes[1], centers[1])

for shape, center, color in zip(shapes, centers, colors):
    print(shape, center, color)
    
s= "This is nice"
#print(s)

li0ifNumbers = [x for x in range(10) if x%2 ==0]
print(li0ifNumbers)

#4px x 4px
# 16x x 16x

imagePixels = [ 
               [0,0], [1,0], [2.0], [3.0]
               [0.1], [1.1], [2.1], [3.1]
               [0.2], [1.2], [2.2], [3.2]
               [0.3], [1.3], [2.3], [3.3]
               
            ]

#shift x axis 3 pixles to the right 
for i in range(0 , len(imagePixels)):
    imagePixels[i][0]= imagePixels[i][0] + 3

print(imagePixels)

#shift Y axis 2 pixels downwards
for i in range(0 , len(imagePixels)):
    imagePixels[i][0]= imagePixels[i][0] + 2
    
print(imagePixels)

## functions

db1=["kate", "Moss", "David"]
db2=["Lee", "Steve"]
db3=["Tony", "Lara"]

def addToDatabase(name):
    
    global db1
    global db2
    global db3
    
    db1=[name]
    db2=[name]
    db3=[name]
    
    
addToDatabase('John')
addToDatabase("MrHamsho")
print("Db 1 is:", db1)
print("Db 2 is:", db2)
print("Db 3 is:", db3)

def pwr2(num):
    pw2= num*num
    div = num/num
    return pw2, div

pw2, div= pwr2(5)
print("pw2 is ", pw2)
print("div is ", div)

import turtle


screen = turtle.Screen()
screen.title("PingPong")
screen.bgcolor("Blue")
screen.setup(width=800, height=600)
screen.tracer(0)


paddle_1 = turtle.Turtle()
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350,0)


paddle_2 = turtle.Turtle()
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350,0)

ball = turtle.Turtle()
ball.shape("circle")
ball.color("Green")
ball.penup()
ball.goto(0,0)
ball.dx = 0.1
ball.dy = -0.1

score1= 0
score2= 0
scoreText = turtle.Turtle()

scoreText.color("white")
scoreText.hideturtle()
scoreText.penup()
scoreText.goto(0,260)
scoreText.write("Player 1 : 0  Player 2 : 0", align="center", font=("Courier",22,"normal"))
step = 10

def moveBall():
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ ball.dy)
    
    x = ball.xcor()
    y = ball.ycor()
    
    if x>390:
        ball.setx(390)
        ball.dx = ball.dx * -1
    if x <-390:
        ball.setx(-390)
        ball.dx = ball.dx * -1
    
    if y >290:
        ball.sety(290)
        ball.dy = ball.dy * -1
        
    if y <-290:
        ball.sety(-290)
        ball.dy =ball.dy * -1
        
        

  
    

def paddle_1_up():
    y = paddle_1.ycor()
    y = y+step
    paddle_1.sety(y)
    if  y > 240:
        paddle_1.sety(240)
    
def paddle_1_down():
    y = paddle_1.ycor()
    y = y-step
    paddle_1.sety(y)
    if y<-240:
        paddle_1.sety(-240)
        
def paddle_1_right():
    x =  paddle_1.xcor()
    x= x+step
    paddle_1.setx(x) 
    if x >-10:
        paddle_1.setx(-10)

def paddle_1_left():
    x =  paddle_1.xcor()
    x= x-step
    paddle_1.setx(x) 
    if x <-350:
        paddle_1.setx(-350)

def paddle_2_left():
    x =  paddle_2.xcor()
    x= x-step
    paddle_2.setx(x) 
    if x <10:
        paddle_2.setx(10)

def paddle_2_right():
    x =  paddle_2.xcor()
    x= x+step
    paddle_2.setx(x) 
    if x >350:
        paddle_2.setx(350)        


def paddle_2_down():
    y = paddle_2.ycor()
    y = y-step
    paddle_2.sety(y)
    if y<-240:
        paddle_2.sety(-240)

def paddle_2_up():
    y = paddle_2.ycor()
    y = y+10
    paddle_2.sety(y)
    if  y > 240:
        paddle_2.sety(240)
        
        

def checkCollision():
    if (paddle_1.xcor()+20 >=  ball.xcor() >= paddle_1.xcor()-20) and (paddle_1.ycor()+60 >=  ball.ycor() >= paddle_1.ycor()-60):
        ball.dx = ball.dx*-1
        ball.dy = ball.dy *-1
        
        x = ball.xcor()
        x= x+10
        ball.setx(x)
    
    if (paddle_2.xcor()+20 >=  ball.xcor() >= paddle_2.xcor()-20) and (paddle_2.ycor()+60 >=  ball.ycor() >= paddle_2.ycor()-60):
        ball.dx = ball.dx*-1
        ball.dy = ball.dy *-1
        
        x = ball.xcor()
        x= x-10
        ball.setx(x) 

def xx (par):
    return par/10

x = lambda x: x/10

print(xx(50))

l = ['a','b','c',' ',' ']

filteredList = list(filter(lambda x: x!=' ',l))
print(filteredList)

appendList = list(map(lambda x: x+"d",l))
print(appendList)

