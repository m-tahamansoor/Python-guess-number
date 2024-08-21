import random

def guess_the_number():
    print("\n\tWelcome to Guess The Number!")
    print("\nI am thinking between a number between 2 to 100.")

    lower_limit = 1
    higher_limit = 100
    max_attemts = 10

    difficulty = input("Choose a difficuty level - easy , medium , hard: ").lower()

    if difficulty == "easy":
        max_attemts = 15
    elif difficulty == "meduium":
        max_attemts = 10
    elif difficulty == "hard":
        max_attemts = 5
    else: 
        print("Invalid difficulty level...Playing on Medium")

    secret_number = random.randint(lower_limit,higher_limit)
    attempts = 0

    while attempts < max_attemts:
        guess = int(input(f"Attempt {attempts + 1}/{max_attemts}: Enter your guess"))

        if guess < secret_number:
            print("opss! try a higher number...")
        elif guess > max_attemts:
            print("opss! try a lower number...")
        else:
            print(f"Congragulations! You guessed the number {secret_number} correctly in {attempts + 1} attempts.")
            break
        
        attempts += 1

    if attempts == max_attemts:
        print(f"Sorry, you've run out of attempts. The secret number was {secret_number}.")

if __name__ == "__main__":
    guess_the_number() 