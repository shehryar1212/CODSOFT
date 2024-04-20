import random
import string
from tkinter import *

def generate_password():
    try:
        length = int(psvalue.get())
        if length <= 0:
            password_label.config(text="Please enter a valid length")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choices(characters, k=length))
        password_label.config(text=password)
    except Exception as e:
        password_label.config(text="Please enter a valid length")

root = Tk()
root.geometry("800x200")
root.title("Password Generator")

Label(root, text="Generating strong random passwords", font="System 30 bold").pack()
Label(root, text="Enter password length: ", font="System 20 ", pady=10).pack()

psvalue = StringVar()
entry = Entry(root, textvariable=psvalue)
entry.pack()

generate_button = Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

password_label = Label(root, text="", font="System 20", pady=10)
password_label.pack()

root.mainloop()
