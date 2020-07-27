def setup():
    size(600,600,P3D);
    background(255);
    #frameRate(4);
def draw():
    #pushMatrix();
    lights();
    #background(255);
    stroke(mouseX,mouseY,mouseX/2);
    strokeWeight(4);
    #fill(mouseX/3,mouseX%6,mouseY/4);
    #translate(width/2,height/2);
    #rotate(mouseY);
    
    #sphere(100);
    ellipse(mouseX,mouseY,60,60);
    # print(mouseX,mouseY);
    # print(displayWidth,displayHeight);
    # print(width,height);
    #popMatrix();
    
    
def mousePressed():
    background(255)    
#     #background(255);
    #noFill();
    #ellipse(mouseX,mouseY,60,60);
