import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


def predict(x):
    return slope * x + intercept

pageSpeeds = np.random.normal(3.0,1.0,1000)
purchaseAmount = 100 - (pageSpeeds + np.random.normal(0,0.1,1000)) * 3

slope,intercept,r_value,p_value,std_err = stats.linregress(pageSpeeds, purchaseAmount)
fitLine = predict(pageSpeeds)

plt.scatter(pageSpeeds, purchaseAmount)
plt.plot(pageSpeeds,fitLine, c='r')
print(plt.show())