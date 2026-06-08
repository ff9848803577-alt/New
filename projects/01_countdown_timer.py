import time

time.sleep(3)

print("Time's up!")

# for countdown
import time
my_time = int(input("Enter time in second:"))

for x in range(0, my_time):
    print(x)
    time.sleep(2)

print("TIME'S UP!")

# for countdown in reverse

import time
my_time = int(input("Enter time in second:"))

for x in reversed(range(0, my_time)):
    print(x) # x is counter
    time.sleep(2)

print("TIME'S UP!")

# for digital clock 

import time
my_time = int(input("Enter time in second:"))

for x in range( my_time, 0, -1):
    seconds = x % 60
    minutes = int(x/60) % 60
    hours = int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}") 
    time.sleep(1)

print("Time's Up!")
