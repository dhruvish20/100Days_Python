import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
lives = 6
word_list = ["ardvark","baboon","camel"]

chosen_word = random.choice(word_list)
print(f"chosen word is {chosen_word}")

display = []
for _ in range(len(chosen_word)):
        display.append("_")
print(display)

while not end_of_game:
    guess = input("Guess a letter : ").lower()
    
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess

    print(display)
    if guess not in chosen_word:
        lives -=1 
        if lives == 0:
            end_of_game = True
            print("You lose")

    if "_" not in display:
        end_of_game = True
        print("You win.")
        
    print(stages[lives])