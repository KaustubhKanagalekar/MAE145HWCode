import numpy as np

def predict_next_pos(x, y, theta, vel_l, vel_r, t, l, R):
    # implement the exact differential drive motion model here
    # from the initial pose x,y ,theta, obtain the next pose x_1, y_1, \theta_1
    w = R*(vel_r - vel_l)/l
    v = R*(vel_r + vel_l)/2 

    if w == 0:
        x_1 = x + v*np.cos(theta)*t 
        y_1 = y + v*np.sin(theta)*t
        theta_1 = theta 
        
    else: 
        x_1 = np.array([x]) + np.array([[-v/w*np.sin(theta) + v/w*np.sin(theta + w*t)]])
        y_1 = np.array([y]) + np.array([[v/w*np.cos(theta) - v/w*np.cos(theta + w*t)]])
        theta_1 = np.array([theta]) + np.array([[w*t]])
    return x_1, y_1, theta_1



