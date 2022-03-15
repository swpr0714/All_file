from test import PID
pid = PID(1,0.1,0.05,setpoint=1)


a=1
b=2
c=3
print (pid(b))
print (pid(c))
