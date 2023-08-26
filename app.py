from tkinter import *

def move_up(event):
    label.place(x=label.winfo_x(),y=label.winfo_y()-10)
def move_down(event):
    label.place(x=label.winfo_x(),y=label.winfo_y()+10)
def move_left(event):
    label.place(x=label.winfo_x()-10,y=label.winfo_y())
def move_right(event):
    label.place(x=label.winfo_x()+10,y=label.winfo_y())

root = Tk()
root.title("Car")
root.geometry("500x500")

root.bind("<w>",move_up)
root.bind("<a>",move_left)
root.bind("<d>",move_right)
root.bind("<s>",move_down)
root.bind("<Up>",move_up)
root.bind("<Left>",move_left)
root.bind("<Right>",move_right)
root.bind("<Down>",move_down)

label = Label(root,bg='red')
label.place(x=0,y=0)



root.mainloop()