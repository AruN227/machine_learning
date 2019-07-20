import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.stats import expon
from scipy.stats import binom

#Bionomial pmf
n,p = 10, 0.5
data2 = np.arange(0,10,0.001)
plt.plot(data2, binom.pmf(data2,n,p))
print(plt.show())


data = np.arange(-3,3,0.001)
plt.plot(data, norm.pdf(data))
print(plt.show())


#exponential pdf

data1 = np.arange(0,10,0.001)
plt.plot(data1, expon.pdf(data1))
print(plt.show())