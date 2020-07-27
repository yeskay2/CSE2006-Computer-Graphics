time =0;

def setup():
    size(1024,768);



def draw ():
    global time;
    time=time+0.1;
    strokeWeight(1);
    translate(width/2,height/2);
 
  
    
    ellipse(0,0,200,200);
    for i in range(12):
        pushMatrix();
        rotate(2*i*PI/12);
        line(80,0,100,0);
        popMatrix();

   
    
    beginShape(); 
    strokeWeight(4);
    rotate(time/12);
    line(0,0,55,0);
    triangle(55,-2,55,2,60,0);
    endShape();
  
  
    beginShape();
    strokeWeight(2);
    rotate(time);
    line (0,0,0,-70);
    triangle(-2,-70,2,-70,0,-77);
    endShape();
