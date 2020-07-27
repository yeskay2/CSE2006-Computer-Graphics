def setup():
    size(800, 600, P3D)
    background(255)
    
def draw():
    pushMatrix()
    translate(400, 300)
    line(0, 0, mouseX - 400, mouseY - 300)
    popMatrix()
    clearScreen();
    
def clearScreen():
    if mousePressed:
        background(255)
