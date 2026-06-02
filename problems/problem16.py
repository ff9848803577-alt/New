#  WAP to detect spam comment 

p1 = "Make alot of money"
p2 = "Subscribe to my channel"
p3 = "Click here to earn money"
p4 = "Buy now! Limited time offer!"

message = input("Enter your comment:")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("this is a spam")

else:
    print("This is not a spam")

# here 'in' is a keyword which is use to check whether the string is present in the message or not. It returns a boolean value True or False.