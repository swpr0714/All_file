"""
Import Module
"""
from vpython import *
"""
Var Setup
"""
L = 20                                  # Length of Water
m, r = 1, 1                             # Mess of stone, Radius of stone
theta=pi/45                             # Angle of V0
V=12                                    # Magnitude of V0
v0=vec(V*cos(theta),V*sin(theta),0)     # Vector of V0 
dt=0.001                                # dt
rho, g = 1, -9.8                         
ya, yb = 1, 1                           # Variable to determine if a stone falls into the water
"""
Scene Setup
"""
canva = canvas(width=2000,height=1200,z=0,y=0,center=vec(0,0,0),forward=vec(0,-1,-5))
water = box(size=vec(2*L,5,5),pos=vec(0,-2.5,0),color=color.blue)
land = box(size=vec(5,6,5),pos=vec(-L-2.5,-2,0),color=color.green)
stone = cylinder(radius=r,axis=vec(0,0.5,0),pos=vec(-L,1,0),color=vec(0.5,0.5,0.5),make_trail=True)
stone.rotate(angle=theta,axis=vec(0,0,1),origin=vec(stone.pos))
point = sphere(radius=0.3,pos=land.pos-vec(0,1,0),color=color.red)      # Points to mark where the stone contact the water
"""
Sub
"""
def get_B (rho,r,h):        # A sub function to calculate Buoyancy
    B = rho*r*r*pi*h
    return B
"""
Main
"""
sleep(2)
while (stone.pos.y>-5):
    rate(1000)
    ya=stone.pos.y
    v0.y+=g*dt
    stone.pos+=v0*dt
    yb=stone.pos.y
    if (stone.pos.y<0):
        h = stone.pos.y
        if (stone.pos.y>0.5):
            h=0.5
        B = get_B(rho,r,-h) 
    if (stone.pos.y<0 and ya*yb<0 and v0.x>5):
        v0.x*=0.8
        v0.y*=-0.8
        a=point.clone(pos=stone.pos)
    elif (stone.pos.y<0 and ya*yb<0):
        a=point.clone(pos=stone.pos)
stone.rotate(angle=-theta,axis=vec(0,0,1),origin=vec(stone.pos))
    