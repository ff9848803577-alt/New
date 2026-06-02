#WAP to find our whether the student passed or failed if it requires 40% total percentage and 33% in each subject. Assume 4 subjects

marks1 = int(input("Enter the marks of subject 1:"))
marks2 = int(input("Enter the marks of subject 2:"))
marks3 = int(input("Enter the marks of subject 3:"))
marks4 = int(input("Enter the marks of subject 4:"))

total_percentage = (marks1 + marks2 + marks3 + marks4)/400*100

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33 and marks4>=33):
    print("Passed")

else:
    print("Failed")