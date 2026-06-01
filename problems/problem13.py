# create an empty dictionary and allow 4 frn1s to entre their fav language as value and use key as their names. assume that the names are  unique

f = {}
name = input("Enter the name of frn1:")
lang = input("Enter the fav language of frn1:")
f.update({name: lang})

name = input("Enter the name of frn2:")
lang = input("Enter the fav language of frn2:")
f.update({name: lang})

name = input("Enter the name of frn3:")
lang = input("Enter the fav language of frn3:")
f.update({name: lang})

name = input("Enter the name of frn4:")
lang = input("Enter the fav language of frn4:")
f.update({name: lang})


print(f)
#note: if any two names are the same then the value that is added last will be updated and replace the previous value but the value can be same
#note: we cant change the value inside a list which is contained in a set
# eg. s = { 1, 2, 4. "bikki", [8, 9]} # this is not possible because we cant change the value inside a list which is contained in a set. and its not possible to have a list inside a set because list is mutable and set is immutable. but we can have a tuple inside a set because tuple is immutable and set is immutable. eg. s = { 1, 2, 4. "bikki", (8, 9)} # this is possible because we can change the value inside a tuple which is contained in a set. and its possible to have a tuple inside a set because tuple is immutable and set is immutable.