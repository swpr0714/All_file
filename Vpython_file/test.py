from vpython import *
scene = canvas(width=2400, height=1600,x=0,y=0)
arrx=arrow(pos=vec(0,0,0),axis=vec(8,0,0),shaftwidth=0.05,color=vec(1,1,0))
arrY=arrow(pos=vec(0,0,0),axis=vec(0,8,0),shaftwidth=0.05,color=vec(0,0,1))
arrZ=arrow(pos=vec(0,0,0),axis=vec(0,0,8),shaftwidth=0.05,color=vec(1,1,1))

N=250; L1=5; L2=25; d=2; R=0.1
balls = [sphere(pos=vec(-2,0,0), radius=R, color=color.red) for i in range(N)]
plate1=box(pos=vec(L1/2.,-d,0),size=vec(L1,0.1,L1), color=color.blue, opacity=0.3)
plate2=box(pos=vec(L1/2.,d,0),size=vec(L1,0.1,L1), color=color.blue, opacity=0.3)
plate3=box(pos=vec(L1*1.5+L1/2.,0,-d),size=vec(L1,L1,0.1), color=color.green, opacity=0.3)
plate4=box(pos=vec(L1*1.5+L1/2.,0,d),size=vec(L1,L1,0.1), color=color.green, opacity=0.3)
plate5=box(pos=vec(L2,0,0),size=vec(0.1,20,20), color=color.cyan)
gun=cylinder(radius=0.6,pos=vec(-2,0,0),axis=vec(2,0,0))

vx=4.
ay0=0.8
az0=6.0
vy=[0. for i in range(N)]
ay=[0. for i in range(N)]
vz=[0. for i in range(N)]
az=[0. for i in range(N)]
T=4.
t,dt=0.,0.01; NR=int(1./dt)
while t < 100.:
    rate(NR)
    for i in range(N):
        if(t < 0.05*i):  continue
        
        if(balls[i].pos.x > 0.) and (balls[i].pos.x < 10.): ay[i]=ay0*sin(0.2*(t-0.5)+pi/2.)
        else:   ay[i]=0.
        if(balls[i].pos.x > 25-R):   continue
        vy[i] += ay[i]*dt
        balls[i].pos.y += vy[i]*dt
        
        if(balls[i].pos.x > 1.5*L1) and (balls[i].pos.x < 2.5*L1): az[i]=az0*sin(4.*t)
        else:   az[i]=0.
        if(balls[i].pos.x > 25.):   continue
        vz[i] += az[i]*dt
        balls[i].pos.z += vz[i]*dt
        
        balls[i].pos.x += vx*dt
    t += dt