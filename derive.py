# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt


def derivative(X, Y):
    '''
    Численное дифференцирование dy/dx.
    Значение для последнего элемента находится интерполяцией.

    Return list производных
    '''

    dy = []

    for i in range(len(X) - 1):
        dy.append((Y[i + 1] - Y[i]) / (X[i + 1] - X[i]))

    dy.append(2 * dy[-1] - dy[-2])

    return dy


def get_curvature(d, dd):
    '''
    Нахождение кривизны кривой по производным

    http://www.math24.ru/%D0%BA%D1%80%D0%B8%D0%B2%D0%B8%D0%B7%D0%BD%D0%B0-%D0%BF%D0%BB%D0%BE%D1%81%D0%BA%D0%B8%D1%85-%D0%BB%D0%B8%D0%BD%D0%B8%D0%B9.html
    '''

    curve = []

    for i in range(len(d)):
        curve.append(dd[i] / (1 + d[i]**2)**1.5)

    return curve


def main():

    ### Дискретный набор точек из полинома четвертой степени

    # X_np = np.arange(-1.0, 2.0, 0.1)
    #
    # Y = []
    #
    # for x in X_np:
    #     y = np.power(x, 4) - 3 * np.power(x, 3) + 2 * np.power(x, 2) + x + 3
    #     Y.append(y)
    #
    # Y_np = np.array(Y)


    ### Дискретный набор точек из Global Planner

    # X_np = np.array([-155.707, -154.956, -154.158, -153.315, -152.443, -151.553, -150.647, -149.73, -148.804, -147.872, -146.935, -145.994, -145.051, -144.105, -143.152, -142.194, -141.231, -140.265, -139.296, -138.324, -137.348, -136.368, -135.386, -134.402, -133.417, -132.432, -131.447, -130.462, -129.476, -128.49, -127.503, -126.514, -125.525, -124.535, -123.544, -122.552, -121.56, -120.568, -119.576, -118.584, -117.592, -116.6, -115.608, -114.616, -113.624, -112.632, -111.64, -110.649, -109.657, -108.666, -107.676, -106.69, -105.713, -104.754, -103.82, -102.924, -102.06, -101.222, -100.407, -99.6202, -98.8741, -98.1997, -97.5724, -96.9761, -96.4069, -95.8715, -95.3606])

    # Y_np = np.array([-350.082, -350.719, -351.299, -351.817, -352.292, -352.736, -353.152, -353.545, -353.919, -354.279, -354.625, -354.963, -355.294, -355.615, -355.916, -356.2, -356.469, -356.726, -356.97, -357.201, -357.419, -357.616, -357.8, -357.978, -358.151, -358.323, -358.493, -358.663, -358.83, -358.996, -359.156, -359.308, -359.453, -359.592, -359.726, -359.854, -359.98, -360.105, -360.231, -360.357, -360.483, -360.609, -360.735, -360.861, -360.986, -361.109, -361.23, -361.345, -361.449, -361.534, -361.589, -361.591, -361.521, -361.337, -361.049, -360.655, -360.185, -359.662, -359.101, -358.504, -357.861, -357.142, -356.376, -355.582, -354.767, -353.927, -353.07])

    ### Дискретный набор точек окружности

    phi_step = 1.0     # градусы
    radius = 20

    step = phi_step / 180 * np.pi
    phi_np = np.arange(0.0, 2.0 * np.pi - step, step)

    X_np = radius * np.cos(phi_np)
    Y_np = radius * np.sin(phi_np)

    ### Интерполяция

    if False:
        z = np.polyfit(X_np[-30:-1], Y_np[-30:-1], 4)

        xp = np.arange(-110.0, -95.0, 0.5)

        p = np.poly1d(z)

    ### Нахождение производных
    if True:

        for i in range(len(X_np) - 1):
            if abs(X_np[i] - X_np[i+1]) < 10e-6:

                diff = (Y_np[i + 1] - Y_np[i]) / (X_np[i + 1] - X_np[i])
                print(diff)

        d = derivative(X_np, Y_np)

        D = np.array(d)

        dd = derivative(X_np, D)

        DD = np.array(dd)

        ### Получение кривизны
        c = get_curvature(D, DD)

        c_np = np.array(c)


    ### Отрисовка графиков
    fig = plt.figure()
    ax = fig.gca()

    # ax.scatter(X_np, Y_np, c='r', marker='o')
    # ax.scatter(X_np, D, c='b', marker='o')
    # ax.scatter(X_np, DD, c='--r', marker='o')
    # ax.scatter(X_np, c_np, c='b', marker='o')

    # plt.plot(X_np, Y_np, c='b', marker='o')
    # plt.plot(xp, p(xp), c='g', marker='o')
    plt.plot(X_np, D, c='g', marker='o')
    # plt.plot(xp, DD, c='r', marker='o')
    # plt.plot(xp, c_np, c='b', marker='o')

    # plt.gca().set_aspect('equal', adjustable='box')
    plt.show()



if __name__ == "__main__":
    main()