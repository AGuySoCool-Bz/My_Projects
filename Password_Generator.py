# Different Types of Password Generators
from random import *
def generate_password(landmark_info,length):
        num="1234567890"
        spc="!@#$%&*"
        password = ""
        for i in range(len(landmark_info)):
            password += choice(landmark_info)
        for i in range(length - len(landmark_info)-2):
            password += choice(spc)
        for i in range(2):
            password += choice(num)

def random_password(length):
    password=""
    alphanum="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%&*"
    items=list(alphanum)
    for i in range(length):
            password += choice(items)
            print(f"Password Generated: {password}")

def spc_password(landmark_info,password_length):
    spc="!@#$%&*"
    password = ""
    ran_li = ""
    for i in range(len(landmark_info)):
        lol = landmark_info.lower()
        a=choice(lol)
        ran_li += a
        lol.replace(a,"")
    # print(ran_li)
    for i in ran_li:
        if i == "a":
            password += "@"
        elif i == "s":
            password += "$"
        elif i == "h":
            password += "#"
        elif i == "i":
            password += "!"
        elif i == "p":
            password += "%"
        else:
            password += i
    num="1234567890"
    if len(landmark_info) < password_length:
        for i in range(password_length - len(landmark_info)):
            password += choice(num)
    return password
        
              