from random import *
from time import *
from tkinter import *


def record(string):
    records=open("TestRecords.txt", "a")
    records.write(string + "\n")
    records.close()

# def marktest():
#     file=open("TestRecords.txt", "r")
#     while True:
#         line=file.readlines()
#         if not line:
#             break
#         elif "Test" in line:
#             testno = line[-1] + 1
#             break
    
def displayfn():
    # THIS IS THE DATA WHICH CAN BE APPENDED LATER OR FOR PERSON TO PERSON
    phybooks=["HC VERMA", "GIANCOLI", "SL ARORA", "NCERT","EXEMPLAR","PYQS"]
    chembooks=["NCERT", "OP TANDON ORG","EXEMPLAR","PYQS"]
    mathbooks=["NCERT", "EXEMPLAR", "PYQS", "RD Sharma"]

    # subject = input('ENTER SUBJECT:')
    subject = subentry.get()
    if subject.lower() in "physics": 
        booklist = phybooks 
        c_num=4
        # c_num = 14
    elif subject.lower() in "chemistry": 
        booklist = chembooks
        c_num = 3
        # c_num = 10
    elif subject.lower() in "maths": 
        booklist = mathbooks
        c_num = 6
        # c_num = 13

    records=open("TestRecords.txt", "a")
    records.write("\n" + f"{subject.upper()} TEST" + "\n")
    records.close()
    for qno in range(20):
        qline=f"Q{qno+1}: Question number {randint(1,60)} of {choice(booklist)} of chapter number {randint(1,c_num)}"
        record(qline)
        # sleep(2)

def lols():
    display["text"] = "In Process ..."
def morelols():
    sleep(5)
    display["text"] = "Done! Kindly Open the TestRecords.txt file"


window=Tk()

window.title("TEST GENERATER")
window.config(bg="skyblue")

heading=Label(window, text="GENERATE A TEST", font=("Impact", 60, "bold"), bg="skyblue", fg="black")
heading.pack()

label = Label(window, text="Enter Subject:", font=("Arial", 30), bg="skyblue", fg="black")
label.pack()

subentry = Entry(window,font=("Arial", 20), bg="white", fg="black" )
subentry.pack()

genbutn = Button(window, text="Generate !", font=("Arial", 20), bg="green", fg="white",command=lambda: [displayfn(), lols(),morelols()])
genbutn.pack()

display = Label(window, text="", font=("Arial", 30), bg="skyblue", fg="black")
display.pack()

window.mainloop()