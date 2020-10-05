import rosbag


x = []
y = []
z = []

roll = []
pitch = []
yaw = []


bag = rosbag.Bag('left_lidar_2020-10-05-14-15-24.bag')

for topic, msg, t in bag.read_messages(topics=['/ndt_pose']):

    x.append(msg.pose.position.x)
    y.append(msg.pose.position.y)
    z.append(msg.pose.position.z)

    roll.append(msg.pose.orientation.x)
    pitch.append(msg.pose.orientation.y)
    yaw.append(msg.pose.orientation.z)

bag.close()

print("X: ", sum(x)/(len(x)-1))
print("Y: ", sum(y)/(len(y)-1))
print("Z: ", sum(z)/(len(z)-1))

print("roll: ", sum(roll)/(len(roll)-1))
print("pitch: ", sum(pitch)/(len(pitch)-1))
print("yaw: ", sum(yaw)/(len(yaw)-1))