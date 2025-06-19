# CALCULATOR
from tkinter import *

# "." , "()" , "^", "backspace", "root", "%", "1/x", "00"



inputstr=""
inputs=0




def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

def t1():
    global inputs
    global inputstr
    inputs=1
    inputstr+=str(inputs)
    bresult["text"] = inputstr
def t2():
    global inputs
    global inputstr
    inputs=2
    inputstr+=str(inputs)
    bresult["text"] = inputstr
def t3():
    global inputs
    global inputstr
    inputs=3
    inputstr+=str(inputs)
    bresult["text"] = inputstr
def t4():
    global inputs
    global inputstr
    inputs=4
    inputstr+=str(inputs)
    bresult["text"] = inputstr
def t5():
    global inputs
    global inputstr
    inputs=5
    inputstr+=str(inputs)
    bresult["text"] = inputstr
def t6():
    global inputs
    global inputstr
    inputs=6
    inputstr+=str(inputs)
    bresult["text"] = inputstr
def t7():
    global inputs
    global inputstr
    inputs=7
    inputstr+=str(inputs)
    bresult["text"] = inputstr
def t8():
    global inputs
    global inputstr
    inputs=8
    inputstr+=str(inputs)
    bresult["text"] = inputstr
def t9():
    global inputs
    global inputstr
    inputs=9
    inputstr+=str(inputs)
    bresult["text"] = inputstr
def t0():
    global inputs
    global inputstr
    inputs=0
    inputstr+=str(inputs)
    bresult["text"] = inputstr

def tadd():
    global inputstr
    inputstr+=" + "
    bresult["text"] = inputstr
def tsub():
    global inputstr
    inputstr+=" - "
    bresult["text"] = inputstr
def tmul():
    global inputstr
    inputstr+=" x "
    bresult["text"] = inputstr
def tdiv():
    global inputstr
    inputstr+=" / "
    bresult["text"] = inputstr
def calc():
    global inputstr
    evaluation_line = inputstr
    # op=["x", "/", "+", "-"]
    newlist=evaluation_line.split()
    l=newlist
    while len(l) != 1:
        try:
            if "/" in l:
                rk=l.index("/")
                try:
                    ans=float(float(l[rk-1]) / float(l[rk+1]))
                except ZeroDivisionError:
                    res = "Not Defined"
                    bresult["text"] = res
                    return 0
            elif "x" in l:
                rk=l.index("x")
                ans=float(l[rk-1]) * float(l[rk+1])
            elif "+" in l:
                rk=l.index("+")
                ans=float(l[rk-1]) + float(l[rk+1])
            elif "-" in l:
                rk=l.index("-")
                ans=float(l[rk-1]) - float(l[rk+1])
        except ValueError:
            bresult["text"] = "Invalid Input"
            return 0

        l.pop(rk)
        l.pop(rk-1)
        l.pop(rk-1)
        l.insert(rk-1, ans)
    
    res = str(l[0])
    bresult["text"] = res
    inputstr = res
def clear():
    global inputstr
    inputstr = ""
    bresult["text"] = inputstr

window=Tk()

window.title("Calculator")
window.config(bg="skyblue")

b1=Button(window, text="1", font=("Arial", 25), bg="orange",fg="black", activebackground="green", activeforeground="yellow", width=4, command=t1)
b2=Button(window, text="2", font=("Arial", 25), bg="orange",fg="black", activebackground="green", activeforeground="yellow", width=4, command=t2)
b3=Button(window, text="3", font=("Arial", 25), bg="orange",fg="black", activebackground="green", activeforeground="yellow", width=4, command=t3)
b4=Button(window, text="4", font=("Arial", 25), bg="orange",fg="black", activebackground="green", activeforeground="yellow", width=4, command=t4)
b5=Button(window, text="5", font=("Arial", 25), bg="orange",fg="black", activebackground="green", activeforeground="yellow", width=4, command=t5)
b6=Button(window, text="6", font=("Arial", 25), bg="orange",fg="black", activebackground="green", activeforeground="yellow", width=4, command=t6)
b7=Button(window, text="7", font=("Arial", 25), bg="orange",fg="black", activebackground="green", activeforeground="yellow", width=4, command=t7)
b8=Button(window, text="8", font=("Arial", 25), bg="orange",fg="black", activebackground="green", activeforeground="yellow", width=4, command=t8)
b9=Button(window, text="9", font=("Arial", 25), bg="orange",fg="black", activebackground="green", activeforeground="yellow", width=4, command=t9)
b0=Button(window, text="0", font=("Arial", 25), bg="orange",fg="black", activebackground="green", activeforeground="yellow", width=4, command=t0)

