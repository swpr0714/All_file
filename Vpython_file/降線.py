from vpython import *
R1=1; R2=2; R3=3; R4=4; R5=5; L=30
scene = canvas(width=2800, height=1800, x=0, y=0,color=color.white)
floor = box (size=vec(2*L,0.2,1),pos=vec(0,-0.1,0),color=color.black)
back = box (size=vec(200,200,1),pos=vec(0,0,-20),color=color.white)

a = cylinder(radius=R1,pos=vec(-L+R5,R1,0),axis=vec(0,0,1))
ball1 = sphere (radius=0.01,pos=vec(a.pos.x,0.01,1),color=color.red,make_trail=True)

b = cylinder(radius=R2,pos=vec(-L+R5,R2,0),axis=vec(0,0,1))
ball2 = sphere (radius=0.01,pos=vec(b.pos.x,0.01,1),color=color.yellow,make_trail=True)

c = cylinder(radius=R3,pos=vec(-L+R5,R3,0),axis=vec(0,0,1))
ball3 = sphere (radius=0.01,pos=vec(c.pos.x,0.01,1),color=color.green,make_trail=True)

d = cylinder(radius=R4,pos=vec(-L+R5,R4,0),axis=vec(0,0,1))
ball4 = sphere (radius=0.01,pos=vec(d.pos.x,0.01,1),color=color.cyan,make_trail=True)

e = cylinder(radius=R5,pos=vec(-L+R5,R5,0),axis=vec(0,0,1))
ball5 = sphere (radius=0.01,pos=vec(e.pos.x,0.01,1),color=color.magenta,make_trail=True)

graph_y_t = graph(title="y-t plot", width=1400, height=900, x=0, y=400, xtitle="t(s)", ytitle="y(m)",color=color.black)
curve_1 = gcurve(graph=graph_y_t,color=ball1.color)
curve_2 = gcurve(graph=graph_y_t,color=ball2.color)
curve_3 = gcurve(graph=graph_y_t,color=ball3.color)
curve_4 = gcurve(graph=graph_y_t,color=ball4.color)
curve_5 = gcurve(graph=graph_y_t,color=ball5.color)

dt=0.001
t=0
while(a.pos.x<L-R1):
    rate(1000)
    a.rotate(angle=pi/720,axis=vec(0,0,1),origin=a.pos)
    ball1.rotate(angle=pi/720,axis=vec(0,0,1),origin=a.pos)
    a.pos.x+=2*1*pi/720
    ball1.pos.x+=2*1*pi/720
    curve_1.plot(pos=(t,ball1.pos.y))
    t+=dt
t=0
while(b.pos.x<L-R2):
    rate(1000)
    b.rotate(angle=pi/720,axis=vec(0,0,1),origin=b.pos)
    ball2.rotate(angle=pi/720,axis=vec(0,0,1),origin=b.pos)
    b.pos.x+=2*1*pi/720
    ball2.pos.x+=2*1*pi/720
    curve_2.plot(pos=(t,ball2.pos.y))
    t+=dt
t=0
while(c.pos.x<L-R3):
    rate(1000)
    c.rotate(angle=pi/720,axis=vec(0,0,1),origin=c.pos)
    ball3.rotate(angle=pi/720,axis=vec(0,0,1),origin=c.pos)
    c.pos.x+=2*1*pi/720
    ball3.pos.x+=2*1*pi/720
    curve_3.plot(pos=(t,ball3.pos.y))
    t+=dt
t=0
while(d.pos.x<L-R3):
    rate(1000)
    d.rotate(angle=pi/720,axis=vec(0,0,1),origin=d.pos)
    ball4.rotate(angle=pi/720,axis=vec(0,0,1),origin=d.pos)
    d.pos.x+=2*1*pi/720
    ball4.pos.x+=2*1*pi/720
    curve_4.plot(pos=(t,ball4.pos.y))
    t+=dt
t=0
while(e.pos.x<L-R3):
    rate(1000)
    e.rotate(angle=pi/720,axis=vec(0,0,1),origin=e.pos)
    ball5.rotate(angle=pi/720,axis=vec(0,0,1),origin=e.pos)
    e.pos.x+=2*1*pi/720
    ball5.pos.x+=2*1*pi/720   
    curve_5.plot(pos=(t,ball5.pos.y))
    t+=dt
