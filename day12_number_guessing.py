from random import randint

EASY_LEVEL = 10
HARD_LEVEL = 5

def set_difficulty():
    level = input("Set a difficulty level. Type 'easy' or 'hard'. ").lower()
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL
    
def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high. ")
        return turns - 1
    elif guess < answer:
        print("Too low. ")
        return turns - 1
    else:
        print(f"You guessed it. the right number was {answer}. ")
    
def game():  
    print("Welcome to the Number Guessing Game. ")
    print("I'm thinking of a number between 0 to 100.")


    answer = randint(0,100)
    turns = set_difficulty()
    guess = 0

    while guess != answer:
        print(f"you have {turns} remaining.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer , turns)

        if turns == 0:
            print("You have run out of guesses, You Lose.")
            return
        elif guess != answer:
            print("guess again.")

game()



        
