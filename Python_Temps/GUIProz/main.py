import tkinter

window = tkinter.Tk()
window.title("CodeGreen Project")
window.minsize(width=500, height=300)


#Label

my_label = tkinter.Label(text="CodeGreen Projectz", font=("Arial", 22, "bold"))
my_label.pack(side="left")

# import turtle

# tim = turtle.Turtle()
# tim.write("Some Text", font="Times New Roman" 30)
window.mainloop()