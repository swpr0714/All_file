from simple_pid import PID
from vpython import *
import matplotlib.pyplot as plt
"""
scene = canvas(width=1920, height=1080,x=0,y=0, center=vec(0,0,0))
floor = box(pos=vec(0,0,0),size=vec(25,0.1,0.1),color=color.red)
center = box(pos=vec(0,0,0),size=vec(0.1,10,0.1),color=color.cyan)
ball = sphere(pos=vec(-10,0,0),radius=0.5,color=color.blue)
"""
v=0
#current_pt=ball.pos.x
current_pt=-10
des_pt = 0
dt=0.001
t=0
acc_range=[-10,10]

pid = PID(0, 10000, 280, setpoint=des_pt, proportional_on_measurement=False, output_limits=acc_range)
#pid = PID(0.1, 0.1, 0.05, setpoint=des_pt, proportional_on_measurement=False, output_limits=acc_range)
pid.sample_time = 0.1
n=0
l_point=[]
l_speed=[]
l_acc=[]
l_componets=[]
l_maxv=[]
l_maxvt=[]
l_0=[]
while n<10:
    rate(5000)
    acc_control = pid(current_pt, dt=pid.sample_time)
    #ball.pos.x+=v*dt
    #current_pt = ball.pos.x
    current_pt+=v*dt
    v += acc_control*dt
    l_point.append(current_pt)
    l_speed.append(v)
    l_acc.append(acc_control)
    l_componets.append(pid.components)
    l_0.append(0)
    t+=dt
    if (v>-0.008 and v<0.008):
        n+=1
        l_maxv.append(current_pt)
        l_maxvt.append(t)
print (t)
print(l_maxv, l_maxvt)
    

def plot_history(data_list, line,plt_title,legends=None):
    plt.title(plt_title)
    plt.plot(data_list)
    plt.plot(line)
    #for i in l_maxv:
    #    plt.plot([i,-10],[i,0])
    if legends :
        plt.legend(legends)
    plt.show()

plot_history(l_point, l_0,"position_point")
# plot_history(l_speed, "speed")
# plot_history(l_acc, "accelerate")
# print(t)
#plot_history(l_speed, "PID_power_list")
#plot_history(l_componets, "PID_components",legends=['proportional','integral','derivative'])