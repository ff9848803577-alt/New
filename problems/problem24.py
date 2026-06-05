# WAP to find whether the given number is prime or not

n = int(input("Enter a number:"))

for i in range(2, n):
    if(n%i) == 0:
        print("Not a prime")

else:
    print("It is prime ")

 