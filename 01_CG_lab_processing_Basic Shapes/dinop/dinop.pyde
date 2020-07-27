import random
x = 50
y = 185
grav = 1.5
class obstacle:
    def __init__(self , x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    
    def draw_ob(self): 
        fill(60)   
        rect(self.x, self.y, self.w, self.h)
    
    def move(self):
        self.x -= 1
        if self.x <= 0 :
            self.x=780
    
    def collision(self, x, y):
        if(((y+15)-self.y)>=0 and ((x+15)-self.x)>=0):
            return True
        else:
            return False
        
    
def setup():
    global obs
    size(800, 300)
    obs = []
    x_val = 780
    y_val = 180
    ht = 20
    wdt = 20
    for i in range(4):
        ob = obstacle(x_val, y_val, wdt, ht)
        x_val += random.randrange(150, 250)
        ht = random.randrange(20, 50)
        y_val = 200 - ht
        wdt = random.randrange(20, 50)
        
        obs.append(ob)
        
def draw():
    background(255)
    frameRate(120)
    global x, y
    fill(51)
    rect(0, 200, 800, 300)
    
    fill(255)
    ellipse(x, y, 30, 30)
    
    if(y<185):
        y += grav
    
    for ob in obs:
        ob.draw_ob()
        ob.move()
    
        flag = ob.collision(x, y)    
        
        if flag:
            break
    if flag:
        noLoop()
        background(0)
        textSize(32);
        fill(200);
        text("GAME OVER", 302, 152, -30)
        fill(255) 
        text("GAME OVER", 300, 150)
        redraw()
            
    
def keyPressed():
    global y  
    if key == CODED:
        if keyCode == UP:
            y -= 100
    if y<=15:
        y=15
