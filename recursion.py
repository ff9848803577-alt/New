# Recursion means a function calls itself.
# Instead of using a loop, the function keeps calling itself to solve smaller versions of the same problem.

n = int(input("Enter a number:"))

def factorial(n):
    if(n==0 or n==1 ):
        return 1
    return n * factorial(n-1)

print(f" The factorial of this number is:{factorial(n)}")

# another eg:
def count(n):
    if n == 6:
        return
    print(n)
    count(n+1)

count(1)