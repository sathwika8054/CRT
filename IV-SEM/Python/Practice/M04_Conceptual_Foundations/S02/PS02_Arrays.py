#Revese the array elements
'''
input:[12,45,36,78]
output:[78,36,45,12]
'''
l=[12,45,36,78]
r_l=[]
for i in range(-1,-(len(l)+1),-1):
    r_l.append(l[i])
print(r_l)
print([l[i] for i in range(-1,-1*(len(l)+1),-1)])
r_l=[]
for ele in l:
    r_l=[ele]+r_l
print(r_l)
#check the array is sorted or not 
'''li=list(map(int,input("Enter the array: ").split()))
print(li==sorted(li)[::-1])'''
def check_array(nums):
    for i in range(len(nums)-1):
        if nums[i]>nums[i+1]:
            return False
    return True
print(check_array([12,45,78,96,100]))
'''def check_array_sorte(nums):
    asc=True
    dec=True
    for i in range(len(nums)-1):
        if nums[i]>nums[i+1]:
            asc=False
        if nums[i]<nums[i+1]:
            dec=False
    return asc or dec
# decending order
print(check_array_sorte([12,45,78,96,100]))'''
