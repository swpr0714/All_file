from vpython import *
scene = canvas(title="Rutherford Scattering", width=800, height=600, x=0, y=0,
               center=vec(0, 0, 0), background=color.black)
# 產生原子核
alpha = sphere(pos=vec(-0.5*L + r1, b, 0), radius=r1, m=m1, q=q1, v=v0, color=c1, make_trail=True)