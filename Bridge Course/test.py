import numpy as np
print()
print("1 D Array")
l1= [10,20,30,40,50]
n1=np.array(l1)
print(n1)

print()
print("2 D Array")
l1= [[10,20,30],
     [40,50,60],
     [70,80,90]]
n1=np.array(l1)
print(n1)

print()
print("Multi dimensional array filled with 0")
n1=np.zeros([5,5])
print(n1)

print()
print("Single dimensional array initlaized with a range")
n1=np.arange(10,20)
print(n1)

print()
print("Single dimensional array initlaized with a random")
n1=np.random.randint(1,100,5)
print(n1)

print()
print("Vertical Stack")
n1=np.array([10,20,30])
n2=np.array([11,12,13])
print(np.vstack((n1,n2)))

print()
print("horizontal Stack")
print(np.hstack((n1,n2)))

print()
print("Column Stack")
print(np.column_stack((n1,n2)))

print ()
print ("Intersection between two arrays")
n1=np.array([10,20,30,40,50])
n2=np.array([11,12,13,40,50])
print(np.intersect1d(n1,n2))

print()
print("Difference between two arrays ")
print("n1-n2")
n1=np.array([10,20,30,40,50])
n2=np.array([11,12,13,40,50])
print(np.setdiff1d(n1,n2))
print("n2-n1")
print(np.setdiff1d(n2,n1))

print()
print("Sum of two arrays")
n1=np.array([10,20,30,40,50])
n2=np.array([11,12,13,40,50])
print(np.sum([n1,n2]))
print()
print("On Axis 0")
print(np.sum([n1,n2],axis=0))
print(np.sum([n2,n1],axis=0))
print()
print("On Axis 1")
print(np.sum([n1,n2],axis=1))

print()
print("Arithematic Ops on Array")
n1=np.array([10,20,30,40,50])
print("Addition")
print(n1+1)
print("Subtraction")
print(n1-2)
print("Multiplication")
print(n1*5)
print("Division")
print(n1/2)
print("Modulo")
print(n1%3)
print("Power")
print(n1**2)

print()
print("Mean of an Array")
n1=np.array([10,20,30,40,50])
print(np.mean(n1))

print()
print("Median of an Array")
n1=np.array([10,20,30,40,50,60])
print(np.median(n1))

print()
print("Standard Deviation of an Array")
n1=np.array([10,20,30,40,50])
print(n1)
print(np.std(n1))
print()
n1=np.array([10,20,30,40,50,60])
print(n1)
print(np.std(n1))



import pandas as pd 
print()
print("Importing Pandas and Creating a series")
s1=[1,2,3,4,5]
print(pd.Series(s1))

print()
print("Chnaging Index of Series")
s1=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(s1)
print()
s2=pd.Series([1.0,2.0,3.0,4.0,5.0]
             ,index=['a','b','c','d','e'])
print(s2)
print()
s3=pd.Series(['Alex','Ben','Clark','Doe','Emily']
             ,index=['a','b','c','d','e'])
print(s3)
print()
s4=pd.Series([[1,1,1],[2,2,2],[3,3,3],[4,4,4],[5,5,5]]
             ,index=['a','b','c','d','e'])
print(s4)
print()
s5=pd.Series([[1,1,1],[2.0,2.0,2.0],['a','b','c']
              ,[4,4,4],[5,5,5]]
             ,index=['a','b','c','d','e'])
print(s5)
print()
s6=pd.Series([1,2.0,'a'])
print(s6)

print()
print("Indexing")
s1=pd.Series(['Alex','Ben','Clark','Doe','Emily'])
print(s1)
print(f"Enter Indexing Value at 3 : {s1[3]}")
print(f"Enter Negative Indexing Value at 3 : {s1.iloc[-3]}")

print()
print("Series of Dictionary")
s1=pd.Series({'Name':['Alex','Ben','Clark'],
              'Marks':[90,60,70]})
print(s1)
print()
print("Dataframe of Dictionary")
s1=pd.DataFrame({'Name':['Alex','Ben','Clark'],
              'Marks':[90,60,70]})
print(s1)


