"""A Number Guessing Game"""

import random

def give_hint(guess: int, correct_number: int) -> str:
    if guess < correct_number:
        return "Too low."
    if guess > correct_number:
        return "Too high."
    return "Correct!"

class GuessGame:
    def __init__(self, max_number: int = 10, attempts: int = 3):
        self.max_number = max_number
        self.attempts = attempts

    def play(self) -> bool:
        correct_number = random.randint(1, self.max_number)
        print(f"Guess a number between 1 and {self.max_number}. You have {self.attempts} attempts.")
        for attempt in range(1, self.attempts + 1):
            try:
                guess = int(input(f"Attempt {attempt}: "))
            except ValueError:
                print("Please enter a valid integer.")
                continue

            hint = give_hint(guess, correct_number)
            if guess == correct_number:
                print("You got it!")
                return True
            else:
                print(hint)
        print(f"Out of attempts. The correct number was {correct_number}.")
        return False

if __name__ == "__main__":
    # spawn several games with different max numbers
    games = [
        GuessGame(max_number=3, attempts=3),
        GuessGame(max_number=4, attempts=3),
        GuessGame(max_number=5, attempts=3),
        GuessGame(max_number=6, attempts=3),
    ]
    for game in games:
        game.play()
        print("-" * 40)