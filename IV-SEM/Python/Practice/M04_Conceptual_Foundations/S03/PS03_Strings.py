'''
Strings
String creation
acceing character
slicing
immutable
'''
'''def Reverse_string(s):
    a=""
    for i in range(len(s)-1,-1,-1):
        a+=s[i]
    return a
    pass
s=input()
print(Reverse_string(s))
b=input()
print(b[::-1])
h="".join(reversed(s))
if '''
'''def is_palindrome(a):
    b="".join(reversed(a))
    return a==b
print(is_palindrome("aabbaabbaa"))'''
def  freq_count(s):
    freq={}
    for ch in s:
        if ch not in freq:
            freq[ch]=1
        else:
            freq[ch]+=1
    return freq
def Anagrams(s1,s2):
    return freq_count(s1)==freq_count(s2)
    pass
print(Anagrams("paces","space"))
print(Anagrams("abs","aabbcc"))
import collections
def Anagrams(s1,s2):
    return collections.Counter(s1)==collections.Counter(s2)
    pass
print(Anagrams("paces","space"))
print(Anagrams("abs","aabbcc"))



