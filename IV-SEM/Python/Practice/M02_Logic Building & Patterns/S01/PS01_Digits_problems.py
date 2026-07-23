'''nt(input("Enter a number:"))
print("Number of digits in the number is:",len(str(a)))
count=0
while a>0:
    count+=1
    a=a//10
print(count)
#input=1565
#output=17
n=int(input("Enter a number:"))
temp=n
d=str(n)
l=[]
for i in range(len(d)):
    l.append(int(d[i]))
print(sum(l))
#method 2
c=0
while n>0:
    digits=n%10
    c+=digits
    n=n//10
print(c)
#method 3
print(sum(map(int,str(temp))))
#input=12345
#output=2 3
b=int(input( "Enter a number:"))
ev=0
od=0
while b>0:
    di=b%10
    b//=10
    if di%2==0:
        ev+=1
    else:
        od+=1
print(ev,od)

#input=546
#output=6
d=int(input("Enter a number:"))
while d>9:  
    d=sum(map(int,str(d)))
print(d)
'''
#input=12345
#output=54321
e=int(input("Enter a number:"))
rev=""
while e>0:
    rev+=str(e%10)
    e//=10
print(int(rev))
#7,43
