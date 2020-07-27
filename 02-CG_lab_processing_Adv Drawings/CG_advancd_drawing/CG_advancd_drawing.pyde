a= 0;
b= 0;
c= 0;
d= 0;
x1 = 0;
x2 = 0;
y1 = 0;
y2 = 0;

gt = 1;
gr = ((1 + sqrt(5)) / 2);

def setup():
  size(1280, 720);
  colorMode(RGB, 255);
  background(0);
  noStroke();
  frameRate(30);
  
  noCursor();


def draw():
    global x1;
    global x2;
    global y1;
    global y2;
    global a;
    global b;
    global c;
    global d;
    global gt;
    global gr;
    w = width/2;
    h = height/2;
  
    #cos1 = cos(millis() / float(5000));
    #sin1 = sin(millis() / float(5000));
  
    #cos1 = cos(millis() / float(3000));
    #sin1 = sin(millis() / float(3000));
  
    cos1 = cos(millis() / float(1000));
    sin1 = sin(millis() / float(1000));
  
    #cos1 = cos(millis() / float(100));
    #sin1 = sin(millis() / float(100));
  
  
    a = a + gt;
    b = b + gt;
    c = c - gt;
    d = d - gt;
  
    x1 = a * cos1;
    y1 = b * sin1;
    x2 = c * cos1;
    y2 = d * sin1; 

    '''
    Power Circle
    '''
    '''
    line(y1 + w, x1 + h, w, h);
    line(x1 + w, y1 + h, w, h);
    line(y2 + w, x2 + h, w, h);
    line(x2 + w, y2 + h, w, h);
    '''
    
    '''
    Point Circle
    '''
    '''
    line(x1 + w, y1 + h, x1 + w, y1 + h);
    line(x2 + w, y2 + h, x2 + w, y2 + h);
    line(y1 + w, x1 + h, y1 + w, x1 + h);
    line(y2 + w, x2 + h, y2 + w, x2 + h);
    '''
    
    '''
    Tulip
    '''
    '''
    line(x1 + w, y1, w, y1 + h);
    line(x2 + w, y2, w, y2 + h);
    line(y1 + w, x1, w, x1 + h);
    line(y2 + w, x2, w, x2 + h);
    '''
    
    '''
    Four element
    '''
    '''
    line(x1 + w, y2 + h, y2 + w, x2 + h); //quartetA
    line(x2 + w, y1 + h, y2 + w, x2 + h);
    line(-x1 + w, -y2 + h, -y2 + w, -x2 + h);
    line(-x2 + w, -y1 + h, -y2 + w, -x2 + h);
    '''
    '''
    line(y1 + w, x2 + h, x2 + w, y2 + h); //quartetB
    line(y2 + w, x1 + h, x2 + w, y2 + h);
    line(-y1 + w, -x2 + h, -x2 + w, -y2 + h);
    line(-y2 + w, -x1 + h, -x2 + w, -y2 + h);
    '''
    
    '''
    Tangle
    '''
    '''
    line(y1 + w, y1 + h, y2 + w, x2 + h);
    line(x1 + w, x1 + h, x2 + w, y2 + h);
    line(x1 + w, y2 + h, y2 + w, y1 + h);
    #line(-y1 + w, -y1 + h, -y2 + w, -x2 + h); //+
    #line(x1 + x2 + y1 + w, y1 + y2 + x1 + h, w, h); //++
    #line(x1 + y1 + y2 + w, y1 + y2 + x2 + h, x2 + w, y2 + h); //+++
    '''
    
    '''
    Data Circle
    '''
    '''
    line(y1 + w, y2 + h, x1 + w, y2 + h);
    line(x1 + w, x2 + h, y1 + w, x2 + h);
    line(y2 + w, y1 + h, x2 + w, y1 + h);
    line(x2 + w, x1 + h, y2 + w, x1 + h);
    '''
    
    '''
    Process of rage
    '''
    '''
    line(x2 + w, x2 + h, y2 + w, y1 + h);
    line(x2 + w, x2 + h, y1 + w, y2 + h);
    line(x1 + w, x1 + h, y1 + w, y2 + h);
    line(x1 + w, x1 + h, y2 + w, y1 + h);
    '''
    
    '''
    Spiral of rage
    '''
    #line(-x2 + w, -x2 + h, -y2 + w, -y1 + h);
    
    '''
    Mount Tsukuba
    '''
    #line(x2 + x1 + w, x2 + y1 + h, y2 + w, y1 + h);
    #line(x2 + y1 + w, y2 + x1 + h, x2 + w, y2 + y1 + h);
    
    '''
    Tube riding
    '''
    line(x2 + y1 + w, y2 + x1 + h, x2 + w, y1 + h);
    
    stroke(255);
    #saveFrame("frames/####.tga");
