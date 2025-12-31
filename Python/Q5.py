##Ask user for two numbers (as strings), convert them to integers, then print:
##their sum
##their difference
##their product
##which one is bigger (or if they are equal)
A = int(input("Enter the first number: "))
B = int(input("Enter the second number: "))
sum = A + B
difference = A - B
product = A * B
print("Sum:", sum)
print("Difference:", difference)
print("Product:", product)
if A > B:
    print("Number A is bigger.")
elif B > A:
    print("Number B is bigger.")
else:
    print("Both numbers are equal.")