bmult=Button(window, text="X", font=("Arial", 25), bg="violet",fg="black", activebackground="green", activeforeground="yellow", width=4, command=tmul)
bdiv=Button(window, text="/", font=("Arial", 25), bg="violet", fg="black", activebackground="green", activeforeground="yellow", width=4, command=tdiv)
badd=Button(window, text="+", font=("Arial", 25), bg="violet",fg="black", activebackground="green", activeforeground="yellow", width=4, command=tadd)
bsub=Button(window, text="-", font=("Arial", 25), bg="violet",fg="black", activebackground="green", activeforeground="yellow", width=4, command=tsub)
bequals=Button(window, text="=", font=("Arial", 25), bg="violet",fg="black", activebackground="green", activeforeground="yellow", width=4, command=calc)
bclear=Button(window, text="Clear", font=("Arial", 25), bg="violet",fg="black", activebackground="green", activeforeground="yellow", width=4, command=clear)


# "." , "()" , "^", "backspace", "root", "%", "1/x", "00"

bdot=Button(window, text=".", font=("Arial", 25), bg="violet",fg="black", activebackground="green", activeforeground="yellow", width=4, command=clear)
bparen=Button(window, text="()", font=("Arial", 25), bg="violet",fg="black", activebackground="green", activeforeground="yellow", width=4, command=clear)
bpower=Button(window, text="^", font=("Arial", 25), bg="violet",fg="black", activebackground="green", activeforeground="yellow", width=4, command=clear)
bbackspace=Button(window, text="<--", font=("Arial", 25), bg="violet",fg="black", activebackground="green", activeforeground="yellow", width=4, command=clear)
broot=Button(window, text="Root", font=("Arial", 25), bg="violet",fg="black", activebackground="green", activeforeground="yellow", width=4, command=clear)
bpercent=Button(window, text="%", font=("Arial", 25), bg="violet",fg="black", activebackground="green", activeforeground="yellow", width=4, command=clear)
breciprocal=Button(window, text="1/x", font=("Arial", 25), bg="violet",fg="black", activebackground="green", activeforeground="yellow", width=4, command=clear)
b00=Button(window, text="00", font=("Arial", 25), bg="violet",fg="black", activebackground="green", activeforeground="yellow", width=4, command=clear)





bresult=Label(window, text="Calculate !", font=("Arial", 20), bg="white", fg="black")
bresult.grid(row=1, columnspan=5, padx=0, pady=0)

b1.grid(row=2,column=1, padx=0, pady=0)
b2.grid(row=2,column=2, padx=0, pady=0)
b3.grid(row=2,column=3, padx=0, pady=0)
badd.grid(row=2,column=4, padx=0, pady=0)

b4.grid(row=3,column=1, padx=0, pady=0)
b5.grid(row=3,column=2, padx=0, pady=0)
b6.grid(row=3,column=3, padx=0, pady=0)
bsub.grid(row=3,column=4, padx=0, pady=0)

b7.grid(row=4,column=1, padx=0, pady=0)
b8.grid(row=4,column=2, padx=0, pady=0)
b9.grid(row=4,column=3, padx=0, pady=0)
bdiv.grid(row=4,column=4, padx=0, pady=0)

b0.grid(row=5,column=2)
bmult.grid(row=5,column=4)
bequals.grid(row=5,column=1)
bclear.grid(row=5,column=3)

window.mainloop()

