"""import turtle
import random
import math
import time
numofapples = 20

wn = turtle.Screen()

wn.bgcolor("white")
turtle.ht()
turtle.setundobuffer(1)
turtle.tracer(0)

wn.register_shape("head",((-30,0),(-30,30),(-20,0),(20,0),(30,30),(30,0),(20,-20),(-20,-20)))

border = turtle.Turtle()
border.ht()
border.speed(0)
border.color("black")
border.pu()
border.goto(-300,300)
border.pd()

for i in range(4):
    border.fd(600)
    border.rt(90)
border.pu()
border.ht()

class Sprite(turtle.Turtle):
    def __init__( self ,spriteshape,color,startx,starty):
        turtle.Turtle.__init__(self, shape = spriteshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.goto(startx,starty)
        self.speed= 1
        
    def collision(t1,t2):
        distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
        
        if distance < 30:
            return True
        else:
            return False
            
    def catch(head,apple):
        if apple.ycor()<-220 and apple.ycor()>-250 and apple.xcor()>head.xcor()-30 and apple.xcor()<head.xcor()+30:
            return True
        else:
            return False
        
class P1(Sprite):
    def __init__(  self ,spriteshape,color,startx,starty):
        Sprite.__init__( self ,spriteshape,color,startx,starty)
        self.pu()
        self.setheading(90)
        self.leftt = False
        self.rightt = False
        self.color(color)
        self.goto(startx,starty)
        self.speed= 10
    
    def left(self):
        self.leftt = True
	
    def right(self):
        self.rightt = True
			
    def lefty(self):
        self.leftt = False
    
    def righty(self):
        self.rightt = False
        
    def move(self):
        x = self.xcor()
		
        if self.leftt==True:
            x-=5
            self.setposition(x,self.ycor())
            # Check for left border
            if self.xcor()<-250:
                self.setx(-250)	
                
        if self.rightt==True:
            x+=5
            self.setposition(x,self.ycor())
            # Check for right border
            if self.xcor()>250:
                self.setx(250)	
        
class Apple(Sprite):
     def __init__(self,spriteshape,color,startx,starty):
        Sprite.__init__(self,spriteshape,color,startx,starty)
        self.pu()
        self.color(color)
        self.goto(startx,starty)
        self.speed= 3
        
     def move(self):
        self.setheading(270)
        self.fd(self.speed)
        if self.ycor()<-300:
            self.setposition(random.randint(-250,250),random.randint(350,1000))
        if Sprite.catch(p1, apple):
            self.setposition(random.randint(-250,250),random.randint(350,1000))
        
apples = []
for i in range(numofapples):
    apples.append(Apple("circle","red",random.randint(-250,250),random.randint(350,1000)))
    
p1 = P1("head","brown",0,-250)

turtle.listen()
turtle.onkeypress(p1.left,"Left")
turtle.onkeypress(p1.right,"Right")
turtle.onkeyrelease(p1.lefty,"Left")
turtle.onkeyrelease(p1.righty,"Right")

while True:
    turtle.update()
    for apple in apples:
        apple.move()
    p1.move()
"""
"""
import pyautogui as pya
from pynput.mouse import Button, Controller
from time import sleep
from random import randint
mouse = Controller()
print(mouse.position)
#mouse.move(100,-30)
#mouse.click(Button.left,2)
#mouse.scroll(0,-20)
sleep(2)
pya.moveTo(525,461)
mouse.press(Button.left)

pya.moveTo(522,760)
pya.moveTo(1317,764)
pya.moveTo(1318,461)
pya.moveTo(525,461)
pya.moveTo(935, 289)
pya.moveTo(1318,461)
mouse.release(Button.left)
pya.moveTo(850, 760)
mouse.press(Button.left)
pya.moveTo(851, 563)
pya.moveTo(995, 563)
pya.moveTo(999, 760)
mouse.release(Button.left)
#lay binh son
pya.moveTo(316, 83)
pya.click()
#chon mau do
pya.moveTo(970, 72)
pya.click()
#to mai nha
pya.moveTo(921, 379)
pya.click()
#lay mau vang
pya.moveTo(1026, 72)
pya.click()
#to mau tuong
pya.moveTo(757, 549)
pya.click()
#lay mau xanh
pya.moveTo(1079, 70)
pya.click()
#to mau cua
pya.moveTo(922, 655)
pya.click()"""

"""(525,461)
press
(522,760)
,(1317,764)
(1318,461)
(525,461),
(935, 289)
,(1318,461),
release
(850, 760)
press
,(851, 563)(995, 563),(999, 760)"""
"""
for i in range(200):
	a = randint(100,1800)
	b= randint(100,1000)
	pya.moveTo(a,b)
"""
import pyautogui as pya
from pynput.mouse import Button, Controller
from time import sleep
from random import randint
mouse = Controller()
print(mouse.position)


