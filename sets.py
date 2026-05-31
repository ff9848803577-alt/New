# set is collection of unique items
# no repetition allowed in set
# set is unordered collection of items so if we need order we can use list or tuple
# rhere is no way to change the items in the sets
#sets cant contain duplicate values
# sets are unindexed so we cant access the items in the set by index

s = { 1, 5, 5, 67} # here 5 will be stored only once because set does not allow repetition

e = set() # this is empty set, dont use {} it will create an empty dictionary

print(type(s))

# Here are some methods of set:

s.add(566)
print(s, type(s))

len(s) # to find the length of the set
print(len(s))

s.remove(5)
print(s)

s.pop() # it will remove a random item from the set
print(s)

s.clear() # will remove all items
print(s)

s1 = { 1, 2, 4}
s2 = { 3, 4, 5}

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2)) # will return the items that are in s1 but not in s2
print(s1.symmetric_difference(s2)) # will return the items that are in s1 or s2 but not in both     
print(s1.issubset(s2)) # will return true if s1 is subset of s2
print(s1.issuperset(s2)) # will return true if s1 is superset of s2
print(s1.isdisjoint(s2)) # will return true if s1 and s2 have no common items
print(s1.copy()) # will return a copy of the set
