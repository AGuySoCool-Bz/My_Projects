print("Welcome to Kaun Banega Crorepati !!!")
questions=[
    "Which planet is known as the Red Planet? ",
"What is the capital city of Japan?",
"In which year did the Titanic sink?",
"What is the largest mammal in the world?",
"Who wrote the play Romeo and Juliet?",
"What is the chemical symbol for gold?",
"Which of the following is a primary color?",
"What is the largest ocean on Earth?",
"Who was the first woman to win a Nobel Prize?",
"In which year did the United States declare its independence?",
"Which gas makes up the majority of Earth's atmosphere?",
"Who painted the Mona Lisa?",
"What is the capital of Australia?",
"Which of the following is a programming language?",
 "What is the powerhouse of the cell?", 
 "Who is known as the Father of Computer Science?"
]
options=[
    "A) Venus, B) Mars, C) Jupiter, D) Saturn",

"A) Beijing, B) Tokyo, C) Seoul, D) Bangkok",

"A) 1905, B) 1912, C) 1920, D) 1931",

"A) Elephant, B) Blue Whale, C) Giraffe, D) Gorilla",

"A) Charles Dickens, B) William Shakespeare, C) Jane Austen, D) F. Scott Fitzgerald",

"A) Gd, B) Au, C) Ag, D) Fe",

"A) Orange, B) Green, C) Yellow, D) Purple",

"A) Atlantic Ocean, B) Indian Ocean, C) Pacific Ocean, D) Arctic Ocean",

"A) Marie Curie, B) Amelia Earhart, C) Rosa Parks, D) Mother Teresa",

"A) 1776, B) 1789, C) 1801, D) 1620",

"A) Nitrogen, B) Oxygen, C) Carbon dioxide, D) Hydrogen",

"A) Vincent van Gogh, B) Pablo Picasso, C) Leonardo da Vinci, D) Michelangelo",

"A) Sydney, B) Melbourne, C) Canberra, D) Brisbane",

"A) HTML, B) JPEG, C) XML, D) Java",

"A) Nucleus, B) Mitochondria, C) Endoplasmic reticulum, D) Golgi apparatus",

"A) Alan Turing, B) Bill Gates, C) Steve Jobs, D) Tim Berners-Lee"
]

cans=[
    "B) Mars",
"B) Tokyo",
"B) 1912",
"B) Blue Whale",
"B) William Shakespeare",
"B) Au",
"C) Yellow",
"C) Pacific Ocean",
"A) Marie Curie",
"A) 1776",
"A) Nitrogen",
"C) Leonardo da Vinci",
"C) Canberra",
"D) Java",
"B) Mitochondria",
"A) Alan Turing"
]
n=0
price_value={1:1000, 2:2000, 3:3000, 4:5000, 5:10000, 6:20000, 7:40000, 8:80000, 9:160000, 10:320000, 11:640000, 12:1250000, 13:2500000, 14:5000000, 15:10000000, 16:70000000 }
while n<16:
    print("Question No", n+1 , questions[n], options[n])
    ch=input("Enter option of your choosen option(in caps):")
    if ch == (cans[n])[0]:
        print("Congratulations!!! Correct answer")
        print("You won", price_value[n], "rupees by answering this question correctly")
        n+=1

    elif ch == "quit":
        print("You won", price_value[n], "rupees")
        break
        
    else:
        print(f"Wrong Answer !!! Correct Answer is {cans[n]}")
        if n<5:
            print("Sorry!!! You didn't win any price")
            break
        elif n<10:
            print("You won", price_value[5], "rupees")
            break
        elif n>=10:
            print("You won", price_value[10], "rupees")
            break



        