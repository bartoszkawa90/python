print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,.% .%`` %``, `"-._"-._   ". '__|___________________
          |           |o`"=._` %,% "%` %`;.%".,  "-._"-._;;              |
 _________|___________| ;`-.o`"=._; %."% `% '`."\` . "-._/_______________|_______
|                   | |o;    `"-.o`"=._`` %`% " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

side_choise = input("You are at a cross road.Where do you want to go? Type 'left' ot 'right'.\n")
if side_choise == "right" :
    print("You fall in to the hole. Game over")
elif side_choise == "left":
    lake_choise=input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
    if lake_choise=="swim":
        print("You are attacked by a trout . Game over")
    elif lake_choise=='wait':
        door_choise=input("You arrive at the island unharmed. There is a hause with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
        if door_choise=="red":
            print("You were burned by fire . Game over")
        elif door_choise=="yellow":
            print("You win")
        elif door_choise=="blue":
            print("You have been eaten by beasts . Game over")
        else:
            print("Game over")
    elif lake_choise=="I'll pass and go somewhere else":
        print(" +1 , Bye good luck and have fun")
    else:
        print("Error . You did something wrong")
else:
    print("Error . You did something wrong")
