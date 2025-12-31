##Ask user for their age. Print different messages:
##< 13 → "You are a child"
##13–17 → "You are a teenager"
##18–64 → "You are an adult"
##≥ 65 → "You are a senior"
age = int(input("Enter your age: "))   
if age < 13:
    print("You are a child.")
elif 13 <= age <= 17:
    print("You are a teenager.")    
elif 18 <= age <= 64:
    print("You are an adult.")
elif age >= 65:
    print("You are a senior.")
