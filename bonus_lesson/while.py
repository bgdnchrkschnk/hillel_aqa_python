# while <condition> - поки condition True цикл повторюэться

i = 1
while i <= 5:
    print(f"Number: {i}")
    i += 1

# ----------------------------
while True:
    user_input = input("Enter 'stop' to exit: ")
    if user_input.lower() == "stop":
        print("⛔ Program terminated!")
        break
    print(f"You entered: {user_input}")

# -----------------------------

import random

secret = random.randint(1, 10)
guess = None

while guess != secret:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < secret:
        print("🔺 The secret number is higher!")
    elif guess > secret:
        print("🔻 The secret number is lower!")
    else:
        print("🎉 Congratulations, you guessed it!")