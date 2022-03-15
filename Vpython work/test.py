from simple_pid import PID
import time

pid = PID(1,0.1,0.05,setpoint=1)
e=1
while e>0:
    print(pid(e))
    # print(e)
    e-=0.01
