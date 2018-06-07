import pygame as p
import os
import random
import tkinter as tk
from body import *

#basic environment parameters
WIDTH = 800; HEIGHT = 1000
c_x = int(WIDTH/2) #centerX
c_y = int(HEIGHT/2)+300 #centerY

os.environ['SDL_VIDEO_CENTERED'] = '1'

##colors
white = (255,255,255);black = (0,0,0);red = (255,0,40);
light = (250, 245, 252)
paste = (180, 233, 252)
ash = (105,109,126)
violate = (137, 13, 175)
#__tkinter tools ops
def test():
    print('test')
##set origin at surface center
def X(x): 
    global width
    return int((c_x+x))
def Y(y):
    global height
    return int((c_y-y))

#create visible axis
def axis():
    p.draw.line(duniya,ash,[X(-c_x),Y(0)],[X(c_x),Y(0)],2) #x-axis
    #p.draw.line(duniya,ash,[X(0),Y(c_y)],[X(0),Y(-c_y)],1) #y-axis

#__ENVIRONMENT
duniya = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption("Duniya Simulation")
clock = p.time.Clock()
#__EMBEDED TKINTER


'''btn1 = tk.Button(root,text="test",command=test)
btn1.pack()'''

def draw_environment(item_list):
    duniya.fill(light)
    #print(item_list)
    clk = p.time.get_ticks()/1000
    
    #create body on the screen according to tag
    for item in item_list:
        if item.tag==1:
            p.draw.rect(duniya,item.color,(X(item.x),Y(item.y),item.w,item.h),6)
            item.alive(clk)
        elif item.tag==2:
            p.draw.circle(duniya,item.color,[X(item.x),Y(item.y)],item.radi,2)
            item.alive(clk)
            
    axis()
    p.display.update()
    
    
def mainLoop():
    #items
    r = random.randrange(0,255)
    g = random.randrange(0,255)
    b = random.randrange(0,255)
    
    red_box = Box(40,c_y,50,50,red); red_box.button()
    paste_box = Box(-180,300,50,50,paste); paste_box.button()
    ash_box = Box(-80,350,50,50,ash); ash_box.button()
    violate_box = Box(300,c_y,50,50,ash); violate_box.button()
    life_box = Box(200,c_y+50,60,60,(r,g,b)); life_box.button()

    life_ball = Ball(0,c_y,50,(r,g,b)); life_ball.button()

    #main_loop
    while  True:
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
        #pass items
        draw_environment([red_box,paste_box,ash_box,violate_box,life_box,life_ball])
       
        clock.tick()
        tool.update()
    
if __name__=='__main__':
    mainLoop()
    
