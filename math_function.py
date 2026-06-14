# Python has a set of built-in math functions, including an extensive math module, that allows you to perform mathematical tasks on numbers.

# Python has built in math module called math by which we can use the methods and constants of the module 

import math # we must import the module first of all 

# The math.sqrt() returns the square root of a number 

import math 

j = math.sqrt(64)
print(j)


# The math.ceil() rounds a number upwards to its nearest integer 
# The math.floor() rounds a number downwards to its nearest integer

import math 

d = math.ceil(1.4)
f = math.floor(1.4)

print(d)
print(f)


# The math.pi constant retunrs the value of pi 

import math 

c = math.pi 

print(c)

# The min() and max() functions are used to find the lowest and the highest value in an iterable 
  
x = min(4, 10, 100)
y = max(9, 100, 890)

print(x)
print(y)


# The abs() function returns the absolute(positive) value of the specified number

z = abs(-5.89)
print(z)


# The pow(x, y) function returns the value of x to the power of y 

i = pow(4, 3)
print(i)

