'''
f = open("file.txt")
print(f.read())
f.close() 

'''
# The same thing can be written using with statement like:

with open("file.txt") as f:
    print(f.read())

# dont have to explicitly close the file 