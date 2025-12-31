##Create 4 variables of different data types (integer, float, string, boolean) that describe yourself (age, height, name, are_you_student). Print all of them with nice formattin
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))
name = input("Enter your name: ")
are_you_student = input("Are you a student? (yes/no): ")
print("Name:", name)
print("Age:", age)         
print("Height:", height, "meters")  
if are_you_student.lower() == 'yes':
    print("Student: True") 
else:
    print("Student: False")
