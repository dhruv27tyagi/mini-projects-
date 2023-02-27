from tkinter import *

window = Tk()
window.title("Mile to km Converter")
window.minsize(width=300, height = 200)
window.config(padx=20, pady=20)

def button_clicked():
    new_text = float(input.get())
    km = new_text * 1.609
    my_label_3.config(text=f"{km}")


input = Entry(width = 10)
input.grid(column=1,row=0)

my_label_1 = Label(text="Miles", font = ("Arial", 18, "bold"))
my_label_1.grid(column=2,row=0)

my_label_2 = Label(text="is equal to", font = ("Arial", 18, "bold"))
my_label_2.grid(column=0,row=1)

my_label_3 = Label(text="0", font = ("Arial", 18, "bold"))
my_label_3.grid(column=1,row=1)
my_label_3.config(padx=10, pady = 10)

my_label_4 = Label(text="Km", font = ("Arial", 18, "bold"))
my_label_4.grid(column=2,row=1)

button = Button(text="Calculate", command =button_clicked)
button.grid(column=1, row=2)




window.mainloop()