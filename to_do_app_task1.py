# Task 1
# To-Do List Application
import tkinter as tk
from tkinter import messagebox

root = tk.Tk() 

# Window title
root.title("ToDo List Application")

# Add task
def tsk_add_func():         
    task = task_text.get()
    if task:
        task_lst.insert(tk.END, f"{task}")
        task_text.delete(0, tk.END) 
    else:
        messagebox.showinfo("No Task","Please enter task.")
        task_text.focus_set()

# Deletion of task
def del_tsk_func():
    selected_task_index = task_lst.curselection()     
    if selected_task_index:
        task = task_lst.get(tk.ACTIVE)
        result = messagebox.askokcancel("Confirmation", "Do you want to delete the selected task?")
        if result:
            task_lst.delete(tk.ACTIVE)
    else:
        messagebox.showinfo("No Item","Please select an item from the list above.")

# Mark task as completed
def mark_comp_func():
    selected_task_index = task_lst.curselection()     
    if selected_task_index:
        task = task_lst.get(selected_task_index)
        task_lst.delete(selected_task_index)
        comp_lst.insert(tk.END, f"{task} - Completed")
    else:
        messagebox.showinfo("No Item","Please select an item from the list above.")
        
# Completed task cleared
def tsk_comp_func():
    selected_task_index = comp_lst.curselection()     
    if selected_task_index:
        result = messagebox.askokcancel("Confirmation", "Do you want to clear selected task?")
        task = comp_lst.get(tk.ACTIVE)
        if result:
            comp_lst.delete(tk.ACTIVE)
    else:
        messagebox.showinfo("No Item","Please select an item from the list above.")

# Frame creation
frame = tk.Frame()
frame.grid(row=0, column=0, sticky=tk.W+tk.E+tk.N+tk.S)    

# Task entry
task_text = tk.Entry(frame, width=25, takefocus=True)
task_text.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

# Add button
task_add_btn = tk.Button(frame, text="Add Task", command= tsk_add_func, takefocus=False)
task_add_btn.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
 
# Task list box
task_lst = tk.Listbox(frame, width=50, height=10)
task_lst.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky=tk.W+tk.E+tk.N+tk.S)

# Delete button
del_btn = tk.Button(frame, text="Delete Task", command=del_tsk_func)
del_btn.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

# Mark as complete button
comp_btn = tk.Button(frame, text="Mark task completed", command=mark_comp_func)
comp_btn.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

# Clear completed task button
comp_tsk_btn = tk.Button(frame, text="Clear completed Tasks", command=tsk_comp_func)
comp_tsk_btn.grid(row=2, column=2, padx=5, pady=5,sticky=tk.W)

# Frame for completed tasks
frame2 = tk.Frame()
frame2.grid(row=1, column=0, sticky=tk.W + tk.E + tk.N + tk.S)
 
# Completed tasks list box
comp_lst = tk.Listbox(frame2, width=50, height=5,activestyle="none")
comp_lst.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)
 
# Set focus on the task_text widget
task_text.focus_set()
root.mainloop()