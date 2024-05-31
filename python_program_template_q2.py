import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np


def sample_normal_distribution(mu, var):
    # define variables
    var = var**0.5
    x=[]
    i = 0
    for i in range(12):
        x.append(np.random.uniform(-var, var))
        i +=1
    x = sum(x)
 
    y = mu + 0.5*x
    
    return y
    
if __name__ == '__main__':
    y = []
    mu = 100
    sigma = 15
    samples = 10000
    
    for sample in range(samples):
        y.append(sample_normal_distribution(mu, sigma))
    # plot the histogram of the data 
    # the histogram of the data
    plt.hist(y, bins=100, density=True, alpha=0.6, color='g') 
    plt.xlabel('x')
    plt.ylabel('Frequency')
    plt.title('Histogram of Normal Distribution')
    plt.grid(False)

    plt.show()
