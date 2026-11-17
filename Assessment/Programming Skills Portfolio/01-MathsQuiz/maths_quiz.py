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
    global difficulty, score, question_count #this uses the variables from the top of the file isntead of making new ones in this function
    difficulty = level                       #this remembers the level that was chosen
    score = 0                                #this resets the score for a new quiz
    question_count = 1                       #we start on question 1
    new_problem()                            #this displays the first question

#menu widgets as lambda allows each button pass its own level number to start_quiz)
Label(menu_frame, text="Difficulty Level", font=("Calibri", 16, "bold")).pack(pady=20)
Button(menu_frame, text="1. Easy", width=20, command=lambda: start_quiz(1)).pack(pady=8)
Button(menu_frame, text="2. Medium", width=20, command=lambda: start_quiz(2)).pack(pady=8)
Button(menu_frame, text="3. Hard", width=20, command=lambda: start_quiz(3)).pack(pady=8)

#displays the question and answer entry box for the quiz
def displayProblem(number1, operator, number2):
    #str turns a number into text, because + cant join text and a number
    problem_label.config(text=str(number1) + " " + operator + " " + str(number2) + " =")
    answer_entry.delete(0, END) #clears the entry box
    answer_entry.focus()        #puts the cursor in the entry box
    quiz_frame.tkraise()        #brings the screen quiz to the front

#this creates a new problem for the player to answer and displays it
def new_problem():
    global attempt, correct_answer
    attempt = 1                     #every new problem starts with the first attempt
    number1 = randomInt(difficulty) #first random number
    number2 = randomInt(difficulty) #second random number
    operator = decideOperation()    # '+' or '-'

    if operator == '+':
        correct_answer = number1 + number2
    else:
        correct_answer = number1 - number2 #this allows for negative like 5 - 20

    displayProblem(number1, operator, number2)

#quiz screen widgets
problem_label = Label(quiz_frame, font=("Calibri", 26, "bold")) #this is the label that will display the question
problem_label.pack(pady=40)

answer_entry = Entry(quiz_frame, font=("Calibri", 18), width=10, justify="center") #the player types here
answer_entry.pack()

#this checks the answer, shows a message, returns true of false
def isCorrect(user_answer, right_answer, tries):
    if user_answer == right_answer:
        if tries == 1:
            messagebox.showinfo("correct", "correct! +10 points")
        else:
            messagebox.showinfo("correct", "correct! +5 points")
        return True #tells the program that the answer was correct
    else:
        if tries == 1:
            messagebox.showinfo("wrong", "wrong! try one more time")
        else:
            messagebox.showinfo("wrong", "wrong again. on to the next question")
        return False #tells the program that the answer was wrong

#moves on to the next question, or to the results after question 10
def next_question():
    global question_count
    question_count = question_count + 1
    if question_count > 10:
        displayResults(score) #the quiz is over
    else:
        new_problem()

#this runs when the submit button is clicked
def check_answer():
    global score, attempt
    user_answer = int(answer_entry.get()) #get() reads the typed text while int() turns it into a whole number

    if isCorrect(user_answer, correct_answer, attempt): #true means the answer is correct
        if attempt == 1:
            score = score + 10 #first attempt gives 10 pts
        else:
            score = score + 5 #while second number gives only 5 pts
        next_question()
    else:
        if attempt == 1:
            attempt = 2 #one more chance at the same problem
            answer_entry.delete(0, END)
        else:
            next_question() #if the tow answers are wrong we move on

#the submit button goes here because it needs to check_answer to exist above it
Button(quiz_frame, text="submit", width=15, command=check_answer).pack(pady=20)

#shows the final score out of 100 and the players rank
def displayResults(final_score):
    if final_score > 90:
        rank = "A+"
    elif final_score >= 80:
        rank = "A"
    elif final_score >= 70:
        rank = "B"
    elif final_score >= 60:
        rank = "C"
    elif final_score >= 50:
        rank = "D"
    else:
        rank = "F"

    final_score_label.config(text="your score: " + str(final_score) + " / 100") #the config changes a widgets text
    rank_label.config(text="your rank: " + rank)
    result_frame.tkraise() #brings the results screen to the front

#results screen widgets
Label(result_frame, text="quiz finished!!!", font=("Calibri", 20, "bold")).pack(pady=20)

final_score_label = Label(result_frame, font=("Calibri", 16))
final_score_label.pack(pady=5)

rank_label = Label(result_frame, font=("Calibri", 16))
rank_label.pack(pady=5)

Label(result_frame, text="would you like to play again?", font=("Calibri", 12)).pack(pady=15)
Button(result_frame, text="play again", width=15, command=displayMenu).pack(pady=5)

displayMenu()   #this brings the menu ot the front
root.mainloop() #this keeps the window open