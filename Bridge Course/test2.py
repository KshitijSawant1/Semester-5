import numpy as np
import matplotlib.pyplot as plt 
print()
print("Line Graph")
x = np.arange(1,11)
print(x)
y = 2*x
z=2**x
a =x+1
b= x-2
c=x*2
d=x*5
e=d/2
plt.plot(x,a)
plt.plot(x,b)
plt.plot(x,c)
plt.plot(x,d)
plt.plot(x,e)
plt.plot(x,y)
plt.title('Line Plot')
plt.show()