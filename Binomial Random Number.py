from scipy.stats import binom
import matplotlib.pyplot as plt
import numpy as np

a = pow(7,5)
b = 0
m = 2**31 - 1
x = 18
# Seed
arr1 = np.zeros((1,44000),dtype=np.float64)
for i in range (44000):
    x = (a*x+b)% m
    u1 = x/m
    arr1[0,i] = u1

for i in range (44000):
    if arr1[0,i] <= 0.64:
        arr1[0,i] = 1
    else:
        arr1[0,i] = 0


arr2 = np.zeros((1,1000),dtype=np.float64)
for i in range (1000):
    for j in range (44):
        arr2[0,i] += arr1[0,(j+44*i)]

plt.hist(arr2[0], bins=40, histtype='bar', rwidth=0.8, color='r')
plt.xlabel('Value of Binomial Random Number')
plt.ylabel('No. of Random Variables')
plt.title('Random Binomial Number Generation')
plt.show()

sum =0
for i in range (1000):
    if arr2[0,i]>=40:
        sum +=1

print ('Probability that random variable X ia at least 40 by out distribution: ', (sum/1000))
cdf = binom.cdf(40,44,.64)
print('Probability that random variable X ia at least 40 by formula driven: ', (1-cdf))




