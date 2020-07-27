def setup():
    global viewport;
    size(700, 300,  P3D);
    viewport = createGraphics(400, 200);
def draw():    
    fill(0, 12);
    rect(0, 0, width, height);
    fill(255);
    noStroke();
    ellipse(mouseX, mouseY, 60, 60);
  
    viewport.beginDraw();
    viewport.background(51);
    viewport.noFill();
    viewport.stroke(255);
    viewport.ellipse(mouseX-120, mouseY-60, 60, 60);
    viewport.endDraw();
    image(viewport, 120, 60); 
