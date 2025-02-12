# Main.py

# Dependencies
import Characters.Thrawn
import Characters.Vader
from Characters.Thrawn import Manipulate, Fracture
from Characters.Vader import Terrifying_Swing, Force_Crush

# Metadata
version = "1.0.0"
chosen_character = ""

print("Star Wars Galaxy of Heroes in Terminal\nBy D4LM")
print(version)

print("Who do you want to play as?")
print("1.Grand Admiral Thrawn\n2.Darth Vader")
choice=int(input())

if choice == 1:
    print("You have chosen to play as Grand Admiral Thrawn")
    chosen_character = "Grand Admiral Thrawn"
elif choice == 2:
    print("You have chosen to play as Darth Vader")
    chosen_character = "Darth Vader"
else:
    print(choice)
    print("Invalid choice. Please try again.")
    exit(1)

# The match
print(f"The match begins! {chosen_character} vs Damage Reader Bot!")
print("Available moves:")
if chosen_character == "Grand Admiral Thrawn":
    print("1. Manipulate")
    print("2. Fracture")
    chosen_move = int(input())
    if chosen_move == 1:
        print(f"Grand Admiral Thrawn uses Manipulate, dealing {Manipulate()} damage.")
    elif chosen_move == 2:
        print(f"Grand Admiral Thrawn uses Fracture, dealing {Fracture()} damage.")
    else:
        print("Invalid move. Please try again.")
        exit(1)
elif chosen_character == "Darth Vader":
    print("1. Terrifying Swing")
    print("2. Force Crush")
    chosen_move = int(input())
    if chosen_move == 1:
        print(f"Darth Vader uses Terrifying Swing, dealing {Terrifying_Swing()} damage.")
    elif chosen_move == 2:
        print(f"Darth Vader uses Force Crush, dealing {Force_Crush()} damage.")
    else:
        print("Invalid move. Please try again.")
        exit(1)