from python_program_template_q4 import predict_next_pos
import numpy as np

def kinematic_properties(x, y, theta, vel_l, vel_r, t, L, R):
    omega = R*(vel_r-vel_l)/L
    vel = R*(vel_r + vel_l) / 2

    if omega == 0:
        rad_curv = float('inf')
        x_c = float('inf')
        y_c = float('inf')
    else:
        rad_curv = vel/omega
        x_c = x - vel/omega*np.sin(theta)
        y_c = y + vel/omega*np.cos(theta)

    icc = (x_c, y_c)
    return omega, rad_curv, icc

if __name__ == '__main__':
    L = 0.5
    R = 0.15

    x = 1.5
    y = 2.0
    theta = np.pi/2
    commands = ((0.3, 0.3, 3), (0.1, -0.1, 1), (0.2, 0, 2), (0.1, 0.2, 3))
    for command in commands:
        omega, rad_curv, icc = kinematic_properties(x, y, theta, command[0], command[1], command[2], L, R)
        print("omega = ", omega)
        print("rad_curve =", rad_curv)
        print("icc =", icc)
        x, y, theta = predict_next_pos(x, y, theta, command[0], command[1], command[2], L, R)
        print("x =", x)
        print("y = ", y)
        print("theta = ", theta)
    
    
