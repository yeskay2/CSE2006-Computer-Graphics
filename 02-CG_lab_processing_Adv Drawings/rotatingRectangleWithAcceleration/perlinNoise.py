speed = 0
position = [0,0]
linearVelocity = [0,0]
linearAcceleration = [0,1]


def setup():
    size(640,640)
    background(255)


def draw():
    global position, linearVelocity, linearAcceleration
    ellipse(position[0],position[1],100,100)
    position[0] = position[0] + linearVelocity[0]
    position[1] = position[1] + linearVelocity[1]
    linearVelocity[0] = linearVelocity[0] + linearAcceleration[0]
    linearVelocity[1] = linearVelocity[1] + linearAcceleration[1]
