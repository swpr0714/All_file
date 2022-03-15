from vpython import *
v=0.2
dt=0.001
scene = canvas(width=1920, height=1080, x=0, y=0, center=vec(0,0.06,0))
floor = box(pos=vec(0,-0.05,0),size=vec(1,0.1,1),color=color.cyan)
wall_left = box(pos=vec(-0.5,0,0),size=vec(0.1,1,1),color=color.cyan)
wall_right = box(pos=vec(0.5,0,0),size=vec(0.1,1,1),color=color.cyan)
cube = box(pos=vec(-0.4,0.05,0), size=vec(0.1,0.1,0.1),color=color.red,v=vec(v,0,0))
while True:
    rate(1000)
    cube.pos.x += v*dt
    if cube.pos.x >=0.4:
        v=-v
    if cube.pos.x <=-0.4:
        v=-v    