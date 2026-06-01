# can we have a set with 18 as int and '18' as string as a value in i?/
 
s = set()
s.add(18)
s.add('18')

print(s)
print(len(s))

v = set()
v.add(14)
v.add(14.0)
v.add('14')
print(len(v)) # here the length will be 2 bcz in python it checks the value not the data type. since 14 and 14.0 has same value so only one value will be stored  in the set 
