from tkinter import *

root = Tk()
root.title("Calculator")

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
                scvalue.set(value)
                screen.update()
            except Exception as e:
                scvalue.set("Error")
                screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

scvalue = StringVar()
screen = Entry(root, width=20, borderwidth=10, textvariable=scvalue,font=("System", 33)) 
screen.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ("1", 1, 0), ("2", 1, 1), ("3", 1, 2),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2),
    ("7", 3, 0), ("8", 3, 1), ("9", 3, 2),
    ("0", 4, 0),
    ("+", 4, 1), ("-", 5, 0), ("*", 5, 1), ("/", 5, 2),
    ("=", 4, 2), ("C", 4, 3)
]

for button_text, row, col in buttons:
    button = Button(root, text=button_text, padx=40, pady=20, font="System 20 bold")
    button.grid(row=row, column=col)
    button.bind("<Button-1>", click)

root.mainloop()
