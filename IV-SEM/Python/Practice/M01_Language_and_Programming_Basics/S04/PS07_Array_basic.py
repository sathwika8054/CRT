import array
arr=array.array('i',[])
print(arr,type(arr))
arr.append(10)
arr.append(30)
arr.append(44)
arr.append(34455)
print(arr)
'''List:
1. use [] to create a list
2.list is Mutable
3.list allows duplicates
4.list is heterogeous 
5.list is indexed'''
li=[1,2,3,4,5,6,7,"A",'Hello','World',22333.33]
print(li,type(li))
print(li[3])#using specific index
print(li[8:11:1]) #slice
print(li[::-1])#reverse
print(len(li))#length
li.append(30)#adds element at the end
li.insert(2,24)# adds element using specific index
li.pop(4)#removes the given element from the list 
li.remove(7)#remove the given element from the list
li.insert(20,3333)
li.count(1)
print(li)
"read a number from the user and display no.of digits in the number"
n=int(input())
print(len(str(n)))