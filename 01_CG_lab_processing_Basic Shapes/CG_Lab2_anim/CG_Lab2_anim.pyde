def setup():
    size(800, 600);
    frameRate(450);
    background(0);
    noStroke();
def draw_ellipse():
    x = random(0, width); #lower limit and upper limit
    y = random(0, height);
    dist1 = dist(x, y, width / 2, height / 2);
    diameter = 30 - dist1 / 10.0;
    if diameter > 0:
        fill(63, 127, 255, 70);
        ellipse(x, y, diameter, diameter);

def draw():
    draw_ellipse();
    # NUM = 10000;
    # diameter = 5;
    # for i in range (NUM):
    #     x = random(0, width);
    #     y = random(0, height);
    #     dist1 = dist(x, y, width / 2, height / 2);
    #     if dist < height / 4 :
    #         fill(63, 127, 255);
    #     elif dist < height / 2 :
    #         fill(17, 184, 255);
    #     else:
    #         fill(124, 212, 255);
    #     ellipse(x, y, diameter, diameter);
        
        
    
