from simple_pid import PID
from vpython import *
import matplotlib.pyplot as plt
from math import *


m=0.05
g=9.8
theta=0
a = vec(0,0,0)
v = vec(0,0,0)
des_pt = 0
dt=0.001
t=0

scene = canvas(width=1920, height=1080,x=0,y=0, center=vec(0,0,0))
floor = box(pos=vec(0,0,0),size=vec(24,0.1,0.1),axis=vec(25*cos(theta),25*sin(theta),0),color=color.red)
center = sphere(pos=vec(0,0,0),radius=0.1,color=color.cyan)
box = box(pos=vec(-10,0,0),size=vec(0.5,0.5,0.5),color=color.blue)
graph_d_t = graph(title="d-t plot", width=400, height=300, x=0, y=400, xtitle="t(s)", ytitle="x(m)")
d_t = gcurve(graph=graph_d_t,color=color.red)
graph_theta_t = graph(title="theta-t plot", width=400, height=300, x=0, y=400, xtitle="t(s)", ytitle="theta(degree)")
theta_t = gcurve(graph=graph_theta_t,color=color.red)


distance=sqrt(box.pos.x**2 + box.pos.y**2)

theta_range=[-pi/18,pi/18]

theta1=0
theta2=0
d_theta=0

pid = PID(0.005, 100, 5, setpoint=des_pt, proportional_on_measurement=False, output_limits=theta_range)
pid.sample_time = 0.1
sleep(0.5)

dist_lst=[]
line=[]
while t<30:
    rate(2000)
    ##計算
    theta1=atan(abs(floor.axis.y)/abs(floor.axis.x))
    theta = pid(distance, dt=pid.sample_time)
    if(box.pos.x>0):
        theta1=-theta1
        theta=-theta
    d_theta=theta+theta1
    ##旋轉
    floor.axis=vec(25*cos(theta),25*sin(theta),0) 
    box.rotate(angle=d_theta,axis=vec(0,0,1),origin=vec(0,0,0))
    ##運動
    a = vec(-g*sin(theta)*cos(theta),-g*sin(theta)*sin(theta),0)
    v += a*dt
    box.pos+=v*dt
    ##限位
    if (box.pos.y<box.pos.x*tan(theta)):
        box.pos.y=box.pos.x*tan(theta)
    ##紀錄
    distance=sqrt(box.pos.x**2 + box.pos.y**2)
    if(box.pos.x<0):
        dist_lst.append(-distance)
        line.append(0)
    else:   
        dist_lst.append(distance)
        line.append(0)
    t+=dt
    d_t.plot(pos=(t,distance))
    theta_t.plot(pos=(t,theta/pi*180))
    

def plot_history(data_list,line,plt_title,legends=None):
    plt.title(plt_title)
    plt.plot(data_list)
    plt.plot(line)
    if legends :
        plt.legend(legends)
    plt.show()

plot_history(dist_lst,line,"position_point")


