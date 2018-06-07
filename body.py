import pygame as p
import os
import random
import tkinter as tk

#duniya parameters
g = 9.8

tool = tk.Tk()
tool.title('Tools')
tool.geometry('400x300')

class Box:
    def __init__(self,x,y,w,h,color,tag=1,t=0,t_state=False):
        self.color = color
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.tag = tag
        self.t_state = t_state
        self.t = t
        
    def alive(self,clk): #dropping event 
        self.clk = clk
        if self.t_state == False:
            if self.y > self.h:
                self.t_state = True
                self.t = self.clk
                #print(self.y,self.h,self.t_state)
                
        else:
            dt = abs(self.t-self.clk) #dt = elasped time
            H = .5*g*dt**2 #falling height
            yy = int(self.y-H)
            if yy>self.h:
                self.y = yy
                #print("dropping...",self.y,H,self.t,self.color,dt)
            else:
                #print("DOOMED\n")
                self.y = self.h
                self.t = 0
                self.t_state = False

    def button(self,btn=None):
        def up():
            self.y = 800
        name = 'Box '+str(id(self))+' up'    
        self.btn = tk.Button(tool,text=name,command=up)
        self.btn.pack()
        
    def properties(self):
        print("BOX TAG 1\n (x,y) = (",self.x,",",self.y,")\n width,height = ",self.w,self.h,"\n color = ",self.color,"\n ",id(self))


                
class Ball:
    def __init__(self,x,y,radi,color,tag=2,t=0,t_state=False):
        self.color = color
        self.x = x
        self.y = y
        self.radi = radi

        self.tag = tag
        self.t_state = t_state
        self.t = t

    def alive(self,clk): #dropping event 
        self.clk = clk
        if self.t_state == False:
            if self.y > self.radi:
                self.t_state = True
                self.t = self.clk
                #print(self.y,self.h,self.t_state)
                
        else:
            dt = abs(self.t-self.clk) #dt = elasped time
            H = .5*g*dt**2 #falling height
            yy = int(self.y-H)
            if yy>self.radi:
                self.y = yy
                #print("dropping...",self.y,H,self.t,self.color,dt)
            else:
                #print("DOOMED\n")
                self.y = self.radi
                self.t = 0
                self.t_state = False

    def button(self,btn=None):
        def up():
            self.y = 800
        name = 'Ball '+str(id(self))+' up'    
        self.btn = tk.Button(tool,text=name,command=up)
        self.btn.pack()
                
    def properties(self):
        print("BALL TAG 2\n (x,y) = (",self.x,",",self.y,")\n radius = ",self.radi,"\n color = ",self.color,"\n ",id(self))

if __name__ == '__main__':
    b  = Box(22,55,22,22,"no")
    b.button()
