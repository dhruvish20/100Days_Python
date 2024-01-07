print("Welcome to the Tresure Island.\n Your goal is to find the tresure")

choice1 = input('You are at the croroad , where do you want to go ? Type "Left "or "right"').lower()

if choice1 == "left":
    choice2 = input("You have come to the lake, do you want to wait or swim ?").lower()
    if choice2 == "swim":
        choice3 = input("You have reached the final door? which you want to open ? Red , Yellow or Orange?").lower()
        if choice3 == "red":
            print("You have find the tresure. Congratulations.")
        else:
            print("Game Over.")
    else:
        print("Game Over.")
else:
    print("Game Over.")