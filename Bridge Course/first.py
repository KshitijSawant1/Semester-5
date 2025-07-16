import numpy as np 
print()
print ("Single Dimensional Array")
l1 = [10,20,30,40]
n1= np.array(l1)
print(n1)

# Multidimensional Array 
print()
print ("Single Dimensional Array")
l1 = ([10,20,30,40],[10,20,30,40])
n1= np.array(l1)
print(n1)

# Multidimensional Zeros filling Array 
print()
print ("Multi Dimensional Array with zeros")
n1= np.zeros([5,5])
print(n1)

# Multidimensional Array initailaize with range
print()
print ("Multidimensional Array initailaize with range")
n1= np.arange(10,20)
print(n1)

# Single Dimensional Array Random form n numebrs
print()
print ("Single Dimensional Array Random form n numbers")
n1= np.random.randint(1,100,5)
print(n1)


# Multi Dimensional Stack Horizonatlly
print()
print ("Multi Dimensional Stack Horizonatlly")
n1= np.array([10,20,30])
n2= np.array([40,50,60])
np.hstack((n1,n2))
print(n1)

# Multi Dimensional Stack Vertical
print()
print ("Multi Dimensional Stack vertical")
n1= np.array([10,20,30])
n2= np.array([40,50,60])
np.vstack((n1,n2))
print(n1)

# Multi Dimensional Stack Column 
print()
print ("Multi Dimensional Stack Column")
n1= np.array([10,20,30])
n2= np.array([40,50,60])
np.column_stack((n1,n2))
print(n1)


# Intersection in arrays 
print()
print ("Intersection in arrays ")
n1= np.array([10,20,30,40,50])
n2= np.array([40,50,60,70,80])
np.intersect1d(n1,n2)
print(n1)

# Difference in arrays 
print()
print ("Intersection in arrays ")
n1= np.array([10,20,30,40,50])
n2= np.array([40,50,60,70,80])
np.setdiff1d(n1,n2)
print(n1)

# Sum of arrays 
print()
print ("Sum of arrays  ")
n1= np.array([10,20,30,40,50])
n2= np.array([40,50,60,70,80])
np.sum([n1,n2])
print(n1)

# Sum of arrays axis = 0
print()
print ("Sum of arrays , axis = 0")
n1= np.array([10,20,30,40,50])
n2= np.array([40,50,60,70,80])
np.sum([n1,n2],axis=0)
print(n1)

# Sum of arrays axis = 1
print()
print ("Sum of arrays , axis = 1")
n1= np.array([10,20,30,40,50])
n2= np.array([40,50,60,70,80])
np.sum([n1,n2],axis=1)
print(n1)

# Aritmatic Ops on Array
print()
print ("Aritmatic Ops on Array")
n1= np.array([10,20,30,40,50])
print(n1)
n2 = n1+1
print(n2)
n3= n1-1 
print(n3)
n4 = n1*2
print(n4)
n5 = n1 /2
print(n5)

# Mean of an Array
print()
print ("Mean of an Array")
n1= np.array([10,20,30,40,50])
np.mean(n1)


# Median of an Array
print()
print ("Median of an Array")
n1= np.array([10,20,30,40,50])
np.median(n1)

# Standard Deviation of an Array
print()
print ("Standard Deviation of an Array")
n1= np.array([10,20,30,40,50])
np.std(n1)



