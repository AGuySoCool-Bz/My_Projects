# NEWS API
from tkinter import *
import requests 
import json
from random import choice

news = {}
article_list = []

def generate_news():
    global news
    global article_list
    query = entry_topic.get()
    if query.isspace() or query.isdigit():
         display_news_title["text"] = "Please Enter Valid Input !!!"
    else:
        url = f""  # Enter your API key here
        r = requests.get(url)
        news = json.loads(r.text)
        article_list = []

        for article in news["articles"]:
            article_list.append(article)
        display_article = choice(article_list)
        article_list.remove(display_article)

        display_news_title["text"] = display_article["title"]
        display_news_desc["text"] = "\n" + display_article["description"]

def next_news():
    display_news_title["text"] = ""
    display_news_desc["text"] = ""
    global article_list
    try:
        display_article = choice(article_list)
        article_list.remove(display_article)

        display_news_title["text"] = display_article["title"]
        display_news_desc["text"] = display_article["description"]
    
    except IndexError:
        display_news_title["text"] = "No Further News !"

window = Tk()

window.title("DAILY NEWS APP")
width= window.winfo_screenwidth() 
height= window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))
window.config(bg = "skyblue")

heading = Label(window, text="GET LATEST NEWS OF ANYTOPIC ANYWHERE", font=("Impact", 35, "bold"), bg="skyblue",fg="black")
heading.pack()

entry_label = Label(window, text = "Enter below the Topic for which you desire to get the latest news" , font=("Arial", 20), bg="skyblue",fg="black")
entry_label.pack()

entry_topic = Entry(window,  font=("Arial", 20), bg="white",fg="black")
entry_topic.pack()

get_button = Button(window, text = "Get News", font=("Arial", 20), bg="green",fg="white" ,activebackground="darkgreen", command= generate_news)
get_button.pack()

display_news_title = Label(window, text="", font=("Arial", 20, "bold"), bg="skyblue",fg="black", wraplength = (window.winfo_screenwidth() - 80))
display_news_title.pack()

display_news_desc = Label(window, text="", font=("Arial", 20), bg="skyblue",fg="black", wraplength = (window.winfo_screenwidth() - 100) )
display_news_desc.pack()

next_button = Button(window, text = "Next News", font=("Arial", 20), bg="green",fg="white" , activebackground="darkgreen", command= next_news)
next_button.pack()

window.mainloop()