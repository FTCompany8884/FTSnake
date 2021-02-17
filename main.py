import turtle
import time
import random
d = 0.1
score = 0
hscore = 0
win = turtle.Screen()
win.title('FT snake')
win.bgcolor('chartreuse')
win.setup(width = 600, height = 600)
win.cv._rootwindow.resizable(False, False)
win.tracer(0)
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('blue')
head.penup()
head.goto(0, 0)
head.direction = 'stop'
apple = turtle.Turtle()
apple.speed(0)
apple.shape('circle')
apple.color('red')
apple.penup()
apple.goto(140, 110)
segments = []
pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('black')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.clear()
pen.write('Score: 0   High score: 0' , align = 'center' , font = ('Courier' , 24 , 'normal'))
def goup():
    if head.direction != 'down':
        head.direction = 'up'
def godown():
    if head.direction != 'up':
        head.direction = 'down'
def goleft():
    if head.direction != 'right':
        head.direction = 'left'
def goright():
    if head.direction != 'left':
        head.direction = 'right'
def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)
win.listen()
win.onkeypress(goup, 'Up')
win.onkeypress(godown, 'Down')
win.onkeypress(goleft, 'Left')
win.onkeypress(goright, 'Right')
while True:
    win.update()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0 , 0)
        head.direction = 'stop' 
        for segment in segments:
            segment.goto(1000 , 1000)
        segments.clear()
        score = 0
        d = 0.1
        pen.clear() 
        pen.write('Score: {}   High score: {} '.format(score , hscore) , align = 'center' , font = ('Courier' , 24 , 'normal'))
    if head.distance(apple) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-240, 240)
        apple.goto(x, y)
        nsegments = turtle.Turtle()
        nsegments.speed(0)
        nsegments.shape('square')
        nsegments.color('dodger blue')
        nsegments.penup()
        segments.append(nsegments)
        d -= 0.001
        score += 10
        if score > hscore:
            hscore = score
        pen.clear() 
        pen.write('Score: {}   High score: {} '.format(score , hscore) , align = 'center' , font = ('Courier' , 24 , 'normal'))
    for index in range(len(segments) -1, 0, -1):
        x = segments[index -1].xcor()
        y = segments[index -1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto( 0 , 0)
            head.direction = 'stop'
            for segment in segments:
                segment.goto(1000 , 1000)
            segments.clear()
            score = 0
            d = 0.1
            pen.clear() 
            pen.write('Score: {}   High score: {} '.format(score , hscore) , align = 'center' , font = ('Courier' , 24 , 'normal'))
    time.sleep(d)
win.mainloop()
