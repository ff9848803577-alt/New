# WAP to read a text frrom a given file file.txt and findout whether it contains the word "Twinkle"

f = open("file.txt")

content = f.read()
if("twinkle" in content):
     print("The word twinkle is present in the content")
                        

else:
     print("The word twinkle is not present in the content")
    

f.close()
