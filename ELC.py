import rosbag
from math import sqrt

from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt


x_t = []
y_t = []
z_t = []

roll_t = []
pitch_t = []
yaw_t = []

time_t = []

bag = rosbag.Bag('top_lidar_2020-09-22-17-53-20.bag')

for topic, msg, t in bag.read_messages(topics=['/ndt_pose']):
    # print(msg)
    # print(msg.header.stamp.nsecs)
    x_t.append(msg.pose.position.x)
    y_t.append(msg.pose.position.y)
    z_t.append(msg.pose.position.z)

    roll_t.append(msg.pose.orientation.x)
    pitch_t.append(msg.pose.orientation.y)
    yaw_t.append(msg.pose.orientation.z)

    # time_t.append(msg.)

bag.close()

x_t_np = np.array(x_t)
y_t_np = np.array(y_t)
z_t_np = np.array(z_t)

roll_t_np = np.array(roll_t)
pitch_t_np = np.array(pitch_t)
yaw_t_np = np.array(yaw_t)

x_r = []
y_r = []
z_r = []

roll_r = []
pitch_r = []
yaw_r = []

bag = rosbag.Bag('right_lidar_2020-09-22-17-51-00.bag')

for topic, msg, t in bag.read_messages(topics=['/ndt_pose']):
    x_r.append(msg.pose.position.x)
    y_r.append(msg.pose.position.y)
    z_r.append(msg.pose.position.z)

    roll_r.append(msg.pose.orientation.x)
    pitch_r.append(msg.pose.orientation.y)
    yaw_r.append(msg.pose.orientation.z)

bag.close()

x_r_np = np.array(x_r)
y_r_np = np.array(y_r)
z_r_np = np.array(z_r)

roll_r_np = np.array(roll_r)
pitch_r_np = np.array(pitch_r)
yaw_r_np = np.array(yaw_r)


roll_sum = 0
pitch_sum = 0
yaw_sum = 0

for i in range(len(roll_t_np)):
    roll_sum += roll_t_np[i] - roll_r_np[i]
    pitch_sum += pitch_t_np[i] - pitch_r_np[i]
    yaw_sum += yaw_t_np[i] - yaw_r_np[i]

ROLL = roll_sum/(len(roll_t_np)-1)
PITCH = pitch_sum/(len(roll_t_np)-1)
YAW = yaw_sum/(len(roll_t_np)-1)

print (ROLL)
print (PITCH)
print (YAW)

x_dif = []
y_dif = []
z_dif = []
r_dif = 0
for i in range(len(x_t_np)):
    x_dif.append(x_r[i] - x_t[i])
    y_dif.append(y_r[i] - y_t[i])
    z_dif.append(z_r[i] - z_t[i])
    r_dif += (sqrt(pow(x_dif[i], 2) + pow(y_dif[i], 2) + pow(z_dif[i], 2)))

R = r_dif/(len(x_t_np)-1)
print (R)
x_diff_np = np.array(x_dif)
y_diff_np = np.array(y_dif)
z_diff_np = np.array(z_dif)

# mpl.rcParams['legend.fontsize'] = 10
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_aspect('equal')

# ax.plot(x_t_np, y_t_np, z_t_np, label='top lidar', c='r', marker='o')
# ax.plot(x_r_np, y_r_np, z_r_np, label='right lidar')
# ax.scatter(x_diff_np, y_diff_np, z_diff_np, label='top lidar', c='r', marker='o')
ax.scatter(roll_t_np, pitch_t_np, yaw_t_np, label='top lidar', c='r', marker='o')
ax.scatter(roll_r_np, pitch_r_np, yaw_r_np, label='right lidar', c='b', marker='o')


x_viz = roll_r_np
y_viz = pitch_r_np
z_viz = yaw_r_np
# Create cubic bounding box to simulate equal aspect ratio
max_range = np.array([x_viz.max()-x_viz.min(), y_viz.max()-y_viz.min(), z_viz.max()-z_viz.min()]).max()
Xb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][0].flatten() + 0.5*(x_viz.max()+x_viz.min())
Yb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][1].flatten() + 0.5*(y_viz.max()+y_viz.min())
Zb = 0.5*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][2].flatten() + 0.5*(z_viz.max()+z_viz.min())
# Comment or uncomment following both lines to test the fake bounding box:
for xb, yb, zb in zip(Xb, Yb, Zb):
   ax.plot([xb], [yb], [zb], 'w')

ax.legend()

plt.show()