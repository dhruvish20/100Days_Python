import random

def deal_card():
    card_list = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    selected_card = random.choice(card_list)
    return selected_card

def calculate_scores(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You Lose."

    if user_score == computer_score:
        return "Draw. "
    elif computer_score == 0:
        return "Computer has black Jack."
    elif user_score == 0:
        return "Win with the black Jack."
    elif user_score > 21:
        return "You Lose."
    elif computer_score > 21:
        return "You Win."
    elif user_score > computer_score:
        return "You Win."
    else:
        return "You Lose."
    
def play_game():

    user_card = []
    computer_card = []
    is_game_over = False

    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    while not is_game_over:

        user_score = calculate_scores(user_card)
        computer_score = calculate_scores(computer_card)

        print(f"You cards : {user_card} and your score : {user_score}")
        print(f"Computer's first card : {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to take a deal or 'n' to pass:  ")
            if user_should_deal == "y":
                user_card.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_scores(computer_card)

    print(f"Your final card: {user_card} and your final score: {user_score} ")
    print(f"Computer's final card: {computer_card} and computer final score: {computer_score}")
    print(compare(user_score, computer_score))

play_game()



