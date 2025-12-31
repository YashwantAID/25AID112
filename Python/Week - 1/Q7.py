##Ask user for a number. Tell them if the number is:positive,negative,zero

number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive.")    
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
