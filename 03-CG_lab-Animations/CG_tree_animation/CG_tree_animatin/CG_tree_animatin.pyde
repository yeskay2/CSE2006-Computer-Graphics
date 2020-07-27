theta = 0;
 
def setup():
    size(600, 400);

 
def draw():
    global theta;
    background(255);
    theta = map(mouseX,0,width,0,PI/2);
    translate(width/2, height);
    stroke(0);
    branch(300);

def branch(len):
    stroke(mouseX*2,mouseY%255,mouseX*7);
    line(0, 0, 0, -len);
    translate(0, -len);
  
    len *= 0.66;
    
    if (len > 2):
        pushMatrix();
        
        rotate(theta);
        
        branch(len);
        noFill();
        popMatrix();
    
        pushMatrix();
        fill(mouseX/2,mouseY/2,mouseX);
        rotate(-theta);
        branch(len);
        noFill();
        popMatrix();
