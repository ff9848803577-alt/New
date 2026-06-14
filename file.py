# A file is data stored in a storage device. RAM is volatile and fastest so we dont use it, we use any other non volatile storage device
# A python program can talk to the file by reading content from it and writing content to it 

f = open("file.txt")
data = f.read()

print(data)
f.close()