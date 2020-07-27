from random import randint
from processing import *

numberOfParticules = 100;
position=[]
velocity=[]
lifespan=[]
color=1

def setup():
    size(600,300)
    frameRate(24)  
    background(0) 
    stroke(255)
    strokeWeight(2)
    global numberOfParticules
    global position
    global velocity
    global lifespan
    for i in range(0, numberOfParticules):
        position.append([0,0])
        if (i < numberOfParticules/2):
            velocity.append([randint(-2,2), randint(-10,-5)])
            lifespan.append(randint(20,40))
        else: 
            velocity.append([0,0])
            lifespan.append(randint(0,40))

def draw():
    global color
    global numberOfParticules    
    global position
    global velocity
    global lifespan    
  
    background(0)
    for i in range(0, numberOfParticules):
      color=i%5
      if color==0:
        stroke(255,255,255)    
      elif color==1:
        stroke(255,255,0)
      elif color==2:
        stroke(255,0,255)
      elif color==3:
        stroke(0,255,0)
      elif color==4:
        stroke(0,255,255)        
      
      point(position[i][0] + 150, position[i][1] + 300 )

      position[i][0]+=velocity[i][0]
      position[i][1]+=velocity[i][1]
      #Add Gravity
      velocity[i][1]+=0.2
      point(position[i][0] + 150, position[i][1] + 300 )
      
      
      point(position[i][0] + 450, position[i][1] + 150 )

      position[i][0]+=velocity[i][0]
      position[i][1]+=velocity[i][1]
      #Add Gravity
      velocity[i][1]+=0.2
      point(position[i][0] + 450, position[i][1] + 150 )
      
      
      #When a particules dies, another one appears
      lifespan[i]-=1
      if (lifespan[i] < 0): 
        velocity[i] = [randint(-2,2), randint(-10,-5)]
        position[i] = [0,0]
        lifespan[i] = randint(0,40)
        
def keyPressed():
    textSize(23)
    text("Color fountain",10, 30);
    #print('A key was pressed', keyboard.key)
    #exitp()
    
def keyReleased() :
    
    exit()
