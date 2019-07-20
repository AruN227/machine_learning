import numpy as np
import matplotlib.pyplot as plt


data = np.random.normal(80.0,20.0,10000)
plt.hist(data,50)
print(plt.show())