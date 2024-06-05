import numpy as np
import scipy.stats

def landmark_sensor_model(z, x, l, vr, vt):
    # z is your range and bearing, x robot pose, l is the landmark
    # position you can make use of a built in python in python to
    # compute your noise samples

    # define variables
    zr, zt = z
    x1, y, theta = x 
    lx, ly = l 
    r_hat = np.sqrt((lx - x1)**2 + (ly - y)**2)
    phi = np.arctan2(ly - y, lx - x1) - theta 
    phi = (phi + np.pi) % (2 * np.pi) - np.pi

    


    # compute your likelhood
    pr = scipy.stats.norm.pdf(zr - r_hat, 0, np.sqrt(vr))
    pt = scipy.stats.norm.pdf(zt - phi, 0, np.sqrt(vt))

    likelihood = pr*pt 

    return likelihood 

z = [[5.0, np.pi/4], [5.0, 0.6], [4.5, np.pi/4], [5.5, 0.9]]
x = [2,3,np.pi/4]
l = [2,8]
vr = 0.25 
vt = 0.01

for z_marks in z:
        likelihood = landmark_sensor_model(z_marks, x, l, vr, vt)
        print(likelihood)