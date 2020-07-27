def setup():
    size(400,400);
    background(0);
    stroke(255);

def draw():
    if(mousePressed):
        if(mouseX<200 and mouseY<200):
            line(pmouseX,pmouseY,mouseX,mouseY);
    img = get(0,0,200,200);
    pushMatrix();
    translate(0,height);
    scale(1,-1);
    image(img,0,0);
    popMatrix();
 
    pushMatrix();
    translate(width,0);
    scale(-1,1);
    image(img,0,0);
    popMatrix();
