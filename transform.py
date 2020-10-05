import numpy as np

def get_Rt(x, y, z, roll, pitch, yaw):

    c_x, s_x = np.cos(roll), np.sin(roll)
    R_x = np.array(((1, 0, 0), (0, c_x, -s_x), (0, s_x, c_x)))
    print(R_x)
    print(np.linalg.det(R_x))

    c_y, s_y = np.cos(pitch), np.sin(pitch)
    R_y = np.array(((c_y, 0, s_y), (0, 1, 0), (-s_x, 0, c_x)))
    print(R_y)
    print(np.linalg.det(R_y))

    c_z, s_z = np.cos(yaw), np.sin(yaw)
    R_z = np.array(((c_z, -s_z, 0), (s_z, c_x, 0), (0, 0, 1)))
    print(R_z)
    print(np.linalg.det(R_z))

    res = np.dot(R_x, R_y)
    res = np.dot(res, R_z)

    return res



x_top = 2.1158119261264803
y_top = 0.5559505902230739
z_top = -0.10251651778817177

roll_top = -0.1358768588952717
pitch_top = 0.0208960986437725
yaw_top = -2.8537542211557736


x_right = 1.948785201032111
y_right = 1.1576138075361861
z_right = -0.24876982417512447

roll_right = 0.3960396441923189
pitch_right = -0.025388206206566677
yaw_right = -2.8625014831074194

map2top = get_Rt(x_top, y_top, z_top, roll_top, pitch_top, yaw_top)
map2right = get_Rt(x_right, y_right, z_right, roll_right, pitch_right, yaw_right)


right2map = np.linalg.inv(map2right)
# print(np.dot(right2map, map2right))

# print(np.linalg.det(right2map))
# print(1/np.linalg.det(map2right))

right2top = np.dot(right2map, map2top)

# print(right2top)

top = np.array([x_top, y_top, z_top])

right = np.array([x_right, y_right, z_right])

right_point_in_map = np.dot(right2map, right)

# print(right_point_in_map + top)



# row = np.array([[0, 0, 0]])
#
# res = np.append(res, row, axis=0)
#
# column = np.array([[x], [y], [z], [1]])
#
# res = np.append(res, column, axis=1)
