'''a=[1,2,3,4,5]
b=[]
for i in range(len(a)):
    b.append(a[i]*2)
print(b)

li1=['a','b','c','d','e']
res=""
print(''.join(li1))
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):3
    print(" "* (n-i) + "* " * i)'''
# inverted pyramid

'''n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
for i in range(n-1,0,-1):
    print(" "*(n-i)+"* "*i)'''
'''1
  1 2 
1  2  3
'''
'''n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+" ".join([str(j) for j in range(1,i+1)]))
for i in range(1,n+1):
    print(" "*(n-i)+" ".join([str(i) for j in range(1,i+1)]))'''
'''
A
B C 
D E F
G H I J'''
n=int(input())
val=65
for i in range(n):
    for j in range(i+1):
        print(chr(val),end=" ")
        val+=1
    print()


    
          