##Create a simple traffic light simulator:
##Ask user to enter "red", "yellow" or "green".
##Print appropriate action:
##red → "STOP!"
##yellow → "Prepare to stop"
##green → "You can go"
##anything else → "Wrong input!"

traffic_light_color = input("Enter the traffic light color (red, yellow, green): ").lower()
if traffic_light_color == "red":
    print("STOP!")  
elif traffic_light_color == "yellow":
    print("Prepare to stop")
elif traffic_light_color == "green":    
    print("You can go")
else:
    print("Wrong input!")
