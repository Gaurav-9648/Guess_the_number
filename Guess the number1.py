from email.mime import image
from tkinter import *
from tkinter import messagebox
from random import randint
from PIL import ImageTk



# Screen
root = Tk()
root.geometry("500x538")

#icon change.
img=PhotoImage(file="g.png")
root.iconphoto(False,img)
root.title("Number Guessing Game")
root.config(bg='black')
img = PhotoImage(file="image1.gif")
label = Label(
    root,
    image=img
)
label.place(x=0, y=0)

# Generate Number Function
def GenerateNumberFunc():
    global Number
    # Generate Number
    Number = randint(1, 10)   
    # MessageBox to show that a number was generated
    messagebox.showinfo("A Number was Generated!", "Please Guess the Number")
# Guess Number Function
def GuessNumberFunc():
    global Number
    # Get Value from Answer Entry Box
    UserResponse = AnswerEntry.get()  
    # Convert Value from Answer Entry Box to a Number
    UserResponse = int(UserResponse)
    # Check if the User Response was higher, lower, or equal to the correct number
    if UserResponse > Number:
        ResultLabel.config(text="Incorrect! Ohh it's Lower ", fg="Red")
    elif UserResponse < Number:
        ResultLabel.config(text="Incorrect! Please Guess Higher", fg="Red")
    else:
        ResultLabel.config(text="You Guess Correctly! The Number was {}".format(Number), fg="Green")
        AnswerEntry.delete(0, "end")
# Title
Title = Label(root, text="Number Guessing Game", font=("Arial", 28))
Title.pack()
# Main Frame
MainFrame = Frame(root)
MainFrame.pack(pady=58)
# Guess the Number Label
GuessNumLabel = Label(MainFrame, text="Guess a number from 1 to 10:", font=("Arial", 19))
GuessNumLabel.pack()

# Answer Entry
AnswerEntry = Entry(MainFrame, font=("Arial", 15))
AnswerEntry.pack(pady=9)

# Generate Number Button
GenerateNumberBtn = Button(MainFrame, text="Generate Number", width=15, font=("Arial", 15), background="Dodgerblue", command=GenerateNumberFunc)
GenerateNumberBtn.pack()



# Guess Button
GuessBtn = Button(MainFrame, text="Guess", width=15, font=("Arial", 15), background="#15e650", command=GuessNumberFunc)
GuessBtn.pack(pady=4)



# Result Label
ResultLabel = Label(MainFrame, text="", font=("Arial", 15))
ResultLabel.pack()



# Mainloop
root.mainloop()