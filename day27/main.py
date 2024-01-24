import tkinter


window = tkinter.Tk()
window.title("My Frist GUI..")
window.minsize(width= 500 , height= 400)


label = tkinter.Label(text= "I am a Lebel..." , font= ("Arial" , 22 , "normal"))
label.grid(row= 0, column= 0)


label.config(text= "newText")

def clicked_button():
    label.config(text= input.get())



button = tkinter.Button(text="Click ME." , command= clicked_button)
button.grid(row= 0, column= 2)

new_button = tkinter.Button(text = "New Button." , command= clicked_button)
new_button.grid(row= 1, column= 1)


input = tkinter.Entry(width= 10)
input.grid(row= 2, column= 3)
print(input.get())











window.mainloop()