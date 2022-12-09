import tkinter
from tkinter import 

def button_clicked():
    print ("Button clicked!")
    new_text = input.get()
    my_label.config(text=new_text)



window = tkinter.Tk()
window.title("CodeGreen Project")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)


#Label
my_label = Label(text="CodeGreen Projectz", font=("Arial", 22, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)
# my_label.pack(side="left")

# Button
button = Button(text="Click Here", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)


# Entry
input = Entry(width=10)

# import turtle

# tim = turtle.Turtle()
# tim.write("Some Text", font="Times New Roman" 30)
window.mainloop()