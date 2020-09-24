import rosbag
from math import sqrt

from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt


def rotate_point(roll, pitch, yaw, x, y, z):
    c_x, s_x = np.cos(roll), np.sin(roll)
    R_x = np.array(((1, 0, 0), (0, c_x, -s_x), (0, s_x, c_x)))

    c_y, s_y = np.cos(pitch), np.sin(pitch)
    R_y = np.array(((c_y, 0, s_y), (0, 1, 0), (-s_x, 0, c_x)))

    c_z, s_z = np.cos(yaw), np.sin(yaw)
    R_z = np.array(((c_z, -s_z, 0), (s_z, c_x, 0), (0, 0, 1)))

    # print("R_x: ", roll)
    # print(R_x)
    # print("R_y: ", pitch)
    # print(R_y)
    # print("R_z: ", yaw)
    # print(R_z)

    res = np.dot(R_z, R_y)

    # print("Res: ")
    # print res

    res2 = np.dot(R_x, res)

    # print("Res2: ")
    # print res2

    P = np.array((x, y, z))
    # print("Point: ")
    # print(P)
    cor = np.dot(res2, P)

    # print("cor: ")
    # print(cor)

    x_cor = cor[0]
    y_cor = cor[1]
    z_cor = cor[2]

    return x_cor, y_cor, z_cor


x_t = []
y_t = []
z_t = []

roll_t = []
pitch_t = []
yaw_t = []

time_t = []

bag = rosbag.Bag('top_lidar_2020-09-23-19-33-27.bag')

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

print(len(x_t))

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

bag = rosbag.Bag('right_lidar_2020-09-23-19-35-48.bag')

for topic, msg, t in bag.read_messages(topics=['/ndt_pose']):
    x_r.append(msg.pose.position.x)
    y_r.append(msg.pose.position.y)
    z_r.append(msg.pose.position.z)

    roll_r.append(msg.pose.orientation.x)
    pitch_r.append(msg.pose.orientation.y)
    yaw_r.append(msg.pose.orientation.z)

bag.close()

print(len(x_r))
x_r_np = np.array(x_r)
y_r_np = np.array(y_r)
z_r_np = np.array(z_r)

roll_r_np = np.array(roll_r)
pitch_r_np = np.array(pitch_r)
yaw_r_np = np.array(yaw_r)

x_dif = []
y_dif = []
z_dif = []
r_dif = 0
for i in range(len(x_r_np)):
    x_dif.append(x_r[i] - x_t[i])
    y_dif.append(y_r[i] - y_t[i])
    z_dif.append(z_r[i] - z_t[i])
    r_dif += (sqrt(pow(x_dif[i], 2) + pow(y_dif[i], 2) + pow(z_dif[i], 2)))

R = r_dif/(len(x_r_np)-1)
print (R)
x_diff_np = np.array(x_dif)
y_diff_np = np.array(y_dif)
z_diff_np = np.array(z_dif)


roll_sum = 0
pitch_sum = 0
yaw_sum = 0

roll_rt = []
pitch_rt = []
yaw_rt = []

x_c = []
y_c = []
z_c = []

for i in range(len(roll_r_np)):
    roll_diff = roll_t_np[i] - roll_r_np[i]
    roll_sum += roll_diff
    pitch_diff = pitch_t_np[i] - pitch_r_np[i]
    pitch_sum += pitch_diff
    yaw_diff = yaw_t_np[i] - yaw_r_np[i]
    yaw_sum += yaw_diff
    x_cor, y_cor, z_cor = rotate_point(-roll_t_np[i], -pitch_t_np[i], -yaw_t_np[i], x_dif[i], y_dif[i], z_dif[i])
    x_c.append(x_cor)
    y_c.append(y_cor)
    z_c.append(z_cor)

    if yaw_diff > 0:
        roll_rt.append(roll_diff)
        pitch_rt.append(pitch_diff)
        yaw_rt.append(yaw_diff)

ROLL = roll_sum/(len(roll_r_np)-1)
PITCH = pitch_sum/(len(roll_r_np)-1)
YAW = yaw_sum/(len(roll_r_np)-1)

roll_rt_np = np.array(roll_rt)
pitch_rt_np = np.array(pitch_rt)
yaw_rt_np = np.array(yaw_rt)

x_c_np = np.array(x_c)
y_c_np = np.array(y_c)
z_c_np = np.array(z_c)

print (ROLL)
print (PITCH)
print (YAW)



# mpl.rcParams['legend.fontsize'] = 10
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_aspect('equal')

# ax.plot(x_t_np, y_t_np, z_t_np, label='top lidar')
# ax.plot(x_r_np, y_r_np, z_r_np, label='right lidar')
# ax.scatter(x_diff_np, y_diff_np, z_diff_np, label='top lidar', c='r', marker='o')
ax.scatter(x_c_np, y_c_np, z_c_np, label='top lidar', c='r', marker='o')

# ax.scatter(roll_t_np, pitch_t_np, yaw_t_np, label='top lidar', c='r', marker='o')
# ax.scatter(roll_r_np, pitch_r_np, yaw_r_np, label='right lidar', c='b', marker='o')

# ax.scatter(roll_rt_np, pitch_rt_np, yaw_rt_np, label='right lidar', c='b', marker='o')


x_viz = x_c_np
y_viz = y_c_np
z_viz = z_c_np
# Create cubic bounding box to simulate equal aspect ratio
max_range = np.array([x_viz.max()-x_viz.min(), y_viz.max()-y_viz.min(), z_viz.max()-z_viz.min()]).max()
Xb = 0.1*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][0].flatten() + 0.1*(x_viz.max()+x_viz.min())
Yb = 0.1*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][1].flatten() + 0.1*(y_viz.max()+y_viz.min())
Zb = 0.1*max_range*np.mgrid[-1:2:2,-1:2:2,-1:2:2][2].flatten() + 0.1*(z_viz.max()+z_viz.min())
# Comment or uncomment following both lines to test the fake bounding box:
for xb, yb, zb in zip(Xb, Yb, Zb):
   ax.plot([xb], [yb], [zb], 'w')

ax.legend()

plt.show()