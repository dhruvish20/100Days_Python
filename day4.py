import random

user_choice = int(input("Enter what you want to choose ? Rock , Paper or Scissors? "))

computer_choice = random.randint(0,2)
print(f"Computer choose {computer_choice}")

if user_choice >= 3 or user_choice < 0:
    print("you choose an invalid number.")
elif user_choice == 0 and computer_choice == 2:
    print("you win.")
elif computer_choice > user_choice:
    print("you lose.")
elif user_choice > computer_choice:
    print("you win.")
elif computer_choice == user_choice:
    print("It's a draw.")
