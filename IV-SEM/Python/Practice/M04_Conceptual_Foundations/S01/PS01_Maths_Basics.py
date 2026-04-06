# gcd using traditional ,method
'''import math
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=min(a,b)
d=1
for i in range(1,c+1):
    if a%i==0 and b%i==0:
            d=i
print(d)
#using math.gcd
print(math.gcd(a,b))'''

#lcm 
'''import math


x=int(input())
y=int(input())
z=max(x,y)
while True:
    if z%x==0 and z%y==0:
        print(z)
        break
    z+=1
import math
print(math.lcm(x,y))'''
#perfect number
'''n=int(input())
m=0
for i in range(1,n//2+1):
    if n%i==0:
        m+=i 
if m==n:
    print("perfect number")
else:
    print("Not a perfect number")'''
#amstrong number 
k=int(input())
b=str(k)
a=len(b)
c=0
for i in range(a):
    c+=int(b[i])**a 
if c==k:
    print("Amstrong")
else:
    print("Not Amstrong")
