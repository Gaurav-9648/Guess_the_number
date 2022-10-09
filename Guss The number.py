import random
from tkinter import *
root = Tk()

#icon change.
img=PhotoImage(file="g.png")
root.iconphoto(False,img)
root.title("GUESS THE NUMBER")
root.geometry('410x480')

# add this backgroun img
img = PhotoImage(file="image1.gif")
label = Label(
    root,
    image=img
)
label.place(x=0, y=0)

# title name
lblInfo = Label(font=('arial',20,'bold'),text='  Guess The Number Games  ',fg='Red')
lblInfo.grid(row=0,column=1,padx=5, pady=10)

# start the project numberguessing game
class NumberGuessing:
    num1 = IntVar()
    num2 = IntVar()
    guessedNumber=IntVar()
    value=None
    def check(self):
        if self.num1.get()==0 or self.num2.get() == 0 or self.guessedNumber.get() ==0 :
            self.ResultLabel.configure(text="Please input all fields")
        else:
            self.value = random.randint(self.num1.get(), self.num2.get())
            if self.guessedNumber.get() == self.value:
                self.ResultLabel.configure(text="Wow You are Right") # if number guess are right 
            else:
                self.ResultLabel.configure(text="Opps number is "+ str(self.value)) # if number guess wrong



    def __init__(self):
        self.lfont = ('Algerian', 20)

        # The first box of entering the number.
        self.entry1= Entry(root, textvariable=self.num1, font=self.lfont, foreground="blue")
        self.entry1.grid(row=1, column=1, padx=5, pady=5)

        # between the two number
        self.Label2= Label(root, text="Between", font=('arial',20,'bold'), foreground="green")
        self.Label2.grid(row=2, column=1, padx=5, pady=5)

        # second number enter
        self.entry2= Entry(root, textvariable=self.num2, font=self.lfont, foreground="Blue")
        self.entry2.grid(row=3, column=1, padx=5, pady=5)

        self.Label3= Label(root, text="Guess Any Number", font=('arial',20,'bold'), foreground="Black")
        self.Label3.grid(row=4, columnspan=2, pady=10)


        # enter the guess number 
        self.entry3= Entry(root, textvariable=self.guessedNumber, font=self.lfont, foreground="blue")
        self.entry3.grid(row=5, column=1, pady=10, padx=5)


        # Click on check if the number is right or not.
        self.btn = Button(root, text="Check", font=('arial',20,'bold'), foreground="black", command=self.check)
        self.btn.grid(row=6, columnspan=3, pady=10,)

        # The result will be visible whether you have guessed right or not.
        self.ResultLabel= Label(root, text="", font=('arial',20,'bold'), foreground="green")
        self.ResultLabel.grid(row=7, columnspan=2, pady=10, padx=5)


        root.mainloop()
NumberGuessing()