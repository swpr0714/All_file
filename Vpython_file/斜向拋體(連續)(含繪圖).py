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

graph_x_t = graph(title="x-t plot", width=400, height=300, x=0, y=400, xtitle="t(s)", ytitle="x(m)")
graph_y_t = graph(title="y-t plot", width=400, height=300, x=0, y=400, xtitle="t(s)", ytitle="y(m)")
graph_vy_t = graph(title="vy-t plot", width=400, height=300, x=0, y=400, xtitle="t(s)", ytitle="vy(m/s)")
graph_ay_t = graph(title="ay-t plot", width=400, height=300, x=0, y=400, xtitle="t(s)", ytitle="ay(m/s<sup>2<sup>)")
curve_x_t = gcurve(graph=graph_x_t,color=color.red)
curve_y_t = gcurve(graph=graph_y_t,color=color.blue)
curve_vy_t = gcurve(graph=graph_vy_t,color=color.green)
curve_ay_t = gcurve(graph=graph_ay_t,color=color.cyan)
while(True):
    rate(1000)
    ball.pos.x+=vx*dt
    ball.pos.y+=vy*dt
    vy+=g*dt
    t+=dt
    if (ball.pos.y<=0.1):
        vy=(-vy)*0.8
    curve_x_t.plot(pos=(t,ball.pos.x))
    curve_y_t.plot(pos=(t,ball.pos.y))
    curve_vy_t.plot(pos=(t,vy))
    curve_ay_t.plot(pos=(t,g))
