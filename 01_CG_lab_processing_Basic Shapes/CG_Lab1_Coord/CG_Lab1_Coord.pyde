def setup():
    #global leftViewport, rightViewport;
    size(800, 600,  P3D);
    print("Monitor display resolution is ");
    
    print("Width is ",displayWidth);
    print("Height is ",displayHeight);
    print ("Width of the current canvas",width);
    print ("Width of the current canvas",height);
    
def draw():    
    print(mouseX,mouseY);
    print("Width is ",displayWidth);
    print("Height is ",displayHeight);
    print("Cartesian coord: Width is ",width/2);
    print("Cartesian coord:Height is ",height/2);
    #ellipse(width/2,height/2,100,100);
    #point(width/2,height/2)
    #line(width/2,height/2,95, 271)
    #rect(width/2,height/2,200,200)
    
    # print ("Width of the current canvas",width);
    # print ("Width of the current canvas",height);
