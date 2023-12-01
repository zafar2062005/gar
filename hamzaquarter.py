import tkinter
from tkinter import *
import random
import pygame


main = tkinter.Tk()
main.title("Quizeria")
main.geometry("500x500")
main.config(background="#ffffff")
img1 = PhotoImage(file = "flappy-bird-start-screen.png")
main.resizable(0,0)

pygame.mixer.init()
questions1 = [
     "Which of the following is the capital city of Pakistan",
     "The current Prime Minister of Pakistan is",
     "Which of the following city is referred to as the Manchester of Pakistan",
     "Which country won the most Football world cup",
     "Which country won the most ODI Cricket world cup",
     "The currenncy of Thailand is",
     "Python Programming language was invented by",
     "National Bird of Pakistan is",
     "National Drink of Pakistan is ",
     "The Largest Province of Pakistan in terms of population",
]
options = [
     ["Karachi","Islamabad","Lahore","Faisalabad"],
     ["Imran Khan", "Nawaz Sharif", "Anwar ul Haq Kakkar", "Shahbaz Sharif"],
     ["Islamabad","Karachi","Lahore","Faisalabad"],
     ["Brazil", "Argentina", "Spain", "Italy"],
     ["Australia", "England", "Spain", "India"],
     ["Pesos", "Baht", "Rupees", "Dollar"],
     ["Charles Babbage", "Linus Torvalds", "Steve Wozniak", "Guido Von Rossum"],
     ["Chakor", "Pigeon", "Peacock","Eagle" ],
     ["Sugarcane juice", "Mango juice", "Tea", "Coffee"],
     ["Punjab", "Sindh", "KPK", "Balochistan"],
]

def win():
    pygame.mixer.music.load("win.mp3")
    pygame.mixer.music.play(loops=0)

def loose():
    pygame.mixer.music.load("lose.mp3") 
    pygame.mixer.music.play(loops=0)

real_answers = [1,2,3,0,0,1,3,0,0,0]

index = []
def qgenerator():
    global index   
    while (len(index) < 5):
        x = random.randint(0,9)
        if not x in index:
            index.append(x)
    return index        


def result(score):
    global correct
    Questions.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    # NextButton.destroy()
    scoreboard.destroy()
    result = Label(
        main,
        background="#ffffff",
        font=("San-serif", 20),
        text=f"You scored {(score/5)*100}% \n \n {correct}",
    )
    result.pack(pady=100)
    pygame.mixer.music.load("win.mp3")
    pygame.mixer.music.play(loops=0)

score = 0
correct = ""
def calculation():
    global user_answer, index, real_answers, correct, ques
    global score
    x = 0
    for i in index:
        if user_answer[x] == real_answers[i]:
            score += 1
            correct += "CORRECT\n"
        else:
            correct += (
                "INCORRECT (Correct answer is "
                + str(options[i][real_answers[i]])
                + ")"
                + "\n"
            )
        x += 1
    # print(score)
    result(score)


random1 = 0
user_answer = []
ques = 1
pointer = 1
def selected():
     global rvariable,Questions,r1,r2,r3,r4,user_answer,scoreboard
     global ques, random1, pointer
     x = rvariable.get()
    #  print(x)
     user_answer.append(x)
     rvariable.set(-1)
     pointer += 1 
     if ques < 5:
        # print(random1)
        # print([user_answer[-1] ,real_answers[index[ques-1]]])
        print(ques)
        print(pointer)
        if not pointer == 5:
            if user_answer[-1] == real_answers[index[ques-1]]:
                random1 += 1
                pygame.mixer.music.load("win.mp3")
                pygame.mixer.music.play(loops=0)
            else:  
                pygame.mixer.music.load("lose.mp3")
                pygame.mixer.music.play(loops=0)

        scoreboard.config(text = f"Score is {random1}")  
        Questions.config(text=questions1[index[ques]])
        r1["text"] = options[index[ques]][0]
        r2["text"] = options[index[ques]][1]
        r3["text"] = options[index[ques]][2]
        r4["text"] = options[index[ques]][3]
        ques  += 1
     else:
         calculation() 
          
       
def startquiz():
        global Questions,r1,r2,r3,r4, scoreboard
        scoreboard = Label(
        main,
        text= "Score is 0"
        )
        scoreboard.pack()
        Questions = Label(
             main,
             text = questions1[index[0]],
             font= ("San-serif",16),
             background="#ffffff",
             width = 500,
             justify="center",
             wraplength=400,
        )
        Questions.pack(pady=(100, 30))
        global rvariable
        rvariable = IntVar()
        rvariable.set(-1)

        r1 = Radiobutton(
             main,
             text= options[index[0]][0],
             value= 0,
             variable= rvariable,
             command=selected,
             background="#ffffff",    
        )
        r1.pack()
        r2 = Radiobutton(
             main,
             text= options[index[0]][1],
             value= 1,
             variable= rvariable,
             command=selected,
             background="#ffffff",
        )
        r2.pack()
        r3 = Radiobutton(
             main,
             text= options[index[0]][2],
             value= 2,
             variable= rvariable,
             command=selected,
             background="#ffffff",
        )
        r3.pack()
        r4 = Radiobutton(
             main,
             text= options[index[0]][3],
             value= 3,
             variable= rvariable,
             command=selected,
             background="#ffffff",
        )
        r4.pack()


def ispressed():
    Labelimage.destroy()
    Labeltext.destroy()
    Buttonstart.destroy()
    qgenerator()
    startquiz()
     
Labelimage = Label(
    main,
    image = img1,
    background="#ffffff"
)
Labelimage.pack()

Labeltext = Label(
    main,
    text = "Welcome",
    font = ("Alef", 24),
    background = "#ffffff",
)
Labeltext.pack()

Buttonstart = Button(
    main,
    text = "START",  
    command= ispressed
) 
Buttonstart.pack()
main.mainloop()
