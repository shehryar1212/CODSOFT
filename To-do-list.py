from tkinter import *

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(END, task)
        entry_task.delete(0, END)
    else:
        label_status.config(text="Please enter a task")

def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        label_status.config(text="No task selected")

def update_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        updated_task = entry_task.get()
        listbox_tasks.delete(selected_task_index)
        listbox_tasks.insert(selected_task_index, updated_task)
        entry_task.delete(0, END)
    except IndexError:
        label_status.config(text="No task selected")

root = Tk()
root.title("To-Do List")
# root.iconbitmap("i.ico")
a=Label(root,text="REMEMBERING THINGS",font="lucida 22 ",padx=50)
a.grid()

# Task entry
entry_task = Entry(root, width=50)
entry_task.grid(row=1, column=0, padx=10, pady=5)

# Buttons
button_add = Button(root, text="Add Task", width=15, command=add_task)
button_add.grid(row=1, column=1, padx=5, pady=5)

button_delete = Button(root, text="Delete Task", width=15, command=delete_task)
button_delete.grid(row=2, column=1, padx=5, pady=5)

button_update = Button(root, text="Update Task", width=15, command=update_task)
button_update.grid(row=3, column=1, padx=5, pady=5)

# Task list
listbox_tasks = Listbox(root, width=50, bd=2)
listbox_tasks.grid(row=2, column=0, padx=10, pady=5, rowspan=2)


# Status label
label_status = Label(root, text="", bd=1, relief=SUNKEN, anchor=W)
label_status.grid(row=4, column=0, columnspan=2, sticky=W+E)

root.mainloop()
