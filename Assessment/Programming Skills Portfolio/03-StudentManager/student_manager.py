from tkinter import *

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