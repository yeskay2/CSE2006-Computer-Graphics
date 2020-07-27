
def setup():
    global rightkey, leftkey, upkey, downkey , space
    rightkey = False; 
    leftkey = False;
    upkey = False; 
    downkey = False; 
    space = False;
    
    size(700, 300,  P3D);
    
    background(255);
    
def draw(): 
    x = width/2;
    y = height/2;
    if (rightkey):
        x+=1;
    if (leftkey):
        x-=1;
    if (upkey) :
        y-=1;
    if (downkey) :
        y+=1;
    if (space): 
        fillColor = color(random(255),random(255),random(255));
    ellipseMode(CENTER);
    fill(100);
    ellipse(x,y,20,20);   

def keyPressed():
    if (keyCode == 39):
        print keyCode;
        rightkey = True;
    if (keyCode == 37):
        leftkey = True;
    if (keyCode == 38):
        upkey = True;
    if (keyCode == 40):
        downkey = True;
    if (keyCode == 32):
        space = True;    
        
def keyReleased():
    
    if (keyCode == 39):
        rightkey = False;
    if (keyCode == 37):
        leftkey = False;
    if (keyCode == 38):
        upkey = False;
    if (keyCode == 40):
        downkey = False;
    if (keyCode == 32):
        space = False;    
    
