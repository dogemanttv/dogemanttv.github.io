from curses.textpad import Textbox
from email.mime import base
import tkinter as tk
from tkinter import *
from tkinter import Menu, PhotoImage, Text, messagebox
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import re
import zlib,base64
import os
import tempfile
root = tk.Tk()
root.title("Calculator")
root.geometry("300x500")
equationn = ''
def button1():
	global equationn
	equationn += '1'
	text.insert("end-1c", '1')
	print(equationn)
def button2():
	global equationn
	equationn += '2'
	text.insert("end-1c", '2')
	print(equationn)
def button3():
	global equationn
	equationn += '3'
	text.insert("end-1c", '3')
	print(equationn)
def button4():
	global equationn
	equationn += '4'
	text.insert("end-1c", '4')
	print(equationn)
def button5():
	global equationn
	equationn += '5'
	text.insert("end-1c", '5')
	print(equationn)
def button6():
	global equationn
	equationn += '6'
	text.insert("end-1c", '6')
	print(equationn)
def button7():
	global equationn
	equationn += '7'
	text.insert("end-1c", '7')
	print(equationn)
def button8():
	global equationn
	equationn += '8'
	text.insert("end-1c", '8')
	print(equationn)
def button9():
	global equationn
	equationn += '9'
	text.insert("end-1c", '9')
	print(equationn)
def button0():
	global equationn
	equationn += '0'
	text.insert("end-1c", '0')
	print(equationn)
def buttonplus():
	global equationn
	equationn += '+'
	text.insert("end-1c", '+')
	print(equationn)
def buttonminus():
	global equationn
	equationn += '-'
	text.insert("end-1c", '-')
	print(equationn)
def buttontimes():
	global equationn
	equationn += '*'
	text.insert("end-1c", '*')
	print(equationn)
def buttondivide():
	global equationn
	equationn += '/'
	text.insert("end-1c", '/')
	print(equationn)
def buttonperiod():
	global equationn
	equationn += '.'
	text.insert("end-1c", '.')
	print(equationn)
def clear():
	global equationn
	text.delete("1.0","end-1c")
	equationn = ''
	print(equationn)
def equate():
	global equationn
	text.delete("1.0","end-1c")
	text.insert("end-1c", eval(equationn))
	equationn = str(eval(equationn))
text_frame = tk.Frame(root, width=300, height=125)
text_frame.pack_propagate(False)
text_frame.pack()
text = tk.Text(text_frame, width=300, height=125, font=("Helvetica", 50))
text.bind("<Key>", lambda e: "break")
button1 = tk.Button(root, text='1', command=button1)
button1.place(x=0,y=125,height=60,width=60)
button2 = tk.Button(root, text='2', command=button2)
button2.place(x=60,y=125,height=60,width=60)
button3 = tk.Button(root, text='3', command=button3)
button3.place(x=120,y=125,height=60,width=60)
button4 = tk.Button(root, text='4', command=button4)
button4.place(x=180,y=125,height=60,width=60)
button5 = tk.Button(root, text='5', command=button5)
button5.place(x=0,y=185,height=60,width=60)
button6 = tk.Button(root, text='6', command=button6)
button6.place(x=60,y=185,height=60,width=60)
button7 = tk.Button(root, text='7', command=button7)
button7.place(x=120,y=185,height=60,width=60)
button8 = tk.Button(root, text='8', command=button8)
button8.place(x=180,y=185,height=60,width=60)
button9 = tk.Button(root, text='9', command=button9)
button9.place(x=0,y=245,height=60,width=60)
button0 = tk.Button(root, text='0', command=button0)
button0.place(x=60,y=245,height=60,width=60)
buttonplus = tk.Button(root, text='+', command=buttonplus)
buttonplus.place(x=240,y=125,height=60,width=60)
buttonminus = tk.Button(root, text='-', command=buttonminus)
buttonminus.place(x=240,y=185,height=60,width=60)
buttontimes = tk.Button(root, text='*', command=buttontimes)
buttontimes.place(x=240,y=245,height=60,width=60)
buttondivide = tk.Button(root, text='/', command=buttondivide)
buttondivide.place(x=240,y=305,height=60,width=60)
buttonperiod = tk.Button(root, text='.', command=buttonperiod)
buttonperiod.place(x=0,y=305,height=200,width=120)
clear = tk.Button(root, text='clear', command=clear)
clear.place(x=240,y=365,height=135,width=60)
buttonequate = tk.Button(root, text='=', command=equate)
buttonequate.place(x=120,y=245,height=255,width=120)

#text.configure(state="disabled")
text.pack(side="top", fill="both", expand=True)
#text.insert("end-1c", '5455')
root.resizable(False, False) 
menubar = Menu(root)
root.config(menu=menubar)
aboutMenu = Menu(menubar, tearoff=False)
def showAuthor():
    messagebox.showinfo("Author", "me is make this!! :D")
aboutMenu.add_command(label="Author", command=showAuthor)
menubar.add_cascade(label="About", menu=aboutMenu)
root.mainloop()