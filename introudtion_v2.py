ask = input("Have you played the game before? ").lower()
valid = False

while not valid:
    if ask == "yes" or ask == "y":
        print("Launch game")
        valid = True
    elif ask == "no" or ask == "n":
        print("Show instructions")
        valid = True
    else:
        print("You must enter Yes or No")
        ask = input("Have you played the game before? ").lower()
