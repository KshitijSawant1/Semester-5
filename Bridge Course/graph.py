import numpy as np
from matplotlib import pyplot as plt 

#Line Plot
print()
print("Line Plot")
x = np.arange(1,11)
print(x)
y=2*x
print(y)
plt.plot(x,y,color="red",linestyle="dashed",marker="o",linewidth=3,markerfacecolor="blue",markersize=12)
plt.title('Line plot')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

#Line Plot grid 2X
print()
print("Line Plot grid 2X")
x = np.arange(1,11)
print(x)
y1=2*x
print(y1)
y2=4*x
print(y2)
plt.plot(x,y1,color="red",marker="o",linewidth=2,markerfacecolor="orange",markersize=12)
plt.plot(x,y2,color="blue",linestyle="dashed",marker="*",linewidth=2,markerfacecolor="white",markersize=12)
plt.grid(True)
plt.title('Line plot')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()


#Line Plot grid 2 subplots
print()
print("Line Plot grid subplots")
x = np.arange(1,11)
print(x)
y1=2*x
print(y1)
y2=4*x
print(y2)
plt.subplot(2,1,1)
plt.plot(x,y1,color="red",marker="o",linewidth=2,markerfacecolor="orange",markersize=12)
plt.grid(True) 
plt.title('Line plot 1')
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.subplot(2,1,2)
plt.plot(x,y2,color="blue",linestyle="dashed",marker="*",linewidth=2,markerfacecolor="white",markersize=12)
plt.grid(True)
plt.title('Line plot 2')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

# Bar graph
print()
print("Bar graph")
Student= {"Alex":87,"Bob":56,"Clark":75,"Den":64,"Emily":46,"Frank":78,"George":90,"Hank":73,"Ivon":32,"Jack":82,"Kent":92,"Leo":69,"Mary":72,"Nataliya":59}
name = list(Student.keys())
print(name)
marks = list(Student.values())
print(marks)
plt.bar(name,marks,color="Black")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

# Scatter Plot
print()
print("Scatter graph")
x=[1,2,3,4,5,6,7,8,9]
print(x)
y=[2,3,4,5,7,8,1,9,0]
print(y)
plt.scatter(x,y,color='g')
plt.show()


# Histogram Plot
print()
print("Histogram graph")
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(data)
plt.hist(data, color='g', bins=4)
plt.title("Histogram of Data")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
