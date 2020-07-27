def setup():
    global leftViewport, rightViewport;
    size(300, 300,  P3D); #PointLineCAD 3D Drawing 
    
    leftViewport = createGraphics(width/2, height);
    rightViewport = createGraphics(width/2, height);

def draw():
    

    leftViewport.beginDraw();
    leftViewport.background(102);
    leftViewport.stroke(255);
    leftViewport.line(40, 40, mouseX, mouseY);
    leftViewport.endDraw();

    rightViewport.beginDraw();
    rightViewport.background(102);
    rightViewport.stroke(255);
    rightViewport.line(40, 40, mouseX, mouseY);
    rightViewport.endDraw();
    image(leftViewport, 0, 0);
    image(rightViewport, width/2, 0);
