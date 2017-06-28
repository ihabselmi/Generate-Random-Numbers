import random
import numpy as np
import matplotlib.pyplot as plt

a = pow(7,5)
b = 0
m = 2**31 - 1
x = 0.1
# Seed
arr1 = np.zeros((1,10000),dtype=np.float64)
for i in range (10000):
    x = (a*x+b)% m
    u1 = x/m
    arr1[0,i] = u1

print(arr1)

arr2 = np.zeros((1,10000),dtype=np.float64)
for i in range (10000):
    if arr1[0,i]<=0.3:
        x= -1
    elif 0.3<arr1[0,i]<=(0.3+.35):
        x=0 
    elif (0.3+.35)<arr1[0,i]<=(0.3+.35+.2):
        x=1
    else:
        x=2
    arr2[0,i]=x
    

print(arr2)
bins =[-2,-1,0,1,2,3,4]
plt.hist(arr2[0], bins, histtype='bar', rwidth=0.8, color='r')

plt.xlabel('Value of Random Number')
plt.ylabel('No. of Random Variables')
plt.title('Random Number Generation')
plt.show()
print('Mean of 10,000 pseudo generated random variables is: ',np.mean(arr2))
print('Standard Deviation of 10,000 pseudo generated random variables is: ',np.std(arr2))

