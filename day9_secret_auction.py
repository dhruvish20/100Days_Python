import os
clear = lambda: os.system('cls')

clear()
print("welcome to the secret auction program.")

def find_highest_bidder(bidding_records):
    highest_amount = 0
    winner = ""
    for bidder in bidding_records:
        bid_amount = bidding_records[bidder]
        if bid_amount > highest_amount:
            highest_amount = bid_amount
            winner = bidder
    print(f"Winner of the auction is {winner} with the bid amount of ${highest_amount}. ")

bids = {}
bidding_finished = False
while not bidding_finished:
    name = input("Please enter yoyr name : ")
    price = int(input("What is your bid? : "))
    bids[name] = price
    should_continue = input("Are there any bidders? Type 'yes' or 'no'.  ").lower()
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()
