import numpy as np
import matplotlib.pyplot as plt
import math

def box_muller(mu, var):
    # this function should give you a sample according to N(mu,sigma^2=var)
    '''
    var = var**0.5
    x=[]
    i = 0
    for i in range(11):
        x.append(np.random.uniform(-var, var))
        i +=1
    x = sum(x)
 
    y = mu + 0.5*x
    '''

    var = var **0.5 
    x= 0
    for i in range(1,13):
        x = x+ np.random.uniform(-var, var)
    y = x*0.5 + mu 

    return y

def predict(x_t, u_t_plus_1, alpha):
    # Add noise odometry reading
    x,y,theta = x_t 
    x = float(x) 
    y = float(y)
    theta = float(theta)
    delta_1 , delta_2, delta_trans = u_t_plus_1
    a1,a2, a3, a4 = alpha 

    delta_1 = delta_1 - box_muller(0,(a1*(delta_1)**2 + a2*(delta_2)**2))
    delta_trans = delta_trans - box_muller(0,(a3*(delta_trans)**2 + a4*(delta_1**2 + delta_2**2 )))
    delta_2 = delta_2 - box_muller(0,(a1*(delta_1)**2 + a2*(delta_2)**2))

    # Compute new pose
    
    #[x_prime, y_prime, theta_prime] = np.array([[x], [y], [theta]]) + np.array([[delta_trans_hat*np.cos(theta + delta_1_hat)],[delta_trans_hat*np.sin(theta + delta_1_hat)], [delta_1_hat + delta_2_hat]])

    #x_prime = np.array([[x]]) + np.array([[delta_trans_hat*np.cos(theta + delta_1_hat)]])
    #y_prime = np.array([[y]]) + np.array([[delta_trans_hat*np.sin(theta + delta_1_hat)]])
    #theta_prime = np.array([theta]) + np.array([delta_1_hat + delta_2_hat])
    x_prime = x + delta_trans*np.cos(theta + delta_1)
    y_prime = y + delta_trans*np.sin(theta + delta_1)
    theta_prime = theta + (delta_1 + delta_2)
    return x_prime, y_prime, theta_prime

if __name__ == '__main__':
    # plot scatter plot with 5000 positions
    x_t = [2, 4, 0]
    u_t_plus_1 = [np.pi/2, 0, 1]
    alpha = [0.1, 0.1, 0.01, 0.01]

    x_p_list, y_p_list, t_p_list = [], [], []
    
    for i in range(5000):
        x_p, y_p, t_p = predict(x_t, u_t_plus_1, alpha)
        x_p_list.append(x_p)
        y_p_list.append(y_p)
        t_p_list.append(t_p)
        #plt.scatter(x_p, y_p)
    
    
    print( x_p)
    print( y_p)
    print(t_p)

    plt.scatter(x_p_list, y_p_list)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid()
    plt.show()
