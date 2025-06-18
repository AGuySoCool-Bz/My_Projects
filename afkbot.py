
def afkBot_typerversion():
    from pyautogui import press,sleep,typewrite
    try:
        while True: 
            typewrite("n")
            press("backspace")
            sleep(25)
    except Exception as e:
        pass

def afkbot_cursormover():
    import pyautogui
    try:
        while True:
            pyautogui.move(1, 0) 
            pyautogui.move(-1, 0)  
            pyautogui.sleep(30)  
    except Exception as e:
        pass

if __name__=="__main__":
    afkbot_cursormover()