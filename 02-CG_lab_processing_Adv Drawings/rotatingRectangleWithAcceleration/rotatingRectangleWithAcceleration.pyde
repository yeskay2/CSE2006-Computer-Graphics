a = 0.0
aVel = 0.0
aAcc = 0.001


def setup():
    size(640,360)
def draw():
    global a,aVel,aAcc
    background(255)
    aAcc = map(mouseX,0,width,-0.01,0.01)
    a = a + aVel
    aVel = aVel + aAcc
    rectMode(CENTER)
    stroke(0)
    fill(127)
    translate(width/2,height/2)
    rotate(a)
    rect(0,0,64,36)
