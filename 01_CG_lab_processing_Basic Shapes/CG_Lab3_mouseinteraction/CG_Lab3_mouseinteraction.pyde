def setup():
    size(700, 300);
    background(255);
def draw():   
    if (mousePressed):
        strokeWeight(4);
        fill(203,153,10);
        point(mouseX, mouseY);
