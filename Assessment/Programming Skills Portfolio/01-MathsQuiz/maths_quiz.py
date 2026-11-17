from tkinter import *
from tkinter import messagebox
import random

#this creates the main window for the quiz application
root = Tk() #main window
root.title("Maths Quiz") #the text in the title bar
root.geometry("400x400") #window size 

#the variables to track rules of the quiz
difficulty = 1          #diffiulty of the quiz 1 easy, 2 medium, 3 hard
score = 0               #the players score (0-100)
question_count = 0      #this tracks which question the player is on for 1-10
attempt = 1             #tracks the attempts, attempt 1 10pts and attempt 2 5pts
correct_answer = 0      #correct answer to the current question

root.mainloop()