import random as r 

pos = [10,10]
vel = [0,0]
acc = [0.01,0.01]

def setup():
    size(640,640)
    background(255)
    
def draw():
    global pos,acc,vel
    ellipse(pos[0],pos[1],10,10)
    pos[0] += vel[0]
    pos[1] += vel[1]
    vel[0] += acc[0]
    vel[1] += acc[1]
    acc = [r.randrange(0,2)*2,r.randrange(0,2)**2]
    if(pos[0]>=400 or pos[0]>=400):
        acc = [-r.randrange(0,1),-r.randrange(0,1)]
