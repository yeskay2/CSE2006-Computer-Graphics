t1 = 3
t2 = 4
colorT = 10
x = noise(t1)
y = noise(t2)
def setup():
    size(640,640)
    background(255)

def draw():
    global x,t1,t2,colorT
    # background((noise(colorT)*100))
    colorT = colorT+0.01
    x = noise(t1)
    y = noise(t2)
    x = x*500
    y = y*500
    t1 = t1+0.01
    t2 = t2+0.01
    noStroke();
    ellipse(x,y,10,10)
    fill(t1,t2,t2,t2+t1/2)
    
