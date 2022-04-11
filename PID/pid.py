# define sim state
from simple_pid import PID
import matplotlib.pyplot as plt
#import random
#import numpy as np
des_point = 100
current_point = 0

#current_speed = 0
power_range = [-10, 10]

pid = PID(0.1, 0.1, 0.05, setpoint=des_point, proportional_on_measurement=False,
          output_limits=power_range
          )
pid.sample_time = 0.1

l_point = []
l_power = []
l_componets = []
for _ in range(200):
    # err = des_point - current_point
    power_control = pid(current_point, dt=pid.sample_time)
    # 电压低于一定值不能运转
#     power_control = 0 if abs(power_control) < 2 else power_control
    current_point += power_control

    l_point.append(current_point)
    l_power.append(power_control)
    l_componets.append(pid.components)


def plot_history(data_list, plt_title,legends=None):
    plt.title(plt_title)
    plt.plot(data_list)
    if legends :
        plt.legend(legends)
    plt.show()


plot_history(l_point, "car_position_point")
plot_history(l_power, "PID_power_list")
plot_history(l_componets, "PID_components",legends=['proportional','integral','derivative'])
