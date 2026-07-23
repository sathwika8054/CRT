#4 first non-repeating element
#5 count Occurance of Each Character in String
a="sathwika"
freq={}
for ch in a:
    freq[ch]=freq.get(ch,0)+1
print(freq)