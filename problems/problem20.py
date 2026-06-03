# WAP to find whether a given post is talking about Bikki or not

post = input("Enter your post:")

if("Bikki".lower() in post.lower() ): # we use.lower to ignore capital and small
    print("Yes this post is talking about Bikki")

else:
    print("No this post is not talking about Bikki")


#Note: here the capital and small matters so we use lower() to ignore the capital and small letters.