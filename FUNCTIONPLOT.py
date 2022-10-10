import numpy as np
import matplotlib.pyplot as plt
def f(x,a,b,c,d,e,h):
    return a*x**5 + b*x**4 + c*x**3+d*x**2+e*x**1+h
x_list=np.arange(-10,10,.001)
y_list=f(x_list,1,2,3,4,5,6)
plt.figure(num=0, dpi=300)
plt.plot(x_list, y_list)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()
