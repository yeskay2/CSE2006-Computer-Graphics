r = 0;
def setup():
    size(400, 400, P3D);
    #frameRate(4000)
def draw():
    global r;
    a = 0;
    #r = 0;
    background(80);
    fill(mouseX%255, mouseY%55,mouseX);
    translate(mouseX, mouseY, map(noise(a), 0, 1, -400, 300));
    rotateY(r);
    box(50);
    a = a + 0.01;
    r = r + 0.02;
