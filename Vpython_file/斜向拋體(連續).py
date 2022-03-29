from vpython import *
import time

speed_0=vec(3,8,0)
vx=speed_0.x
vy=speed_0.y
g=-9.8
t=0
dt=0.001
scene = canvas(width=1920, height=1080, x=0, y=0)
floor = box(pos=vec(0,-0.1,0),size=vec(20,0.2,3),color=color.red)
ball = sphere(pos=vec(-8,0.1,0),radius=0.1,color=color.blue,make_trail=True)
while(True):
    rate(1000)
    ball.pos.x+=vx*dt
    ball.pos.y+=vy*dt
    vy+=g*dt
    t+=dt
    if (ball.pos.y<=0.1):
        vy=(-vy)*0.8