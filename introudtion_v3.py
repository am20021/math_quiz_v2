print("Welcome to Math Quiz!")

ask = input("Have you played the game before? ").lower()
valid = False


def instructions():
    print("\n*** How to Play ****")
    print("\nInstructions Here")


while not valid:
    if ask == "yes" or ask == "y":
        print("Launch Game")
        valid = True
    elif ask == "no" or ask == "n":
        instructions()
        valid = True
    else:
        print("You must enter Yes or No")
        ask = input("Have you played the game before? ").lower()
