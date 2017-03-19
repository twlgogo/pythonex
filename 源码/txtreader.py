from tkinter import *

def hello():
	print("hello123")
	
win = Tk()
win.title("first win")
win.geometry('200x100')

btn = Button(win,text = 'Hello',command = hello)
btn.pack(expand=YES,fill=BOTH)

mainloop()