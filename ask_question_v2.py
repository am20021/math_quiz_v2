import random

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

score = 0
questions_asked = 0
user_choice = int(input("What time table would you like to practice? "))

while questions_asked != questions:
    num1 = user_choice
    num2 = random.randint(2, 11)

    answer = num1*num2
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
