def setup():
    size(400,400)
    background(255);
def draw():
    if (mousePressed == True):
        strokeWeight(5);
        fill(mouseX,mouseY,mouseX/2);
        point(mouseX,mouseY);

def keyPressed():
    if(keyCode == 83):
        save("my_drawing.png");
