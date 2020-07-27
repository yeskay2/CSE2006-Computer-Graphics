#add_library('sound')


add_library('sound');
x = 0;
y =0;
len1 = 0;
yspeed =0;
z =0;
rain=1000;
g=0.02;
def setup():
    global sf;
    global rain;
    background(255);
    sf = SoundFile(this, "rain.wav");
    size(1000,1000);
    stroke(0,102,204);
def drop():
    global len1;
    global yspeed;
    global z;
    global x;
    global y;
    len1=random(4,8);
    yspeed=random(2.5,4.5);
    x=random(0,width);
    y=random(-height,height);
    z=random(0,10);

def update():
    global g;
    global yspeed;
    global y;
    y+=yspeed*z;
    yspeed+=g;
    if (y>height):
        y=random(-height,0);
        yspeed=random(1.5,3);

def show():
    strokeWeight(z);
    line(x,y,x,y+len1);

def mouseClicked():
    
    background(255);
    #sf.stop();

def draw():
    sf.play();

    drop();
    update();
    show();
    sf.stop();

# def keyPressed():
    # sf.loop();
