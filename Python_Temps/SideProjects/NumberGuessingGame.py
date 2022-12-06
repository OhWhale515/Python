from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0
def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

def set_difficulty():
    level = input("Choose a difficulty level. 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print("This is the guessing game.")
    print(" Im thinking of a number between 1 and 100")
    answer = randint(1, 100)

    turns = set_difficulty()
    guess = 0
    
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess.")

        guess = int(input("Make a guess: "))
        
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("No more attempts, its over LMAO!")
            
        elif guess != answer:
            print("Sorry, Guess again.")
game()

