ask = input("Have you played the game before? ").lower()

if ask == "yes" or "y":
    print("Launch Game")
elif ask == "no" or "n":
    print("Show instructions")
else:
    print("You must enter Yes or No")
