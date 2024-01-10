from day14gamedata import data
import random
import os
clear = lambda: os.system('cls')

def get_Account():
    return random.choice(data)

def format_Account(account_data):
    Name = account_data["name"]
    Description = account_data["description"]
    Country = account_data["country"]

    return f"{Name} , a {Description} , from {Country}"

def check_Answer(guess , account_A , account_B):
    if account_A > account_B:
        return guess == "a"
    else:
        return guess == "b"
    

def game():
    account_A = get_Account()
    account_B = get_Account()
    is_game_over = False
    score = 0


    while not is_game_over:
        account_A = account_B
        account_B = get_Account()
        print(f"Compare : {format_Account(account_A)}")
        print("Vs")
        print(f"COmpare : {format_Account(account_B)}")

        followers_A = account_A["follower_count"]
        followers_B = account_B["follower_count"]

        guess = input("Guess the highest followers account :  ")

        is_correct = check_Answer(guess , followers_A , followers_B)

        clear()
        if is_correct:
            score +=1
            print(f"You are right: Your current score is {score}")
        else:
            is_game_over = True
            print(f"You are wrong: Your final score is {score}")

game()
    