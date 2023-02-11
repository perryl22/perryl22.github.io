#choose your own adventure

#Introductory Message
print("You are hiking in the mountains and you find an abanded mansion. You decide to go in and explore. On the front door there's a sign that says:")
print(" THE TREASURE BEHIND THESE DOORS IS NOT WORTH THE TROUBLE.")
go = input("PLAYER, your goal is to survive the mansion and come out with the treasure. Do you want to continue?")
if go == "yes"or go == "yes":
    print("Excellent. You are ready to begin.")
else: 
    print("GAME OVER")
    exit()

print("You walk in and find and entry with a grand staircase. There is also a hallway to your left, but you hear music coming from there.")
stairs = input("Would you like to go up the stairs or in the hallway?")
if stairs == "stairs" or stairs == "Stairs" or stairs == "upstairs" or stairs == "up the stairs" or stairs == "Upstairs" or stairs == "Up the stairs":
    print("You walk slowly up the stairs, trying not to make a sound. When you walk up there are three doors. They each have a sign on them.")
else: 
    print("GAME OVER. You chose to go down the hallway, which was booby trapped. You died.")
    exit()

print("The signs on the door are:   ")
print("Door 1: Zoo")
print("Door 2: Greenhouse")
print("Door 3: Office")

doors = input("Do you want to go through door 1, 2, or 3?   ")
if doors == "1":
    print("GAME OVER. You found a savage tiger behind door 1, and you died.")
    
if doors == "2":
    print("GAME OVER. You found a poisonous plant that touched you as soon as you opened the door. You died.")
else: 
    print("You walk in the bedroom and find an old chest on the desk. You have found the treasure.")
    exit()