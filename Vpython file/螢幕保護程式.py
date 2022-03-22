from vpython import *
import random
import time
#color = [color.red, color.green, color.blue,color.cyan, color.magenta, color.yellow,color.white]
r,g,b=1,1,1
vx1=random.uniform(-0.25,0.25)
vz1=random.uniform(-0.25,0.25)
vx2=random.uniform(-0.25,0.25)
vz2=random.uniform(-0.25,0.25)

cl=vec(1,1,1)
dt=0.001
scene= canvas(width=1920, height=1080, x=0, y=0, center=vec(0,0,0))
floor = box(pos=vec(0,-0.45,0),size=vec(1,0.1,1),color=color.white)
wall_left = box(pos=vec(-0.5,0,0),size=vec(0.1,1,1),color=color.white)
wall_right = box(pos=vec(0.5,0,0),size=vec(0.1,1,1),color=color.white)
wall_up = box(pos=vec(0,0,0.5),size=vec(1,1,0.1),color=color.white)
wall_down = box(pos=vec(0,0,-0.5),size=vec(1,1,0.1),color=color.white)
cube = box(pos=vec(0.3,0.45,0.3),size=vec(0.1,0.1,0.1),color=color.blue,v=vec(vx1,0,vz1))
cube1 = box(pos=vec(-0.3,0.35,-0.3),size=vec(0.1,0.1,0.1),color=color.red,v=vec(vx2,0,vz2))
while True:
    rate(20000)
    cube.pos.x += vx1*dt
    cube.pos.z += vz1*dt
    cube1.pos.x += vx2*dt
    cube1.pos.z += vz2*dt
    if cube.pos.x >= 0.4:
        vx1=-vx1
        cube.color = vec(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))
    if cube.pos.z >= 0.4:
        vz1=-vz1
        cube.color = vec(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))
    if cube.pos.x <= -0.4:
        vx1=-vx1
        cube.color = vec(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))
    if cube.pos.z <= -0.4:
        vz1=-vz1
        cube.color = vec(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))
        
        
        
    if cube1.pos.x >= 0.4:
        vx2=-vx2
        cube1.color = vec(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))
    if cube1.pos.z >= 0.4:
        vz2=-vz2
        cube1.color = vec(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))
    if cube1.pos.x <= -0.4:
        vx2=-vx2
        cube1.color = vec(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))
    if cube1.pos.z <= -0.4:
        vz2=-vz2
        cube1.color = vec(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))


# while True:
#     r,g,b=random.uniform(0,1),random.uniform(0,1),random.uniform(0,1)
#     cl=vec(r,g,b)
#     cube.color=cl
#     print(r,g,b)