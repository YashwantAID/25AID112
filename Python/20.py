##Shopping list manager" mini-project: Start with empty list. Keep asking user what to do in a while loop:
##"add" → ask for item name and add to list , "remove" → ask which item to remove (by name).
##"show" → print current shopping list , "quit" → exit the program , (use if-elif inside while loop)

list = []  
i = 0
while i == 0:
    function = input("What do you want to do? (add/remove/show/quit): ")
    
    if function == "add":
        a = input("Enter the item to add: ")
        list.append(a)
        print("The item " , a , " has been added to the shopping list.")  

    elif function == "remove":
        b = input("Enter the item to remove: ")
        if b in list:
            list.remove(b)
            print("The item " , b , " has been removed from the shopping list.")
        else:
            print(" is not in the shopping list.")

    elif function == "show":
        print("Current shopping list:")
        print(list)

    elif function == "quit":
        print("Exiting the shopping list manager")
        i += 1
        
    else:
        print("Invalid action. Please choose from add, remove, show, or quit (in lowercase).")

    
