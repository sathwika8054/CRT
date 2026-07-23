#two methods
# sequential searching (linear search)
#best case O(1) average case- O(n) Worst case- O(n) Time complexcity
'''def Linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
li=list(map(int,input().split()))
tar=int(input())
print(Linear_search(li,tar))'''

# binary search
def binary_search(nums,target):
    nums.sort()
    left =0
    right=len(nums)-1
    while left<=right:
        mid =(left+right)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1
nums=list(map(int,input().split()))
target=int(input())
print(binary_search(nums,target))
