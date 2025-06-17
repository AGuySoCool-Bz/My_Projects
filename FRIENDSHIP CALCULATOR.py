#Friendship Calculator

from random import *
from tkinter import *
def do():
    lp = randint(0,100)
    r["text"] = str(lp) + "%"
    
window=Tk()

window.geometry("600x320")
window.title("Friendship Calculator")
window.config(bg="skyblue")

heading=Label(window, text="FRIENDSHIP CALCULATOR", font=("Arial", 30, "bold"), bg="skyblue")
heading.pack()

yname=Label(window, text="Enter your name:", font=("Arial", 20), bg="skyblue")
yname.pack()

user_name=Entry(window, font=("Arial", 15), bg="skyblue")
user_name.pack()

thname=Label(window, text="Enter their name:", font=("Arial", 20), bg="skyblue")
thname.pack()

their_name=Entry(window, font=("Arial", 15), bg="skyblue")
their_name.pack()

calculate=Button(window, text="Calculate Friendship Percentage",font=("Arial", 20), command=do)
calculate.pack()

r=Label(window, text="%",font=("Arial", 40))
r.pack()

window.mainloop()