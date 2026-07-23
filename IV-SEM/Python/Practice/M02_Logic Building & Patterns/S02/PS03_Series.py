''' Armstrong Number
n=int(input("Enter the value :"))
count=len(str(n))
a=0
for i in str(n):
    a+=int(i)**count
print("Armstrong Number"if a==n else "Not an Armstrong Number")'''
'''m=int(input("Enter a value:"))
b=0
for i in range(1,(m//2)+1):
    if m%i==0:
        b+=i
print("Perfect number" if m==b else "Not Perfect Number")'''
'''Strong number'''
'''import math
o=int(input("Value:"))
c=0
for i in str(o):
    c+=math.factorial(int(i))
print("Strong number" if c==o else "Not Strong Number")'''
