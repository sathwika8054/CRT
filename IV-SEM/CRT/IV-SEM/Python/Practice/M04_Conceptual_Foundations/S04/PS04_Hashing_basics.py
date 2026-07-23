'''#brutforce approach
def two_sum(nums,t):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==t:
                return [i,j]
    pass
nums=list(map(int,input().split()))
t=int(input())
print(two_sum(nums,t))'''
def two_sum(nums,t):
    d={}
    
    pass

