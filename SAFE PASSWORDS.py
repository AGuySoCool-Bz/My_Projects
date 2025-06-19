# Password Generator

from random import *
import Password_Storage as storage
from Password_Generator import spc_password
print("WELCOME TO THE SAFE PASSWORDS BY NAMAN KANYAL!!!")
name=input('Enter your name:')
print('''Enter the asigned key to perform the following actions:
            1-- Generate a New Password
            2-- Access your Passwords
            3-- Store Password
            4-- quit''')
while True:

    ch=int(input("Enter key: "))
    if ch==1:
        
        place_name=input('Enter the website or the place for which want to generate the password:')
        length=int(input('Enter the length you want for your password:'))
        # landmark_info = input('Please Enter any short landmark word that will help you remember your password:')

        while True: 
            password = spc_password(place_name.lower(), length) 
            print(f"Password Generated: {password}")
            storage.store_password(name,place_name,password)
            print("Stored this password successfully !!!")
            print("Copy this Password and use it")
            break

            # opinion=input('Satisfied with this password or want another one? (Yes/No):')

            # if opinion.lower() == "yes":
                # storage.store_password(name,place_name,password)
                # print("Stored this password successfully !!!")
                # print("Copy this Password and use it")
                # break

            # elif opinion.lower() == "no":
            #     password=""
            
            # else:
            #     print("Invalid Response") 
    elif ch==2:
        get_password_place= input('Enter the name of the place for which you want to see your password(Enter "all" to see the complete list):')
        if get_password_place.lower() == "all":
            storage.all(name)
        else:
            print(storage.read_password(name,get_password_place))
            if storage.read_password(name,get_password_place) == "":
                print("There is no password history for this name and place !")
    elif ch==4:
        print("Thanks for using our program")
        break
    elif ch == 3:
    
        place = input('Enter name of the website or the place of which this password is:')
        passcode = input('Enter the password to be stored:')
        storage.store_password(name, place, passcode)
        print("Password stored successfully !")
    else:
        print("Invalid Input")