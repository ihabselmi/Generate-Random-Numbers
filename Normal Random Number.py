import matplotlib.pyplot as plt
import numpy as np
import math
import time

a = pow(7,5)
b = 0
m = 2**31 - 1
x = 18
# Seed
arr1 = np.zeros((1,5000),dtype=np.float64)
for i in range (5000):
    x = (a*x+b)% m
    u1 = x/m
    arr1[0,i] = u1

start = time.time()
arr2 = np.zeros((1,5000),dtype=np.float64)
for i in range (0,5000,2):
    Z1 = math.sqrt(-2 * math.log(arr1[0, i])) * math.cos(2 * math.pi * (arr1[0, i + 1]))
    arr2[0,i] = Z1
    Z2 = math.sqrt(-2 * math.log(arr1[0, i])) * math.sin(2 * math.pi * (arr1[0, i + 1]))
    arr2[0, i+1] = Z2
end = time.time()
print('Time took to calculate the Box Muller 5000 Normal Randon Variables' ,end - start)

print('Mean of 5,000 pseudo generated normal random variables is: ', np.mean(arr2))
print('Variance of 5,000 pseudo generated normal random variables is: ',np.var(arr2))

start = time.time()
arr3 = np.array((),dtype=np.float64)
for i in range(0,5000,2):
    V1 = 2*arr1[0, i] - 1
    V2 = 2*arr1[0, i+1] - 1
    W = pow(V1,2) + pow(V2,2)
    if W <= 1:
        Z3 = V1 * math.sqrt(-2 * math.log(W)/W)
        Z4 = V2 * math.sqrt(-2 * math.log(W)/W)
        arr3 = np.append(arr3,[Z3,Z4])
end = time.time()
print('Time took to calculate the Polar Marsaglia arounf 75% of 5000 Normal Randon Variables' ,end - start)

print ('Number of Normal Random Variable from 5000 Uniform random variables under Polar Marsaglia: ',len(arr3))
print('Mean of pseudo generated normal random variable under Polar Marsaglia is: ', np.mean(arr3))
print('Variance of pseudo generated normal random variables under Polar Marsaglia is: ',np.var(arr3))

plt.hist(arr2[0], bins=20, histtype='bar', rwidth=0.8, color='r')
plt.xlabel('Value of Normal Random Number ')
plt.ylabel('No. of Random Variables')
plt.title('Random Normal Number Generation under Box Muller')
plt.show()

plt.hist(arr3, bins=20, histtype='bar', rwidth=0.8, color='b')
plt.xlabel('Value of Normal Random Number')
plt.ylabel('No. of Random Variables')
plt.title('Random Normal Number Generation under Polar Marsaglia')
plt.show()

# lam = 1.5
#
# arr2 = np.zeros((1,10000),dtype=np.float64)
# for i in range (10000):
#     Erand = -lam*math.log(1-arr1[0,i])
#     arr2[0,i] = Erand
# print (arr2)
# X1=0
# X2=0
# for i in range (10000):
#     if arr2[0,i]>=1:
#         X1 +=1
# for i in range(10000):
#     if arr2[0,i]>=4:
#         X2 +=1
#
# print (X1,X2)
# print('Probability that random variable X is greater and equal to 1: ', (X1 / 10000))
# print('Probability that random variable X is greater and equal to 4: ', (X2 / 10000))
# print('Mean of 1,000 pseudo generated random variables is: ',np.mean(arr2))
# print('Standard Deviation of 1,000 pseudo generated random variables is: ',np.std(arr2))
# plt.hist(arr2[0], bins=10, histtype='bar', rwidth=0.8, color='r')
# plt.xlabel('Value of Exponential Random Number')
# plt.ylabel('No. of Random Variables')
# plt.title('Random Exponential Number Generation')
# plt.show()




