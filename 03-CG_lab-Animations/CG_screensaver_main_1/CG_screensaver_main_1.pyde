r = 0;
def setup():
    size(700,700);
    background(10);
    smooth();
    noStroke();
def draw():
    global r;
    fill(random(10,255),random(10,255),random(10,255));
    rotate(r);
    circle_size = random(5, 15);
    ellipse(100 + r, 10, circle_size, circle_size);
    r = r + 0.2;
    #println(r);
