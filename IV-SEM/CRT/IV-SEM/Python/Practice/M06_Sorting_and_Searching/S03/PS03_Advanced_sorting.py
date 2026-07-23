def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left =arr[:mid]
    right=arr[mid:]
    left_sorted=merge_sort(left)
    right_sorted=merge_sort(right)
    return merge_fun(left_sorted,right_sorted)
def merge_fun(left,right):
    i,j=0,0
    res=[]
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    res.extend(left[i:])
    res.extend(right[j:])
print(merge_fun([7,14],[3,12]))


def qucik_sort(arr,low,high):
    pivot=arr[low]
    i,j=low+1,high
    while True:
        while i<=j and arr[i]<=pivot:
            i+=1
        while i<=j and arr[j]> pivot:
            j-=1
        if i<=j:
            arr[i],arr[j]=arr[j],arr[i]
        else:
            break
    arr[low],arr[j]=arr[j],arr[low]
    return j
print(qucik_sort([14,7,3,2],0,3))
def Qucik_sort(arr,low,high):
    if low<high:
        p=Partition(arr,low,high)
        Qucik_sort(arr[:p],low,p-1)
        Qucik_sort(arr[p:],p+1,high)
    return arr
print(qucik_sort([14,7,3,2],0,3))

