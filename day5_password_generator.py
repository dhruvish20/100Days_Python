import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
           't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

signs = ['!', '"', '#', '$', '%', '&']

print("Welcome to the password generator.")

num_letters = int(input("How many latters do you want in your password? "))
num_numbers = int(input("How many numbers you would like to add? "))
num_signs = int(input("How many signs you would like to enter? "))

password_list = []

for char in range(1, num_letters +1):
    password_list += random.choice(letters)

for char in range(1, num_numbers + 1):
    password_list += random.choice(numbers)

for char in range(1, num_signs + 1):
    password_list += random.choice(signs)

random.shuffle(password_list)
password = ""

for char in password_list:
    password += char
print(password)