# wAP to accept marks of seven students in a list and print the marks in sorted order

marks = []


f1 = input("Enter the marks of student:")
marks.append(f1)
f2 = input("Enter the marks of student:")
marks.append(f2)
f3 = input("Enter the marks of student:")
marks.append(f3)
f4 = input("Enter the marks of student:")
marks.append(f4)
f5 = input("Enter the marks of student:")
marks.append(f5)

print("marks of stundents in sorted order:", sorted(marks))
# this is for sorted order but this is in the form of string because we have taken input in string form
# if we want to take input in integer form then we have to use int() function while taking input

print(marks)
#this will show as it is without sorted order