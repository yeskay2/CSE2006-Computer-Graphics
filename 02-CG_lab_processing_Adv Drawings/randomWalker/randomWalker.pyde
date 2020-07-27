import random as r
t = 0
x = 640/2
y = 480/2
opList = ['+','-','*','/']
def setup():
    size(640,480)
    background(255)
random = 0
def draw():
    global x,y,opList,random,t
    ellipse(x,y,30,30)
    random = r.randint(1,5)
    if(random == 1):
        x = x+noise(t)
    if(random == 2):
        x = x-noise(t)
    if(random == 3):
        y = y-noise(t)
    if(random == 4):
        y = y-noise(t)
        
    if(x<=0):
        x = 600/2
    if(y<=0):
        y = 400/2
    if(x>=640):
        x = 600/2
    if(y>=480):
        y = 400/2
        
    t = t+0.1
