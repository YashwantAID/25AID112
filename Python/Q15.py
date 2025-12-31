##Create list = [12, 45, 3, 98, 7, 34, 21].
##Use a loop to: a) print each number b) print only numbers greater than 30 c) count how many numbers are greater than 30

List = [12, 45, 3, 98, 7, 34, 21]    
count = 0
for i in List:
    print(i)
for i in List: 
    if i > 30:
        print(i, "is greater than 30")
        count += 1
print("Total numbers greater than 30:", count)           


