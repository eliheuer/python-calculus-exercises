# from drawBot import * # uncomment if using DrawBot as a module
import math

# static variables
pg = 512

num_frames = 100
origin = (pg/4, pg/4)
center = pg/2

# gird variables
origin = (128, 128)
width = 256
height = 256
center = width/2
num_x_units = 8
num_y_units = 8

# dot variables
dot_size = 16  
amp = 128 # short for amplitude
amp_inner = amp - pg/8
step = 0 # step in the animation
flag = False

class Point(object):
    '''Creates a point on a with x and y values.'''
    
    def __init__(self, x, y):
        '''Defines x and y variables'''
        self.x = x
        self.y = y

    def move(self, dx, dy):
        '''Determines where x and y move'''
        self.x = self.x + dx
        self.y = self.y + dy

    def __str__(self):
        return "Point(%s,%s)"%(self.x, self.y) 


    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx**2 + dy**2)
    
    def draw(self, r, g, b):
        print("draw")
        fill(r, g, b)
        stroke(None)
        oval(((int(self.x) - 8) + center), ((int(self.y) - 8) + center), 16, 16)

# Draws a new frame in the animation
def new_page(): 
    newPage(pg, pg)
    frameDuration(1/24)
    fill(0.1, 0.1, 0.1)
    rect(0, 0, pg, pg)
    
# draw each frame as a new page
for frame in range(num_frames):
    new_page()
    translate(128, 128+64)
    
    # Static Lines
    fill(0.3, 0.3, 0.3) 
    oval(center-pg/4, center-pg/4, amp*2, amp*2)
    fill(0.1,0.1,0.1) 
    oval(center-amp_inner, center-amp_inner, amp_inner*2, amp_inner*2)
    
    outer_x_pos = math.cos(step - (math.pi*(1/6))) * amp
    outer_y_pos = math.sin(step - (math.pi*(1/6))) * amp
    inner_x_pos = math.cos((math.pi*(6/4))+step) * amp_inner
    inner_y_pos = math.sin((math.pi*(6/4))+step) * amp_inner
    
    #lines(width, height, (x_pos)-dot_size/2, (y_pos)-dot_size/2)
    strokeWidth(3)
    outer_point = Point(outer_x_pos, outer_y_pos)
    inner_point = Point(inner_x_pos, inner_y_pos)
    centr_point = Point(0, 0)
    
    strokeWidth(6)   
    stroke(0.1,0.3,0.9)
    line((inner_point.x+center, inner_point.y+center),
         (outer_point.x+center, outer_point.y+center))
    stroke(0.9,0.9,0.2)
    line((inner_point.x+center, inner_point.y+center), (center, center))
    stroke(0.9,0.2,0.1)
    line((center, center), (outer_point.x+center, outer_point.y+center))    
    
    outer_point.draw(0.9, 0.2 , 0.1)
    inner_point.draw(0.1, 0.2 ,0.9)
    centr_point.draw(0.9, 0.9, 0.2)
    
    y_line = 0.5
    y_string = "{:.10f}".format(y_line)
    
    r_line = 1
    r_string = "{:.10f}".format(r_line)
    
    b_line = math.sqrt(1 - 0.25)
    b_string = "{:.10f}".format(b_line)
    
    # type 
    fontSize(34)
    font("Helvetica Neue Bold")
   
    fill(0.9,0.9,0.2)
    text("A: ", (0, center-(256-64)))
    text(y_string, (40, center-(256-64)))
    
    fill(0.1,0.2,0.9)
    text("B: ", (-1, center-(256-32)))
    text(b_string, (40, center-(256-32)))
    
    fill(0.9,0.2,0.1)
    text("C: ", (-2, center-256))
    text(r_string, (40, center-256))
            
    print("step=", step)
    step += 0.02 * math.pi
    
saveImage("mamikons-proof.gif")