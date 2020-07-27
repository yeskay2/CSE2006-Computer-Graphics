x = 0;

def setup():
    size(400, 400,);
    fill(255);
    noStroke();
 
def draw():
    global x;
    translate(200, 200);
    background(255);
    
    fill(255, 0, 0);
    ellipse(x, 0, 20, 20);
  
    fill(0, 255, 0);
    ellipse(x*2, 40, 20, 20);
    fill(0, 0, 255);
    ellipse(x*0.5, 80, 20 ,20);
    x = x + 1;
