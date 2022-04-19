while (stone.pos.y>-5):
    rate(1000)
    ya=stone.pos.y
    v0.y+=g*dt
    stone.pos+=v0*dt
    yb=stone.pos.y
    
    if (stone.pos.y<0):
        print(v0.x)
        h = stone.pos.y
        if (stone.pos.y>0.5):
            h=0.5
        B = get_B(rho,r,-h)

    
    if (stone.pos.y<0 and ya*yb<0 and v0.x>5):
        v0.x*=0.8
        v0.y*=-0.8

    scene.center=stone.pos
    # if (v0.y<0.5):
    #     v0=vec(0,0,0)
stone.rotate(angle=-theta,axis=vec(0,0,1),origin=vec(stone.pos))
    