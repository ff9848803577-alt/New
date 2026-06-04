# and: returns ture if both statements are true 
# or: returns true if at least one of them is true
# not: reverse the result

a = 10
b = 13
c = 12

if(a>b and a>c):
    print("Both are true")


if (a>b or a>c):
    print("At least one is true")


if not a>b:
    print("a is not greater than b")

# Combining multiple operators

age = 24
is_student = False
has_discount_code = True

if(age<18 or age>65) and not is_student or has_discount_code:
    print("Discount granted")