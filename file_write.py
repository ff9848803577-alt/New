st = "Hello Bikki!!"

f = open("myfile.txt", "w") # w mode for write only 

f.write(st)

f.close()

# r = open for reading 
# a = open for appending(add something)
# + = open for updating
# 'rb'  = will open for read in binary mode 
# 'rt' = will open for read in text mode 