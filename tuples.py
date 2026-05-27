#tuple is a data type that is immutable basically its like list but list is mutable 

a = (1, 2, 3, 4, 5) # tuple ma element change garna mildaina
print(type(a)) # it is tuple

b = () # this is empty tuple 
print(type(b))

c = (1,) # this is tuple with one element
print(type(c))
 
d = ( 1, 3, 35, False, "rohan")
d[0] = 100 # tuple ma element change garna mildaina so this will give error 
print(d)
