a=10
b="Sathwika"
c=3.454
print(hash(a))
print(hash(b))
print(hash(c))

size=7
table=[None]*size
a=[10,20,30]
for key in a:
    hash_key=key%size 
    table[hash_key]=key
print(table)
