# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove the 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

import random as r
def code(str:str):
    code_lang=""
    if len(str) >= 3:
        for i in range(3):
            code_lang += r.choice("qwertyuiopasdfghjklzxcvbnm")
        code_lang += str[1:] + str[0]
        for i in range(3):
            code_lang += r.choice("qwertyuiopasdfghjklzxcvbnm")
    else:
        code_lang += str[-1::]
    return code_lang

def decode(tr:str):
    # tr=input("enter your code: ")
    decode_lang=""
    if len(tr) >= 3:
        c=len(tr)-4
        decode_lang += tr[c]
        decode_lang += tr[3:c]
    else:
        decode_lang += tr.reverse()
    return decode_lang

if __name__=="__main__":
    print(code("Thismessageissecret"))
    print(decode(code("Thismessageissecret")))

    