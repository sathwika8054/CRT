def fact(a):
    if a<0:
        return "no factorial"
    elif a==0 or a==1:
        return 1
    else:
        fact=1
        for i in range(1,a+1):
            fact=fact*i
        return fact
a=int(input())
s=0
for j in str(a):
    s+=fact(int(j))
print("Strong Number" if s==a else "Not Strong")
