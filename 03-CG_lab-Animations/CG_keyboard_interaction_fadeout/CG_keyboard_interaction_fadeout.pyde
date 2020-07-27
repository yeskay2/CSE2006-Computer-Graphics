def setup():
    size(800, 800);
    background('#3355CC');
    
    
def draw():
    fill(40, 20);
    rect(0,0,width, height);
    if (keyPressed==True):
        fill(255);
        textSize(random(10,300));
        text(key,random(100,400),random(200,400));
    #fill(40, 20);
    #rect(0,0,width, height);
    
# def keyPressed():
#     fill('#FFE200');
#     textSize(random(20, 200));
#     text(key, random(300), random(100,400));
