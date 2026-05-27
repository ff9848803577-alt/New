name = "bikki is good good boy"

print(len(name))

print(name.endswith("kki"))

print(name.startswith("Bi"))

print(name.capitalize())  #capatalizes only starting character

print(name.upper()) #capatalizes all characters

print(name.lower()) #makes all character small

print(name.find("good")) #finds the index of first occurance of the substring 

print(name.replace("good","bad")) # replaces the substring with the new string and returns a new string but does not change the original string

print(name) #here original sting is not changed because string is immutable in python

print(name.replace("good","bad",1)) # here 1 is the count of how many times we want to replace the substring if we want to replace all the occurance then we can omit the count parameter
