print("Welcome to Math Quiz!")

ask = input("Have you played the game before? ").lower()
valid = False


def instructions():
    print("\n*** How to Play ****")
    print(
        "\n- A question relating to the times tables will be asked.\n- Example: 9x9\n- A correct answer will grant you 5 points.\n- An incorrect answer will take away 10 of your points.")
    print(
        "- Depending on game length selected the number of questions asked will be different.\n- Short game = 5 questions, Medium = 10, Long = 15")


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

length = input("\nWhat game length would you like to play(short, medium, long)? ").lower()
if length == "short":
    questions = 5
    print(questions)
elif length == "long":
    questions = 15
    print(questions)
else:
    questions = 10
    print(questions)
