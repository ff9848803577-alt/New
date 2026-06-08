principle = 0
rate = 0
time = 0

while principle <= 0 :
    principle = float(input("Enter the principle amount:"))
    if principle<=0:
        print("Princple cant be less than or equal to zero")

while rate <= 0:
    rate = float(input("Enter your rate: "))
    if rate <= 0:
        print("Rate cant be less or equal to zero ")

while time <= 0:
    time = float(input("Enter yout time:"))
    if time <= 0:
        print("Time can be less or equal to zero")

interest  = (principle * time * rate) / 100 
total = interest + principle
print(f"Your total compound interest after {time} year is:{interest:.2f} $")
print(f"And your total balance after {time} year is: {total} $")

