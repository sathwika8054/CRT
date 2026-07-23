def Digital_sum(a):
    if a<10:
        return a
    b=sum([int(ch) for ch in str(a)])
    return Digital_sum(b)
print(Digital_sum(386))

def is_sorted_array(nums):
    return sorted(nums)==nums

    pass
print(is_sorted_array([10,20,30,40,50]))
print(is_sorted_array([10,2,30,15,50])) 
