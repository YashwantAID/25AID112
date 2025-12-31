##Create a variable with your favourite number.
##Print whether this number is even or odd (use % operator).

favourite_number = int(input("Enter your favourite number: "))
if favourite_number % 2 == 0:
    print(favourite_number, "is an even number.")
else:
    print(favourite_number, "is an odd number.")