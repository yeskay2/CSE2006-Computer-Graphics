t = 0;
incr= 0;
def setup():
    size(700,500);
    background(20);
    

def draw():
    global t;
    global incr;
    stroke(255);
    strokeWeight(5);
    translate(width/100, height/2);
    point(t, sin(t*2.2)*150);
    #incr += .000005;
    t+=.255+incr;
    frameRate(500);
  

 
    
