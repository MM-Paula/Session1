print('1. Reverse the order of the items in an array.')
a=[1,2,3,4,5]
print(a)
a.reverse()
print(a)
print()
print('2. Get the number of occurrences of var b in array a.')
a=[1,1,2,2,2,2,3,3,3]
print(a)
b=2
print(b)
a.count(2)
print('The number of occurrences of var b in array a is:')
print(a.count(2))
print()
print('3. Given a sentence as string, count the number of words in it.')
a='Ana are mere si nu are pere'
print(a)
res=len(a.split())
print ('The number of words in string are: ' + str(res))
