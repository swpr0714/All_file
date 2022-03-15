from vpython import *
v=0.03
t=0
dt=0.01
start_pt=0
scene = canvas(width=1920, height=1080, center=vec(0,0,0),x=0, y=0)
floor = box(pos=vec(0,0,0),size=vec(1,0.02,1),color=color.red)
cube = box(pos=vec(start_pt,0.02,0.45),size=vec(0.02,0.02,0.02),color=color.cyan,v=vec(v,0,0))
while cube.pos.x<=start_pt+0.3:
    rate(100)
    cube.pos.x+=v*dt
    t+=dt
    print(t)
