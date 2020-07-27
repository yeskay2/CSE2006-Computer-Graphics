def setup():
    global viewport;
    size(700, 300,  P3D);
    viewport = createGraphics(400, 200);
def draw():
    viewport.beginDraw();
    viewport.background(51);
    viewport.noFill();
    viewport.stroke(255);
    viewport.endDraw();
    image(viewport, 120, 60); 
