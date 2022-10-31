while True:
    try:
        length = input("\nWhat game length would you like to play(short, medium, long)? ").lower()
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    else:
        break
if length == "short":
    questions = 5
    print(questions)
elif length == "long":
    questions = 15
    print(questions)
else:
    questions = 10
    print(questions)
