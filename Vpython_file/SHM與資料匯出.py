from vpython import *
import csv
import numpy as np
import math

scene = canvas(width=1920, height=1080, x=0, y=0)
floor = box(pos=vec(0,-0.1,0),size=vec(12,0.2,3),color=color.red)
wall = box(pos=vec(-5.9,1,0),size=vec(0.2,2,3),color=color.red)
ball = sphere(pos=vec(0.4,0.5,0),radius=0.5,color=color.blue,make_trail=False)
spring = helix(pos=vec(-5.9,0.5,0),radius=0.3,coils=12,thickness=0.03,color=color.white)

t=0 #s
k=10 #N/x
m=0.5 #kg
dt=0.001 #s
vx=-3 #x/s
n=0
t_list=[]
T=["T1","T2","T3","T4","T5"]
avg_t=[]

with open("t_x_v.csv",'w',newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["時間","位置","速度"])
    while(n<10):
        rate(1000)
        a = -(k/m)*ball.pos.x
        vx += a*dt
        ball.pos.x += vx*dt
        t=t+dt
        spring.length=ball.pos.x+6-ball.radius
        if (vx<0.005 and vx>-0.005):
            t_list.append(t)
            n+=1
        writer.writerow([t,ball.pos.x,vx])
    #print("有",len(t_list),"筆資料")
    for i in range(2,6,1):
        #print(T[i-2],t_list[i]-t_list[i-2])
        avg_t.append(t_list[i]-t_list[i-2])
    print("一次震盪週期 T=",np.average(avg_t),"(這是前五次的平均值)")
    print("由公式計算得 T=",2*math.pi*math.sqrt(m/k)) 
    print("嗯對 平均值與理論值接近 兩者相等")
    