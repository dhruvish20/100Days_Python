import tkinter


window = tkinter.Tk()
window.title("Mile to Km Conveter")
window.config(padx= 20 , pady= 20)
# window.minsize(width= 500 , height= 500)

entry = tkinter.Entry(width=17)
entry.grid(row= 0, column= 1)


miles_label = tkinter.Label(text="Miles")
miles_label.grid(row= 0, column= 2)

is_equal_to_label = tkinter.Label(text="is equal to")
is_equal_to_label.grid(row= 1, column= 0)

km_value_label = tkinter.Label(text="0")
km_value_label.grid(row= 1, column= 1)

km_label = tkinter.Label(text= "Km")
km_label.grid(row= 1, column= 2)

def convert():
    miles = float(entry.get())
    km = miles * 1.609
    km_value_label.config(text= f"{km}")

calculate_button = tkinter.Button(text= "Calculate" , command= convert)
calculate_button.grid(row= 2, column= 1)



window.mainloop()