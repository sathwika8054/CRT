def array_sum(a):
    b=0
    for i in a:
        b+=i
    return b

    pass
print(array_sum([1,2,3,4,5]))
def array_sum_recu(a,i):
    if i==0:
        return 0
    return a[i-1]+array_sum_recu(a,i-1)
    pass
print(array_sum_recu([1,2,3,4,5],5))

def array_sum2(a):
    if len(a)==0:
        return 0
    return a[-1]+array_sum2(a[:-1])
print(array_sum2([1,2,3,4,5]))

def reverse_string(string):
    if string=="":
        return ""
    return string[-1]+reverse_string(string[:-1])    
print(reverse_string("aaaabb"))