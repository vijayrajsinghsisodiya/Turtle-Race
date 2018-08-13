# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 21:32:22 2018

@author: Vijay
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 19:36:45 2018

@author: Vijay
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 19:08:25 2018

@author: Vijay
"""

from turtle import *                    # Turtle is a predefined module
import time                             # time module used for various function likes sleep,pause,stop,etc
from random import randint              # random module used for generating random no's 

w=Screen()
w.bgcolor("dark grey")                    # sets the background colour for screen

penup()                                 # Pull the pen up – no drawing when moving
goto(-100,140)                          # Move turtle to an absolute position(-100,140)
for step in range(15):
    speed(6)                            # Set the turtle’s speed to an integer value(set to 6) in the range 0..10   
    if step == 14:
        x,y=position()                  # Return the turtle’s current location (x,y)
        x=x-5
        hideturtle()                    # Make the turtle invisible.it can be also written as ht()
    pencolor("red")                     # Return or set the pencolor to red
    write(step)                         #
    right(90)                           # turn turtle right by angle units(90)
    forward(10)                         # Move the turtle forward by the specified distance(10)
    pendown()                           # Pull the pen down – drawing when moving.
    forward(150)
    penup()                             #Pull the pen up – no drawing when moving.
    backward(160)                       # Move the turtle forward by the specified distance(10)
    left(90)                            # turn turtle left by angle units(90)
    forward(20)
    

clr=["red","black","blue","yellow"]       # creating a list for selecting colours of turtle
trtl=[]                                    # creating an empty list for storing turtle's object
y=10
for i in range(4):    
    trtl.append(Turtle())                  # Updating the list(t) by adding an object(Turtle) to the list.append()
    trtl[i].right(360)                     # rotating the turtle by an angle(360)
    trtl[i].color(clr[i])                   # setting the colour of turtle
    trtl[i].shape("turtle")                # Set turtle shape to shape with given name ("turtle")
    trtl[i].penup()
    trtl[i].goto(-120,y)                   # Move turtle to an absolute position(-110,y=10)
    y=y+30
    trtl[i].pendown()
w=Turtle()                                  # creates new object(w) of type turtle
w.shape("turtle")
w.color("navy blue")
w.penup()
w.goto(20,200)
w.pendown()         
w.clear()                                                               #Delete the turtle’s drawings from the screen
w.write("3", move=False, align="center", font=("Arial", 50, "normal"))  # Write text on the screen
time.sleep(1)                                                           # it pauses program for given time in secconds
w.clear()
w.write("2", move=False, align="center", font=("Arial", 50, "normal"))
time.sleep(1)
w.clear()
w.write("1", move=False, align="center", font=("Arial", 50, "normal"))
time.sleep(1)
w.clear()
w.write("go", move=False, align="center", font=("Arial", 50, "normal"))

def display_stars():                                                    # function made for creating stars
    star_color=["red","green","yellow","blue","light green","black","purple","cyan"] # list of colors used in stars
    x=50
    y=-70
    speed(10)
    for i in range(8):
            goto(x,y)
            angle = 120
            fillcolor(star_color[randint(0,7)])     # set fillcolor to colorstring, which is a Tk color specification string, such as "red", "yellow", or "#33cc8c"
            begin_fill()                            # it is called before drawing a shape to be filled.
            for side in range(5):
                forward(10)
                right(angle)
                forward(10)
                right(72 - angle)    
            end_fill()                              # Fill the shape drawn after the last call to begin_fill()
            x=randint(-100,250)                     # genarating a random no. between(-100,250) used for setting position of turtle 
            y=randint(-10,200)
            
def winner(c):                                  # function created for displaying winner info on the screen
    goto(0,-70)
    pencolor(c)
    write(f"{c} colour turtle won the game",align="center", font=('MS Sans Serif', 30, "normal"))
    #color(c)                                
    display_stars()                                  # display_stars funcion is called       
    goto(0,-130)
    write("click anywher on Screen to exit", move=False, align="center", font=('arial',20, "italic"))
    exitonclick() # Bind bye() method(Shut the turtlegraphics window) to mouse clicks on the Screen.
    

for i in range(96):                     # loop used for moving turtles on the track
    trtl[0].forward(randint(1,5))
    a,b=trtl[0].position()
    trtl[1].forward(randint(1,5))
    c,d=trtl[1].position()
    trtl[2].forward(randint(1,5))
    e,f=trtl[2].position()
    trtl[3].forward(randint(1,5))
    g,h=trtl[3].position()
    if x<=a:                            # checking if turtle(in this a) wins then calls
        winner("red")                   # calling function winner(passing "color" as argument)
    elif x<=c:
        winner("black")
    elif x<=e:
        winner("blue")
    elif x<=g:
        winner("yellow")
    
