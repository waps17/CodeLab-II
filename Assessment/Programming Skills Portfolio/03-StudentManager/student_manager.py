from tkinter import *
import os

#this finds the folder this py file is in so the txt file is always found and show no errors
folder = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(folder, "studentMarks.txt")

#this stores each student in a list as it reads the txt file
students = []
with open(file_path, "r") as file:
    file.readline() #this skips the first line which is the number of students
    for line in file:
        line = line.strip()
        if line != "":
            parts = line.split(",") #this cuts the line at every comma into a list
            student = {
                "code": parts[0],
                "name": parts[1],
                "cw1": int(parts[2]),
                "cw2": int(parts[3]),
                "cw3": int(parts[4]),
                "exam": int(parts[5])
            }
            students.append(student)

#this works out the total coursework mark
def getCoursework(student):
    return student["cw1"] + student["cw2"] + student["cw3"]

#this works out the total mark of coursework plus exam which is out of 160
def getTotal(student):
    return getCoursework(student) + student["exam"]

#this works out overall percentage based on 160 marks
def getPercentage(student):
    return getTotal(student) / 160 * 100

#while this works out the grade from the percetnage
def getGrade(percentage):
    if percentage >= 70:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"

root = Tk() #makes the main window and stores it inside root 
root.title("Student Manager") #name in the title bar
root.geometry("600x500") #window size

#this is the four menu buttons
view_all_button = Button(root, text="1. view all student records", width=35)
view_all_button.pack(pady=5) #pack() puts the button in the window while pady adds space above and below

view_one_button = Button(root, text="2. view individual student record", width=35)
view_one_button.pack(pady=5)

highest_button = Button(root, text="3. show student with highest total score", width=35)
highest_button.pack(pady=5)

lowest_button = Button(root, text="4. show student with lowest total score", width=35)
lowest_button.pack(pady=5)

root.mainloop() #this keeps window open