# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S465a28buN7MHhpUIbs9sphg1mxKbfxZ
"""

import math
from scipy.stats import binom
import matplotlib.pyplot as plt
import array as arr
import numpy as np
#function to calculate factorial
def fact_func(a):
  ans = 1
  for x in range(1 , a + 1):
    ans = ans * x
  return ans

#function to calculate binomial coefficient
def ncr(n , r):
  ans = fact_func(n) / (fact_func(r) * fact_func(n - r))
  return ans

#function to calculate the probability 
def prob_theo(n , p ,r):

  sum =  ( ncr(n , r) )* ( pow(p , r) ) * ( pow((1-p) , n - r) )
  return sum

p=0.05
#probability of part being defective


n=15
#total number of inspected parts


r_values = np.arange(n+1)


sample_size=500000

binom_dist=[binom.pmf(r, n, p) for r in r_values ] 

binomial_simulation = binom.rvs(n,p,size=sample_size)
#Array containing the simulated probability distribution for each value of r 

count=[0]*(n+1)
#array for count
prob_sim=[0]*(n+1)



for i in range(sample_size):
  for j in range(n+1) :
     if binomial_simulation[i] == j:
       count[j]+=1


 
for k in range(n+1):
  prob_sim[k]=count[k]/sample_size
#Theory Vs simulation.

print("simulated probability",(1-prob_sim[0]-prob_sim[1]))
x=1-prob_theo(15,0.05,0)-prob_theo(15,0.05,1)
print("theoritical Probability",x)

#plotting
# x-coordinates of left sides of bars 
left = [1, 2]
  
# heights of bars
height = [0.1709,0.1716]
  
# labels for bars
tick_label = ['Theory', 'Simulation']
  
# plotting a bar chart
plt.bar(left, height, tick_label = tick_label,
        width = 0.8, color = ['red', 'green'])
  

# naming the y-axis
plt.ylabel('Probability')
# plot title
plt.title('theory vs simulation')
  
# function to show the plot
plt.show()