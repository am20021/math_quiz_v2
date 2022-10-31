import random

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
        valid = True
    elif ask == "no" or ask == "n":
        instructions()
        valid = True
    else:
        print("You must enter Yes or No")
        ask = input("Have you played the game before? ").lower()


def game():
    length = input("\nWhat game length would you like to play(short, medium, long)? ").lower()
    if length == "short":
        questions = 5
    elif length == "long":
        questions = 15
    else:
        questions = 10

    score = 0
    questions_asked = 0
    user_choice = int(input("What time table would you like to practice? "))

    while questions_asked != questions:
        num1 = user_choice
        num2 = random.randint(2, 11)

        answer = num1 * num2
        question = int(input(f"{num1} x {num2} = "))

        if question == answer:
            print("Correct!")
            score += 5
            questions_asked += 1
        else:
            print("Incorrect.")
            score -= 10
            questions_asked += 1

        print(f"Score: {score}")

    print(f"Final Score: {score}")


game()

play_again = input("Game finished, would you like to play again? ").lower()

if play_again == "yes":
    game()
else:
    print("\nThank you for playing!")
