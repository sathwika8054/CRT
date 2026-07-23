#bubble sort
def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

    pass
print(bubble_sort([12,5,25,10,30]))

#selection sort
def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_ind=i
        for j in range(i+1,n):
            if arr[j]<arr[min_ind]:
                min_ind=j
        arr[i],arr[min_ind]=arr[min_ind],arr[i]
    return arr
print(selection_sort([12,5,25,10,30]))

#insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
print(insertion_sort([12,5,25,10,30]))

