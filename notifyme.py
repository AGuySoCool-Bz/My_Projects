import time
from plyer import notification 

# name=input('Enter your name:')
msgtitle = input('Enter title of the msg(eg- Like name of the Event):')
msg=input('Enter info about the event:')
timeot = input('Enter the time at which the event will take place(eg- 5/6/2024 06:00:00): ')
intervals= input('Enter time intervals(in hours) at which you want notifications to appear(1 hour by default): ')

if __name__=="__main__":
    while True:
        lols = 0
        if timeot != "":
            re=time.strptime(timeot,"%d/%m/%Y %H:%M:%S")
            tame = (time.mktime(re) - time.time()) / 3600
            lols = str(round(tame))

        # tame = time.mktime(re) - time.time()
        # lols = str(round(tame))
        # lolstatement = f""
            notification.notify(
                title = f"{msgtitle} !",
                message=f"{msg}. Only {lols} hours left!!!",
                timeout=3
            )

        else:
            notification.notify(
                title = f"{msgtitle} !",
                message=f"{msg}.",
                timeout=3
            )

        if intervals != "":  time.sleep(3600*(float(intervals)))
        else: time.sleep(3600)
       
        
        
    


