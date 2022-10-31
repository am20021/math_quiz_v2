import random

score = 0
user_choice = int(input("What time table would you like to practice? "))

num1 = user_choice
num2 = random.randint(2, 11)

answer = num1*num2
question = int(input(f"{num1} x {num2} = "))

if question == answer:
    print("Correct!")
    score += 5
else:
    print("Incorrect.")
    score -= 10

print(f"Score: {score}")
