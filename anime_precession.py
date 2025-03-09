from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib.animation import FuncAnimation
import numpy as np

import timeit
t0 = timeit.time.time()


colorset=['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple']   
colorset2 = [ 'lightcoral', 'yellowgreen', 'dodgerblue'] 
colorset3 = ['brown', 'goldenrod', 'olivedrab', 'mediumturquoise', 'royalblue' ]        
        

data = np.genfromtxt('data_precession.dat')
ntrim = 1500    
d0, d1, d2, d3, d4, d5, d6, d7, d8, d9 = data[:ntrim, 0], data[:ntrim, 1], data[:ntrim, 2], data[:ntrim, 3], data[:ntrim, 4], data[:ntrim, 5], data[:ntrim, 6], data[:ntrim, 7], data[:ntrim, 8], data[:ntrim, 9]


fig = plt.figure()
ax = fig.add_subplot(projection='3d')
#ax.set_axis_off()


ax.set_xlim(-1,1)
ax.set_ylim(-1,1)
ax.set_zlim(-1,1)
ax.set_xticks([-1, -0.5, 0, 0.5, 1])
ax.set_yticks([-1, -0.5, 0, 0.5, 1])
ax.set_zticks([-1, -0.5, 0, 0.5, 1])


ax.plot(d7,d8,d9, color='r', linestyle='dashed', linewidth=1 )


rm = 1.0


n = 500

u = np.linspace(0,2* np.pi,n);
v3 = np.linspace(0, np.pi, n);
x3 = rm * np.outer(np.cos(u), np.sin(v3));
y3 = rm * np.outer(np.sin(u), np.sin(v3));
z3 = rm * np.outer(np.ones(np.size(u)), np.cos(v3));
ax.plot_surface(x3, y3, z3, alpha=0.3,color=(7/255.0, 237/255.0, 242/255.0))


x1=d4[0]
y1=d5[0]
z1=d6[0]

x2=d7[0]
y2=d8[0]
z2=d9[0]


def compute_segs1(i):
    t = d0[i]
    #tip location
    u, v, w = np.meshgrid(d4[i], d5[i], d6[i])
    #tail location
    x = u*0.0
    y = v*0.0
    z = w*0.0

    return x,y,z,u,v,w
    
   
def compute_segs2(i):
    t = d0[i]
    #tip location
    u, v, w = np.meshgrid(d7[i], d8[i], d9[i])
    #tail location
    x = u*0.0
    y = v*0.0
    z = w*0.0

    return x,y,z,u,v,w
    
def compute_segs3(i):
    t = d0[i]
    #tip location
    u, v, w = np.meshgrid(d8[i]*d6[i]-d5[i]*d9[i], d9[i]*d4[i]-d6[i]*d7[i], d7[i]*d5[i]-d4[i]*d8[i])
    #tail location
    x = u*0.0
    y = v*0.0
    z = w*0.0

    return x,y,z,u,v,w

cols=['g','r', 'b']

alr=0.2
segs = compute_segs1(0)
quiver1 = ax.quiver(*segs, pivot='tail', colors = cols[0], arrow_length_ratio=alr)
segs = compute_segs2(0)
quiver2 = ax.quiver(*segs, pivot='tail', colors = cols[1], arrow_length_ratio=alr)
segs = compute_segs3(0)
quiver3 = ax.quiver(*segs, pivot='tail', colors = cols[2], arrow_length_ratio=alr)

def animate(i):
    global quiver1, quiver2, quiver3
    quiver1.remove()
    quiver2.remove()
    quiver3.remove()
    segs = compute_segs1(i)
    quiver1 = ax.quiver(*segs, pivot='tail', colors = cols[0], arrow_length_ratio=alr)
    segs = compute_segs2(i)
    quiver2 = ax.quiver(*segs, pivot='tail', colors = cols[1], arrow_length_ratio=alr)
    segs = compute_segs3(i)
    quiver3 = ax.quiver(*segs, pivot='tail', colors = cols[2], arrow_length_ratio=alr)
#    return quivers

ani = FuncAnimation(fig, animate, frames = 1500, interval = 10, blit=False)
#ani.save('pton2sphere.gif', writer='imagemagick')
ani.save('lvprecess.mp4', fps=50, extra_args=['-vcodec', 'libx264']) # video duration = frames/fps


#print(timeit.time.time() - t0)
#plt.show()



