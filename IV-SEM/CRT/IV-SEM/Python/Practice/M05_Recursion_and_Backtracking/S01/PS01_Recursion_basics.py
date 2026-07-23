#sum n natural numbers

''''def natural_num(n):
    return (n*(n+1))//2
print(natural_num(5))
print(natural_num(10))'''
'''def natural_sum(n):
    s=0
    for i in range(n,0,-1):
        s+=1
    return s
print(natural_sum(5))
print(natural_sum(10))'''
'''def natural_sum1(n):
    if n==1:
        return 1
    return n+natural_sum1(n-1)
print(natural_sum1(5))
print(natural_sum1(10))'''
# n factorial
def num_factorial(n):
    a=1
    if n==0:
        return 1
    else:
        for i in range(1,n+1):
            a*=i
        return a
print(num_factorial(0))
def num_factorial1(n):
    if n<0:
        return "Factorial doesnot exist for -ve"
    elif n==0 or n==1:
        return 1
    else:
        return n*num_factorial1(n-1)
print(num_factorial1(3))
def fibonaci(n):
    if n<=0:
        return "Fibonaci doesnot exits for -ve"
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonaci(n-2)+fibonaci(n-1)
print(fibonaci(4))
def gcd_of_two_num(n,m):
    if m==0:
        return n
    return gcd_of_two_num(m,n%m)
print(gcd_of_two_num(4,10))



