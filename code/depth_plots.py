# Demo on how to vizualize depth data and on how to compute
# projections on the three Cartesian planes.

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# File containing only one depth frame from a depth video.
filename = '../data/msrda_frame.txt'

# Plot a frame of a depth video from the MSRDailyActivity3D dataset.
with open(filename) as f:
    first_line = f.readline()
    parts = [int(num) for num in first_line.split(',')]
    nframes = parts[0]
    nrows = parts[1]
    ncols = parts[2]

    depth_map = [f.readline() for i in range(nrows)]
    d = np.zeros((nrows, ncols))
    for i in range(len(depth_map)):
        line = depth_map[i]
        elems = [int(num) for num in line.split(',')]
        for j in range(len(elems)):
            d[i][j] = elems[j]

plt.matshow(d, cmap=plt.cm.gray_r)
plt.savefig('../results/depth_plot.png')

# Compute and plot the depth point cloud.

# The following values belong to the Kinect Camera that was used
# while filming the MSRDailyActivity 3D dataset.
cx = 343.645038678435410 # Main point, the center of the image.
cy = 229.805975111304460
fx = 458.455478616934780 # Focal length in the direction of x.
fy = 458.199272745572390 # ...and y.

def depth_to_point_cloud_pos(x, y, d):
    pz = d
    px = (x - cx) * pz / fx
    py = (y - cy) * pz / fy
    return (px, py, pz)

# For the purpose of this demo, we only plot the first depth frame.
Xs = []
Ys = []
Zs = []
for i in range(nrows):
    for j in range(ncols):
        (xs, ys, zs) = depth_to_point_cloud_pos(i, j, d[i][j])
        Xs.append(xs)
        Ys.append(ys)
        Zs.append(zs)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(Xs, Ys, Zs, c=Zs, cmap=cm.gist_stern, s=0.3)

ax.view_init(100, 0)
plt.draw()
plt.savefig('../results/point_cloud.png')

# Plot the three projections on the Cartesian planes.
plt.figure()
plt.scatter(Zs, Ys, c='black', s=0.5)
plt.savefig('../results/proj_ox.png')

plt.figure()
plt.scatter(Zs, [-x for x in Xs], c='black', s=0.5)
plt.savefig('../results/proj_oy.png')

plt.figure()
plt.scatter(Ys, [-x for x in Xs], c='black', s=0.5)
plt.savefig('../results/proj_oz.png')
