# To delete any file, you must import the os module and run its os.remove() function 

import os 
os.remove("demofile.txt")

# To delete the entire folder, use os.rmdir() method

import os
os.rmdir("myfolder") # Note: only the empty folder gets removed 

# To check whether the file exixts:

import os 
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")

else:
    print("The file doesnt exist!")