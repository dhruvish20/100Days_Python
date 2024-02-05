from tkinter import *
import os
import requests

def get_quote():
    response = requests.get(url="https://api.kanye.rest/")
    quote = response.json()
    canvas.itemconfig(canvas_text , text = quote["quote"])


window = Tk()
window.title("Kanye says")

canvas = Canvas(width= 300 , height= 414)
image_file = os.path.join(os.path.dirname(__file__),"background.png")
background = PhotoImage(file= image_file)
canvas.create_image(150 , 207 , image= background)
canvas_text = canvas.create_text(150 , 207, text="hey" , width= 250 , font=("Arial", 20, "bold"))
canvas.grid(row=0 , column=0)

button_path = os.path.join(os.path.dirname(__file__),"kanye.png")
button_image = PhotoImage(file= button_path)
button = Button(image= button_image, highlightthickness=0 , command= get_quote)
button.grid(row=1 , column= 0)
window.mainloop()