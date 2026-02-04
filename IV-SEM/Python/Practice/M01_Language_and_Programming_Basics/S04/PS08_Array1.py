import numpy as np

arr=np.array([10,20,30,40,50])
print("original array:",arr)
print(np.max(arr))
print(np.min(arr))
print(np.mean(arr))
print(np.sum(arr))
print(np.zeros(5))
print(np.ones(8))
print("Even numbers are:",np.arange(2,10,2))
print("Odd numbers are:",np.arange(1,10,2))
n=int(input("Enter the size"))
ele=list(map(int,input("Enter the elements:").split()))
print("Array ")


