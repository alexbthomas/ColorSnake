#imports
import turtle
import random
import time

#creating screen
screen = turtle.Screen()
screen.setup(600, 500)
screen.bgcolor("black")
screen.tracer(0)

speed = 2
p1score = 0

#snake turtle object
head = turtle.Turtle()
head.penup()
head.speed(0)
head.color("#38ff7a")
head.shape("circle")
head.goto(0,0)
head.direction = "stop"

#food turtle object
food = turtle.Turtle()
food.penup()
food.speed(0)
food.color("#03fcf8")
food.shape("circle")
food.goto(0,100)

#turtle responsible for drawing score
scorepen1 = turtle.Turtle()
scorepen1.hideturtle()
scorepen1.speed(0)
scorepen1.color("#FFFB00")
scorepen1.penup()
scorepen1.goto(-250, 200)
scorestring = "%s" %p1score
scorepen1.write(scorestring, False, align = "left", font =("Arial", 14, "normal"))


#keeps track of high score
file = open("Scores.txt", "r")
c = 12
currentHigh = file.readline()[c]
while file.read()[c + 1] != '\n':
  currentHigh = currentHigh + file.read()[c + 1]
  c+=1
file.close()

#turtle responsible for drawing highscore
highscorepen1 = turtle.Turtle()
highscorepen1.hideturtle()
highscorepen1.speed(0)
highscorepen1.color("#FFFB00")
highscorepen1.penup()
highscorepen1.goto(140, 205)
highscorestring = "HIGH SCORE: %s" %currentHigh
highscorepen1.write(highscorestring, False, align = "left", font =("Arial", 14, "normal"))

segments = []
bfood = []

#movement functions
def up():
  head.direction = "up"
  
def down():
  head.direction = "down"
  
def right():
  head.direction = "right"
  
def left():
  head.direction = "left"

def move():
  if head.direction == "up":
    y = head.ycor()
    head.sety(y + speed)
  if head.direction == "down":
    y = head.ycor()
    head.sety(y - speed)
  if head.direction == "right":
    x = head.xcor()
    head.setx(x + speed)
  if head.direction == "left":
    x = head.xcor()
    head.setx(x - speed)
    
#function to check for new highscore
def highscore(score):
  global currentHigh
  if p1score > int(currentHigh):
    file = open("Scores.txt", "w")
    #currentHigh = file.read()[12]
    file.write("HIGH SCORE: " + str(p1score))
    file.close()
  
#function to update score
def scoreupdate(player):
  if(player == 1):
    scorepen1.clear()
    scorestring = "%s" %p1score
    scorepen1.write(scorestring, False, align = "left", font =("Arial", 14, "normal"))
    
#key binding
screen.onkey(up, "w")
screen.onkey(down, "s")
screen.onkey(right, "d")
screen.onkey(left, "a")
screen.listen()

#main game loop
while True:
  screen.update()
  move()
  if head.distance(food) < 20:
    p1score+=1
    scoreupdate(1)
    food.goto(random.randint(-250, 250), random.randint(-220, 220))
    speed += .3
    
    #creation of new segment
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.penup()
    new_segment.shape("circle")
    
    #segment color
    colorChance = random.randint(1, 5)
    if colorChance == 1:
      new_segment.color("#38ff7a")
    if colorChance == 2:
      new_segment.color("#fcf803")#00ff55
    if colorChance == 3:
      new_segment.color("#03dffc")
    if colorChance == 4:
      new_segment.color("#fc03db")
    if colorChance == 5:
      new_segment.color("#ff0000")
    segments.append(new_segment)
    
    #bad food spawn
    bchance = random.randint(1, 5)
    if bchance == 1:
      bad_food = turtle.Turtle()
      bad_food.penup()
      bad_food.speed(0)
      bad_food.color("#ff5338")
      bad_food.shape("circle")
      bfood.append(bad_food)
      bfood[len(bfood) - 1].goto(random.randint(-250, 250), random.randint(-250, 250))
      
  #addition of segment on snake
  for index in range(len(segments) - 1, 0, -1):
    x = segments[index - 1].xcor()
    y = segments[index - 1].ycor()
    segments[index].goto(x, y)
  
  if len(segments) > 0:
    x = head.xcor()
    y = head.ycor()
    segments[0].goto(x, y)
    
  #border collision detection 
  if head.ycor() > 240:
    highscore(p1score)
    exit()
  if head.ycor() < -240:
    highscore(p1score)
    exit()
  if head.xcor() > 290:
    highscore(p1score)
    exit()
  if head.xcor() < -290:
    highscore(p1score)
    exit()
    
  #bad food collision detection
  for index in range(len(bfood)):
    if head.distance(bfood[index]) < 18:
      highscore(p1score)
      exit()
  
screen.mainloop()

