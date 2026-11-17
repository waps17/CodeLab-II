from tkinter import *
from tkinter import messagebox
import random

#this creates the main window for the quiz application
root = Tk()              #main window
root.title("Maths Quiz") #the text in the title bar
root.geometry("400x400") #window size 

#the variables to track rules of the quiz
difficulty = 1          #diffiulty of the quiz 1 easy, 2 medium, 3 hard
score = 0               #the players score (0-100)
question_count = 0      #this tracks which question the player is on for 1-10
attempt = 1             #tracks the attempts, attempt 1 10pts and attempt 2 5pts
correct_answer = 0      #correct answer to the current question

#this created a frame for each screen of the quiz while havingthe same position
menu_frame = Frame(root)
menu_frame.place(x=0, y=0, width=400, height=400)

quiz_frame = Frame(root)
quiz_frame.place(x=0, y=0, width=400, height=400)

result_frame = Frame(root)
result_frame.place(x=0, y=0, width=400, height=400)

#this function displays the difficulty menu
def displayMenu():
    menu_frame.tkraise() #thsi brings the frame in front of the other two

#returns a random integer based on the difficulty level
def randomInt(level):
    if level == 1:
        return random.randint(1, 9)       #easy level single digit numbers
    elif level == 2:
        return random.randint(10, 99)     #medium level two digit numbers
    else:
        return random.randint(1000, 9999) #hard level four digit numbers

#this function randomly chooses an operation for the question
def decideOperation():
    return random.choice(['+', '-'])

#starts a new 10 question quiz based on the difficulty level selected by the player
def start_quiz(level):
    print("Level chosen:", level)

#menu widgets as lambda allows each button pass its own level number to start_quiz)
Label(menu_frame, text="Difficulty Level", font=("Calibri", 16, "bold")).pack(pady=20)
Button(menu_frame, text="1. Easy", width=20, command=lambda: start_quiz(1)).pack(pady=8)
Button(menu_frame, text="2. Medium", width=20, command=lambda: start_quiz(2)).pack(pady=8)
Button(menu_frame, text="3. Hard", width=20, command=lambda: start_quiz(3)).pack(pady=8)

displayMenu()   #this brings the menu ot the front
root.mainloop() #this keeps the window open