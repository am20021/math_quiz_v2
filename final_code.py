import random

# Welcomes user.
print("Welcome to Math Quiz!")
# Asks user if they have played game before.
ask = input("Have you played the game before? ").lower()
# valid variable used to validate data input for yes/no checker.
valid = False


# Function for displaying instruction if user has not played game before.
def instructions():
    print("\n*** How to Play ****")
    print(
        "\n- A question relating to the times tables will be asked.\n- Example: 9x9\n- A correct answer will grant you 5 points.\n- An incorrect answer will take away 10 of your points.")
    print(
        "- Depending on game length selected the number of questions asked will be different.\n- Short game = 5 questions, Medium = 10, Long = 15")


# While loop uses valid variable to validate data input
while not valid:
    # If user types yes valid is set to true to break loop and program continues.
    if ask == "yes" or ask == "y":
        valid = True
    # If user types no valid is set to true to break loop, instructions are displayed and program continues.
    elif ask == "no" or ask == "n":
        instructions()
        valid = True
    # If anything but yes/no is entered, an error message is displayed and question is re-asked.
    else:
        print("You must enter Yes or No")
        ask = input("Have you played the game before? ").lower()


# Function for main game loop.
def game():
    # If user enters anything but a valid game length, game length defaults to medium length game.
    print("\n- The program will revert to medium game length if no valid length is entered.")
    # Asks user what length of game they would like to play.
    length = input("\nWhat game length would you like to play(short, medium, long)? ").lower()
    # If user enters short the number of questions to be asked is set to 5 and a message re-stating chosen game length is displayed for clarity.
    if length == "short":
        questions = 5
        print("You have chosen to play a short game.")
    # If user enters long the number of questions to be asked is set to 15 and a message re-stating chosen game length is displayed for clarity.
    elif length == "long":
        questions = 15
        print("You have chosen to play a long game.")
    # If user enters anything but short or long the number of questions to be asked is set to 10(medium length game) and a message re-stating chosen game length is displayed for clarity.
    else:
        questions = 10
        print("You have chosen to play a medium length game.")

    # Score variable created and set to default value 0.
    score = 0
    # questions_asked variable created and set to default value 0 to track amount of questions that have been asked.
    questions_asked = 0
    # Asks user what timetable they would like to practice/play with.
    user_choice = int(input("What time table would you like to practice? "))

    # While loop works by comparing questions_asked and questions variables to see how many questions need to be asked before breaking loop depending on chosen game length.
    # Once questions_asked is equal to the amount of questions needed to be asked the loop breaks.
    while questions_asked != questions:
        # First number is determined by the timetable the user chose to practice.
        num1 = user_choice
        # Second number is randomly generated between 2 and 12.
        num2 = random.randint(2, 11)

        # Correct answer is calculated by program by multiplying both integers.
        answer = num1 * num2
        # Question is displayed and asks for input.
        question = int(input(f"{num1} x {num2} = "))

        # If the user input in the question variable is equal to the calculated answer that means that the user got a correct answer.
        if question == answer:
            print("Correct!")
            # 5 score is added for a correct answer.
            score += 5
            # questions_asked variable is incremented by 1 to indicate a question has been asked.
            questions_asked += 1
        # If the user input in the question variable is not equal to the calculated answer that means that the user got an incorrect answer.
        else:
            print("Incorrect.")
            # 10 score is deducted from total score for an incorrect answer.
            score -= 10
            # questions_asked variable is incremented by 1 to indicate a question has been asked.
            questions_asked += 1

        # Current score is displayed after each question.
        print(f"Score: {score}")

    # Final score is displayed at the end of the game.
    print(f"Final Score: {score}")


# Calls the game() function.
game()

# play_again variable asks user if they want to play again.
play_again = input("Game finished, would you like to play again? ").lower()

# If the user enters yes then game() function is called again to have a second round of the game.
if play_again == "yes":
    game()
# If anything but yes is entered a thank you for playing message is displayed and game ends.
else:
    print("\nThank you for playing!")
