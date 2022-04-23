"""

Simulate a ball on balance an one-demision line.

"""

#___Import___#
from simple_pid import PID
from vpython import *
import matplotlib.pyplot as plt
from math import *

#___Variable_Declaration___#
des_pt = 0
m, g = 0.05, 9.8
a, v = vec(0,0,0), vec(0,0,0)
t, dt = 0, 0.001

theta, theta1, theta2, delta_theta = 0, 0, 0, 0
theta_range=[-pi/18,pi/18]

dist_lst, Zero, pos_E, neg_E = [], [], [], []
E=0.3

#___Vpython_Scene_Setup___#
scene = canvas(width=1920, height=1080,x=0,y=0, center=vec(0,0,0))
floor = box(pos=vec(0,0,0), size=vec(24,0.1,0.1), axis=vec(25*cos(theta),25*sin(theta),0))
ball = sphere(pos=vec(-10,0,0), radius=0.25, color=color.blue)
center = sphere(pos=vec(0,0,0), radius=0.1, color=color.red)

#___PID_Part___#
distance=sqrt(ball.pos.x**2 + ball.pos.y**2)
pid = PID(0, 250, 8, setpoint=des_pt, proportional_on_measurement=False, output_limits=theta_range)
pid.sample_time = 0.1

#___Main_Program___#
sleep(0.5)
while t<30:
    rate(6000)
    #___Calculate_Vector___#
    theta1=atan(abs(floor.axis.y)/abs(floor.axis.x))
    theta = pid(distance, dt=pid.sample_time)
    if(ball.pos.x>0):
        theta1=-theta1
        theta=-theta
    delta_theta=theta+theta1
    #___Rotate_Ball_And_Floor___#
    floor.axis=vec(25*cos(theta),25*sin(theta),0) 
    ball.rotate(angle=delta_theta,axis=vec(0,0,1),origin=vec(0,0,0))
    #___Calculate_Position____#
    a = vec(-g*sin(theta)*cos(theta),-g*sin(theta)*sin(theta),0)
    v += a*dt
    ball.pos+=v*dt
    if (ball.pos.y<ball.pos.x*tan(theta)):
        ball.pos.y=ball.pos.x*tan(theta)
    #___Record_Data___#
    distance=sqrt(ball.pos.x**2 + ball.pos.y**2)
    if(ball.pos.x<0):
        dist_lst.append(-distance)
    else:   
        dist_lst.append(distance)
    Zero.append(0)
    pos_E.append(E)
    neg_E.append(-E)
    t+=dt
    
#___Plot_Graph___#
def plot_history(data_list,Zero,pos_E,neg_E,plt_title,legends=None):
    plt.title(plt_title)
    plt.plot(Zero, c='k')
    plt.plot(pos_E, c='#D4D4D4')
    plt.plot(neg_E, c='#D4D4D4')
    plt.plot(data_list,c='#E60000')
    if legends :
        plt.legend(legends)
    plt.show()
plot_history(dist_lst,Zero,pos_E,neg_E,"position_point")


