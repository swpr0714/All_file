from vpython import *
import time
"""
"""
 #1. 參數設定, 設定變數及初始值

r = 0.1      # 球的半徑
L = 5        # 地板邊長
thick = 0.1  # 地板厚度
v = 0.03     # 木塊速度
t = 0        # 時間
dt = 0.01    # 時間間隔
a=0
rad = 0

scene = canvas(title="1D Motion", width=800, height=600, x=0, y=0, center=vec(0, 0.1, 0), background=vec(0,0.6,0.6))

floor = box(pos=vec(0, 0, 0), size=vec(L,thick,L), color=color.blue)
ball = sphere(pos=vec(L/2-r,r+0.5*thick,L/2-r), radius = r, color = color.red)
 