import matplotlib.pyplot as plt
import numpy as np
import math

a = pow(7,5)
b = 0
m = 2**31 - 1
x = 18
# Seed
arr1 = np.zeros((1,10000),dtype=np.float64)
for i in range (10000):
    x = (a*x+b)% m
    u1 = x/m
    arr1[0,i] = u1

lam = 1.5

arr2 = np.zeros((1,10000),dtype=np.float64)
for i in range (10000):
    Erand = -lam*math.log(1-arr1[0,i])
    arr2[0,i] = Erand
print (arr2)
X1=0
X2=0
for i in range (10000):
    if arr2[0,i]>=1:
        X1 +=1
for i in range(10000):
    if arr2[0,i]>=4:
        X2 +=1

print (X1,X2)
print('Probability that random variable X is greater and equal to 1: ', (X1 / 10000))
print('Probability that random variable X is greater and equal to 4: ', (X2 / 10000))
print('Mean of 1,000 pseudo generated random variables is: ',np.mean(arr2))
print('Standard Deviation of 1,000 pseudo generated random variables is: ',np.std(arr2))
plt.hist(arr2[0], bins=10, histtype='bar', rwidth=0.8, color='r')
plt.xlabel('Value of Exponential Random Number')
plt.ylabel('No. of Random Variables')
plt.title('Random Exponential Number Generation')
plt.show()




