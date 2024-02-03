from tkinter import *
import os
from tkinter import messagebox
from random import choice, randint, shuffle
import json
import pyperclip

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website)== 0 or len(password) == 0:
        messagebox.showinfo(title="Oosps!" , message="Please fill all the details")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                      f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            try:
                with open(os.path.join(os.path.dirname(__file__),"data.json") , "r") as data_file:
                    data = json.load(data_file)
                    
            except FileNotFoundError:
                with open(os.path.join(os.path.dirname(__file__),"data.json") , "w") as data_file:
                    json.dump(new_data , data_file , indent= 4)  
            else:
                data.update(new_data)

                with open(os.path.join(os.path.dirname(__file__),"data.json") , "w") as data_file:
                    json.dump(data , data_file , indent= 4)
            
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


window = Tk()
window.title("Password Manager")
window.config(padx= 50 , pady= 50)

image_file = os.path.join(os.path.dirname(__file__) , "logo.png")
canvas = Canvas(width= 200 , height= 200)
image_logo = PhotoImage(file= image_file)
canvas.create_image(100 , 100 , image= image_logo)
canvas.grid(row= 0 , column= 1)

website_label = Label(text="Website:")
website_label.grid(row= 1, column= 0)
email_label = Label(text="Email/Username:")
email_label.grid(row= 2, column= 0)
password_label = Label(text="Password:")
password_label.grid(row=3, column= 0)


website_entry = Entry(width= 35)
website_entry.grid(row=1 , column= 1 , columnspan=2 , sticky= 'w')
website_entry.focus()
email_entry = Entry(width= 35)
email_entry.grid(row= 2 , column= 1 , columnspan=2, sticky= 'w')
email_entry.insert(0 ,"parekhdhruvish03@gmail.com")
password_entry = Entry(width= 35)
password_entry.grid(row= 3 , column= 1, sticky= 'w')

generate_password_button= Button(text="Generate" , command=generate_password)
generate_password_button.grid(row=3 , column= 3, sticky= 'w')

add_button = Button(text="Add credetials" , width= 35 , command= save)
add_button.grid(row=4, column=1 , columnspan=2, sticky= 'w')

search_Website_button = Button(text="search")
search_Website_button.grid(row= 1, column=3)


window.mainloop()