import tkinter
from tkinter import *
import random
# from random import shuffle

main = tkinter.Tk()
main.title("Quizeria")
main.geometry("700x600")
main.config(background="#ffffff")
img1 = PhotoImage(file="flappy-bird-start-screen.png")
main.resizable(0, 0)

questions1 = [
    "Which of the following is the capital city of Pakistan",
    "The current Prime Minister of Pakistan is",
    "Which of the following city is referred to as the Manchester of Pakistan",
    "Which country won the most Football world cup",
    "Which country won the most ODI Cricket world cup",
    "The currency of Thailand is",
    "Python Programming language was invented by",
    "National Bird of Pakistan is",
    "National Drink of Pakistan is ",
    "The Largest Province of Pakistan in terms of population",
]
options = [
    ["Karachi", "Islamabad", "Lahore", "Faisalabad"],
    ["Imran Khan", "Nawaz Sharif", "Anwar ul Haq Kakkar", "Shahbaz Sharif"],
    ["Islamabad", "Karachi", "Lahore", "Faisalabad"],
    ["Brazil", "Argentina", "Spain", "Italy"],
    ["Australia", "England", "Spain", "India"],
    ["Pesos", "Baht", "Rupees", "Dollar"],
    ["Charles Babbage", "Linus Torvalds", "Steve Wozniak", "Guido Von Rossum"],
    ["Chakor", "Pigeon", "Peacock", "Eagle"],
    ["Sugarcane juice", "Mango juice", "Tea", "Coffee"],
    ["Punjab", "Sindh", "KPK", "Balochistan"],
]

real_answers = (1, 2, 3, 0, 0, 1, 3, 0, 0, 0)

index = []
def qgenerator():
    if len(index) == 5:
        return index
    else:
        x = random.randint(0, 9)
        if x not in index:
            index.append(x)
    return qgenerator()  


def result(score):
    global correct
    Questions.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    NextButton.destroy()
    result = Label(
        main,
        background="#ffffff",
        font=("San-serif", 20),
        text=f"You scored {(score/5)*100}% \n \n {correct}",
    )
    result.pack(pady=100)


correct = ""
def calculation():
    global user_answer, index, real_answers, correct, ques, score
    # score_var = StringVar()
    x = 0
    score = 0
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
    # score_var.set(f"Your Score: {score}%")
    print(score)
    result(score)




ques = 1
user_answer = []
def next_question():
    global ques, score
    global rvariable, Questions, r1, r2, r3, r4, user_answer
    x = rvariable.get()
    print(x)
    user_answer.append(x)
    rvariable.set(-1)
    if ques < 5:
        Questions.config(text=questions1[index[ques]])
        r1["text"] = options[index[ques]][0]
        r2["text"] = options[index[ques]][1]
        r3["text"] = options[index[ques]][2]
        r4["text"] = options[index[ques]][3]
        ques += 1
        score_var.set(f"Your Score is: {score}%")
    else:
        calculation()

score_var = StringVar()
def start_quiz():
    global Questions, r1, r2, r3, r4, NextButton, scoreboard, score, score_var
    score_var.set("") 
    score_label = Label(main,
                        textvariable=score_var,
                        font=("Alef", 24), 
                        background="#ffffff")
    score_label.pack()
    Questions = Label(
        main,
        text=questions1[index[0]],
        font=("San-serif", 16),
        background="#ffffff",
        width=500,
        justify="center",
        wraplength=400,
    )
    Questions.pack(pady=(100, 30))
    global rvariable
    rvariable = IntVar()
    rvariable.set(-1)

    r1 = Radiobutton(
        main,
        text=options[index[0]][0],
        value=0,
        variable=rvariable,
        background="#ffffff",
    )
    r1.pack()
    r2 = Radiobutton(
        main,
        text=options[index[0]][1],
        value=1,
        variable=rvariable,
        background="#ffffff",
    )
    r2.pack()
    r3 = Radiobutton(
        main,
        text=options[index[0]][2],
        value=2,
        variable=rvariable,
        background="#ffffff",
    )
    r3.pack()
    r4 = Radiobutton(
        main,
        text=options[index[0]][3],
        value=3,
        variable=rvariable,
        background="#ffffff"
        )
    r4.pack()
    NextButton = Button(main,
                        text="NEXT",
                        command=next_question
                        )
    NextButton.pack(pady=(40,10))


def is_pressed():
    Labelimage.destroy()
    Labeltext.destroy()
    Buttonstart.destroy()
    qgenerator()
    start_quiz()


Labelimage = Label(
                main,
                image=img1,
                background="#ffffff"
                )
Labelimage.pack()

Labeltext = Label(
    main,
    text="Welcome",
    font=("Alef", 24),
    background="#ffffff"
)
Labeltext.pack()

Buttonstart = Button(
                    main,
                    text="START", 
                    command=is_pressed)
Buttonstart.pack()

main.mainloop()