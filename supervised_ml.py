import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import  r2_score


pageSpeeds = np.random.normal(3.0,1.0,100)
purchaseAmount = np.random.normal(50.0,30.0,100) / pageSpeeds

#plt.scatter(pageSpeeds, purchaseAmount)
#print(plt.show())

trainX = pageSpeeds[:80]
testX = pageSpeeds[80:]

trainY = purchaseAmount[:80]
testY = purchaseAmount[80:]

#plt.scatter(testX,testY)
#print(plt.show())

x = np.array(trainX)
y = np.array(trainY)

p4 = np.poly1d(np.polyfit(x,y,2))

xp = np.linspace(0,7,100)
axes = plt.axes()
axes.set_xlim([0,7])
axes.set_ylim([0,200])
plt.scatter(trainX,trainY)
plt.plot(xp,p4(xp), c='r')
print(plt.show())

r2 = r2_score(np.array(trainY), p4(np.array(trainX)))
print(r2)



