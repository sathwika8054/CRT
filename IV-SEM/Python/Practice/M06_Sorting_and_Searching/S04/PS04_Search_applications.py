def Loweer_bound(li,x):
    left=0
    right=len(li)-1
    while left<=right:
        mid=(left+right)//2
        if li[mid]<x:
            left=mid+1
        else:
            right=mid-1

    return left

print(Loweer_bound([10,15,23,27,30,35,36],25))
print(Loweer_bound([10,15,23,27,30,35,36],33))
print(Loweer_bound([10,15,23,27,30,35,36],40))
