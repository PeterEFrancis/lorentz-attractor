# Preferences: 

# this defines how much of the graph is added at a time
SEGMENT_LENGTH = 50
# ...and how quickly
TIME_STEP = 10

# name of data file (by default, set to the data I generated):
DATA_FILE = 'L_DATA.npy'

# figure size
SIZE = 10








import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation


data = np.load(DATA_FILE) # N x 3 data array

def add_segment(n):
    pts = data[n:n+SEGMENT_LENGTH].T
    ax.plot(pts[0], pts[1], pts[2], 'b', linewidth=0.2)
    return None

fig = plt.figure(figsize=(int(SIZE),int(SIZE)))
ax = p3.Axes3D(fig)
ax.set_xlim3d([-25, 25])
ax.set_xlabel('X')
ax.set_ylim3d([-30, 30])
ax.set_ylabel('Y')
ax.set_zlim3d([-5,53])
ax.set_zlabel('Z')
ax.set_title('Lorenz Attractor')

# Create the Animation object
line_ani = animation.FuncAnimation(fig, add_segment, range(0, len(data) - SEGMENT_LENGTH, SEGMENT_LENGTH - 1), 
                                   interval=TIME_STEP, blit=False)

# each interval (time step defined as interval = 1 here),
# the function add_segment is run with argument with next
# value in the iterable right after it. In this case, a range object

plt.show()

