import json
import requests
from tkinter import *

root = Tk()
root.title("This Is Your first time of GUI in Pythone")


# creating a Input feield
myInput = Entry(root,font=30,fg="#d0d0d0")

# createing Label by Clicking button
def creatingLabel():
    newlabel = Label(root, text=f"Hello, {myInput.get()}", bg="black", fg="white",font=20)
    newlabel.pack()


# createing a label widget
# myLabel = Label(root, text="this is my Label 1", bg="black", fg="white")
myButton = Button(root,text="MyButton", padx=25,pady=10,font=10,command=creatingLabel)



# packing Item into root
myInput.pack()
myButton.pack()

root.mainloop()
