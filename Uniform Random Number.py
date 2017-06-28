import random
import numpy as np

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

print(arr1)
print('Mean of 10,000 pseudo generated random variables is: ',np.mean(arr1))
print('Standard Deviation of 10,000 pseudo generated random variables is: ',np.std(arr1))

arr2 = np.zeros((1,10000),dtype=np.float64)
for i in range (0,10000):
    y = random.uniform(0,1)
    arr2[0,i] = y

print(arr2)
print('Mean of 10,000 pseudo generated random variables by inbuilt function is: ',np.mean(arr2))
print('Standard Deviation of 10,000 pseudo generated random variables by inbuilt function is: ',np.std(arr2))
