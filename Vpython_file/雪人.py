from vpython import *
scene = canvas(width=1920, height=1080, center=vec(0,0,0),x=0,y=0)



head = sphere(pos = vec(0,1,0), radius = 1, color = vec(1,1,1))
body = sphere(pos = vec(0,-0.8,0), radius = 1.3, color = vec (1,1,1))
r_eye = sphere(pos = vec (0.4,1.1,1), radius = 0.05, color = vec (0,0,0))
l_eye = sphere(pos = vec (-0.4,1.1,1), radius = 0.05, color = vec (0,0,0))
scarf = ring(pos = vec(0,0.3,0), axis = vec(0,1,0), radius=0.8, thickness=0.1, color = color.red)
nose = cone(pos=vec(0,0.9,0.5), axis = vec(0,0,0.8), radius = 0.2, color = color.orange)
r_hand = cylinder(pos=vec(0.4,-0.4,0),axis=vec(1.6,0.4,0),radius=0.1)
l_hand = cylinder(pos=vec(-0.4,-0.4,0),axis=vec(-1.6,0.4,0),radius=0.1)


hat_body = cone(pos=vec(2,0,0), axis=vec(0,1,0), radius=0.5, color=color.blue)
ball = sphere(pos=vec(2,1,0), radius=0.15)

hat = compound([hat_body,ball])
hat.pos=vec(0.2,2.2,0)
hat.axis=vec(1,-0.2,0)
