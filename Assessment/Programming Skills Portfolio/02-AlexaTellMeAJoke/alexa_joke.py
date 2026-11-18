from tkinter import *

root = Tk() #main window
root.title("Alexa Gives Jokes") #text in the title bar
root.geometry("500x400") #size of the window

#the button that starts the joke
tell_button = Button(root, text="Alexa tell me a Joke")
tell_button.pack(pady=5)

#label that will show the setup of the joke
setup_label = Label(root, text="")
setup_label.pack(pady=5)

#label to show the punchline below
punchline_label = Label(root, text="")
punchline_label.pack(pady=5)

#button that shows the punchline 
punchline_button = Button(root, text="Show Punchline")
punchline_button.pack(pady=5)

#this button gives another random joke
next_button = Button(root, text="Next Joke")
next_button.pack(pady=5)

#this button closes the application
quit_button = Button(root, text="Quit", command=root.destroy)
quit_button.pack(pady=5)

root.mainloop() #keeps the window open