alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
            'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type encode or decode to do the task: ")
text = input("type your message: ").lower()
shift = int(input("ender shift number to shift the encryption or decryption: "))

# def encrypt(plain_text , shift_amount):
#     cifer_text = ""
#     for letter in plain_text:
#         position = alphabets.index(letter)
#         new_position = position + shift_amount 
#         new_text = alphabets[new_position]
#         cifer_text += new_text
#     print(f"your encrypted text is {cifer_text}")

# def decrypt(cifer_text, shift_amount):
#     plain_text=""
#     for letter in cifer_text:
#         position = alphabets.index(letter)
#         new_position = position - shift_amount
#         new_text = alphabets[new_position]
#         plain_text += new_text
#     print(f"Your decrypted text is {plain_text}")


# if direction == "encode":
#     encrypt("hello", 5)
# elif direction == "decode":
#     decrypt("mjqqt",5)
# else:
#     print("wrong option")
    
def caesar(start_text , shift_amount , ceasar_direction):
    end_text = ""
    for letter in start_text:
        position = alphabets.index(letter)
        if ceasar_direction == "encode":
            new_position = position + shift_amount
        elif ceasar_direction == "decode":
            new_position = position - shift_amount
        else:
            print("wrong direction, choose between the two options")
        new_text = alphabets[new_position]
        end_text += new_text
    print(f"your updated text is {end_text}")

caesar(text ,shift, direction)
