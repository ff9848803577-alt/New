# Recursion is 
n = int(input("Enter a number:"))

def factorial(n):
    if(n==0 or n==1 ):
        return 1
    return n * factorial(n-1)

print(f" The factorial of this number is:{factorial(n)}")