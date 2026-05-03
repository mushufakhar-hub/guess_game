import random
num = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")
guess = int(input("Enter your guess: "))
attempts=0
while True:
    attempts+=1
    if guess == num:
        print("Congratulations! You win the Game.")
        break   
    elif guess < num:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    if attempts==6:
        print("Game Over! You've used all your attempts.")
        print(f"The correct number was: {num}")
        break
    print(f"Attempt {attempts}/6")
    guess = int(input("Enter your guess: "))

