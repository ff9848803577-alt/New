f = open("file.txt")

lines = f.readlines() # readlines returns a list and readline readline is used to read single lines specifically 

print(lines, type(lines))

line1 = f.readline()
print(line1, type(line1))

line2 = f.readline()
print(line2, type(line2))

line3= f.readline()
print(line3, type(line3))

line4 = f.readline()
print(line4, type(line4))
# there's nothing in the fourth line in file.txt so it showed an empty string 

f.close

# readline reads all the lines until it finds an empty string 