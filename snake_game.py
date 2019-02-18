import turtle
import time
import random

delay=0.25
#Score
score=0
high=0

# set the window
wn=turtle.Screen()
wn.title('Sanke Game')
wn.bgcolor('green')
wn.setup(width=600,height=600)
wn.tracer(0)     # turnes off animation on the screen
segment=[]

#snake head
head=turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('black')
head.penup()
head.goto(0,0)
head.direction='stop'

#snake food
food=turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(0,100)

#scoring the game
pen=turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write('Score: 0   High  Score: 0', align='center', font=('Courier',24,'normal')) 

#Function
def go_up():
    if head.direction!='bottom':
        head.direction='up'

def go_bottom():
    if head.direction!='up':
        head.direction='bottom'

def go_left():
    if head.direction!='right':
        head.direction='left'

def go_right():
    if head.direction!='left':
        head.direction='right'

def move():
    if head.direction=='up':
        y=head.ycor()
        head.sety(y+20)
        
    if head.direction=='bottom':
        y=head.ycor()
        head.sety(y-20)
    
    if head.direction=='left':
        x=head.xcor()
        head.setx(x-20)
    
    if head.direction=='right':
        x=head.xcor()
        head.setx(x+20)

#Keyboard binding
wn.listen()
wn.onkeypress(go_up,'w')
wn.onkeypress(go_bottom,'s')
wn.onkeypress(go_left,'a')
wn.onkeypress(go_right,'d')


#main game loop
while True:
    wn.update()
    #check for boader collission
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction='stop'
        
        #hide the segment
        for segm in segment:
            segm.goto(1000,1000)
        #clear the segment list
        segment.clear()
        #resetting the score
        score=0
        pen.clear()
        pen.write('Score: {}  High Score: {}'.format(score,high),align='center',font=('Courier',24,'normal'))
        
        #resetting time
        delay=0.25
    
    if head.distance(food)<20:
        x= random.randint(-290,290)
        y= random.randint(-290,290)
        food.goto(x,y)
        seg=turtle.Turtle()
        seg.speed(0)
        seg.shape('square')
        seg.color('grey')
        seg.penup()
        segment.append(seg)
        #shorten the delay time
        delay-=0.001
        
        #increase the score
        score+=10
        if score>high:
            high=score
        
        pen.clear()
        pen.write('Score: {}  High Score: {}'.format(score,high),align='center',font=('Courier',24,'normal'))
        
        #Move the end segment first in reverse order
    for index in range(len(segment)-1,0,-1):
        x=segment[index-1].xcor()
        y=segment[index-1].ycor()
        segment[index].goto(x,y)
            
    #Move the segment 0 to where the head is
    if(len(segment)>0):
        x=head.xcor()
        y=head.ycor()
        segment[0].goto(x,y)
        
        
    move()
    #check for the body collission
    for segmen in segment:
        if segmen.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction='stop'
            
            #hide the segment
            for segm in segment:
                segm.goto(1000,1000)
            #clear the segment list
            segment.clear()
            #resetting the score
            score=0
            pen.clear()
            pen.write('Score: {}  High Score: {}'.format(score,high),align='center',font=('Courier',24,'normal'))
            
            #resetting time
            delay=0.25
            
    
    time.sleep(delay)

wn.mainloop()