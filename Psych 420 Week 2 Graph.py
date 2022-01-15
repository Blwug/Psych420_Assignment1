#this was the example given in the study.
import matplotlib.pyplot as plt
import numpy as np
a = np.linspace(-4,6,num=120)
b = [x**3 for x in a];#list comprehension
plt.clf()
plt.plot(a,b)
plt.plot([2,2],[-100,8], 'k-',lw=2)
plt.plot([-4,2],[8,8], 'k-',lw=2)
plt.plot([4,4],[64,-100], 'k-',lw=2)
plt.plot([-4,6],[-64,56], 'r-',lw=2)
plt.plot([-4,4],[64,64], 'k-',lw=2)
plt.plot([4,6],[64,64], 'k--',lw=2)
plt.plot([2,4],[8,64], 'k-',lw=2)
plt.savefig('temp.png')

