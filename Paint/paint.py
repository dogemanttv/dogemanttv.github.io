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
import sys
import io
from PIL import Image, ImageDraw, ImageTk
root = tk.Tk()
root.title("Paint")
root.geometry("800x500")
root.resizable(False, False)
size = 'medium'
color = 0, 0, 0
mousex = 0
mousey = 0
count = 0
debug = False
menubar = Menu(root)
root.config(menu=menubar)
fileMenu = Menu(menubar, tearoff=False)
colorMenu = Menu(menubar, tearoff=False)
sizeMenu = Menu(menubar, tearoff=False)
optionsMenu = Menu(menubar, tearoff=False)
load = Image.new(mode="RGBA", size=(800,500), color="white")
render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.image = render
del render
img.place(x=0, y=0)
def red():
    globals()['color'] = 255, 0, 0
def blue():
    globals()['color'] = 0, 0, 255
def pink():
    globals()['color'] = 255, 0, 255
def green():
    globals()['color'] = 0, 255, 0
def yellow():
    globals()['color'] = 255, 255, 0
def orange():
    globals()['color'] = 255, 128, 0
def purple():
    globals()['color'] = 127, 0, 255
def white():
    globals()['color'] = 255, 255, 255
def black():
    globals()['color'] = 0, 0, 0
def new():
    globals()['load'] = Image.new(mode="RGBA", size=(1920,1080), color="white")
    globals()['load'] = load.resize((800, 500))
    globals()['render'] = ImageTk.PhotoImage(load)
    globals()['img'] = Label(root, image=render)
    globals()['img'].image = render
    globals()['img'].place(x=0, y=0)
def small():
    globals()['size'] = 'small'
def medium():
    globals()['size'] = 'medium'
def large():
    globals()['size'] = 'large'
def debug():
    globals()['debug'] = not globals()['debug']
fileMenu.add_command(label="New", command=new)
fileMenu.add_command(label="Save")
fileMenu.add_command(label="Open")
fileMenu.add_command(label="Close")
menubar.add_cascade(label="File", menu=fileMenu)
colorMenu.add_radiobutton(label="Red", command=red)
colorMenu.add_radiobutton(label="Blue", command=blue)
colorMenu.add_radiobutton(label="Pink", command=pink)
colorMenu.add_radiobutton(label="Green", command=green)
colorMenu.add_radiobutton(label="Yellow", command=yellow)
colorMenu.add_radiobutton(label="Orange", command=orange)
colorMenu.add_radiobutton(label="Purple", command=purple)
colorMenu.add_radiobutton(label="White", command=white)
colorMenu.add_radiobutton(label="Black", command=black)
menubar.add_cascade(label="Colors", menu=colorMenu)
sizeMenu.add_radiobutton(label="Small", command=small)
sizeMenu.add_radiobutton(label="Medium", command=medium)
sizeMenu.add_radiobutton(label="Large", command=large)
menubar.add_cascade(label="Size", menu=sizeMenu)
optionsMenu.add_radiobutton(label="Debug", command=debug)
menubar.add_cascade(label="Options", menu=optionsMenu)
"""
def motion(event):
    x, y = event.x, event.y
    globals()['mousex'] = event.x
    globals()['mousey'] = event.y
    #print('{}, {}'.format(x, y))

def leftclick(event):
    print("LeftClick")
    print(globals()['mousex'], globals()['mousey'])
    if (globals()['size'] == 'smallest'):
      load.putpixel((globals()['mousex'], globals()['mousey']), globals()['color'])
    if (globals()['size'] == 'small'):
      load.putpixel((globals()['mousex'], globals()['mousey']), globals()['color'])
      load.putpixel((globals()['mousex'], globals()['mousey'] + 1), globals()['color'])
      load.putpixel((globals()['mousex'] + 1, globals()['mousey']), globals()['color'])
      load.putpixel((globals()['mousex'] - 1, globals()['mousey']), globals()['color'])
      load.putpixel((globals()['mousex'], globals()['mousey'] - 1), globals()['color'])
    if (globals()['size'] == 'medium'):
      load.putpixel((globals()['mousex'], globals()['mousey']), globals()['color'])
      load.putpixel((globals()['mousex'] + 1, globals()['mousey']), globals()['color'])
      load.putpixel((globals()['mousex'] + 2, globals()['mousey']), globals()['color'])
      load.putpixel((globals()['mousex'] - 1, globals()['mousey']), globals()['color'])
      load.putpixel((globals()['mousex'] - 2, globals()['mousey']), globals()['color'])
      load.putpixel((globals()['mousex'], globals()['mousey'] + 1), globals()['color'])
      load.putpixel((globals()['mousex'] - 1, globals()['mousey'] + 1), globals()['color'])
      load.putpixel((globals()['mousex'] + 1, globals()['mousey'] + 1), globals()['color'])
      load.putpixel((globals()['mousex'], globals()['mousey'] + 2), globals()['color'])
      load.putpixel((globals()['mousex'], globals()['mousey'] - 1), globals()['color'])
      load.putpixel((globals()['mousex'] - 1, globals()['mousey'] - 1), globals()['color'])
      load.putpixel((globals()['mousex'] + 1, globals()['mousey'] - 1), globals()['color'])
      load.putpixel((globals()['mousex'], globals()['mousey'] - 2), globals()['color'])
    if (globals()['size'] == 'large'):
      load.putpixel((globals()['mousex'], globals()['mousey']), globals()['color'])
      load.putpixel((globals()['mousex'] + 1, globals()['mousey']), globals()['color'])
      load.putpixel((globals()['mousex'] + 2, globals()['mousey']), globals()['color'])
      load.putpixel((globals()['mousex'] + 3, globals()['mousey']), globals()['color'])
      load.putpixel((globals()['mousex'] - 1, globals()['mousey']), globals()['color'])
      load.putpixel((globals()['mousex'] - 2, globals()['mousey']), globals()['color'])
      load.putpixel((globals()['mousex'] - 3, globals()['mousey']), globals()['color'])
      load.putpixel((globals()['mousex'], globals()['mousey'] + 1), globals()['color'])
      load.putpixel((globals()['mousex'] - 1, globals()['mousey'] + 1), globals()['color'])
      load.putpixel((globals()['mousex'] + 1, globals()['mousey'] + 1), globals()['color'])
      load.putpixel((globals()['mousex'] - 2, globals()['mousey'] + 1), globals()['color'])
      load.putpixel((globals()['mousex'] + 2, globals()['mousey'] + 1), globals()['color'])
      load.putpixel((globals()['mousex'], globals()['mousey'] + 2), globals()['color'])
      load.putpixel((globals()['mousex'] - 1, globals()['mousey'] + 2), globals()['color'])
      load.putpixel((globals()['mousex'] + 1, globals()['mousey'] + 2), globals()['color'])
      load.putpixel((globals()['mousex'], globals()['mousey'] - 1), globals()['color'])
      load.putpixel((globals()['mousex'] - 1, globals()['mousey'] - 1), globals()['color'])
      load.putpixel((globals()['mousex'] + 1, globals()['mousey'] - 1), globals()['color'])
      load.putpixel((globals()['mousex'] - 2, globals()['mousey'] - 1), globals()['color'])
      load.putpixel((globals()['mousex'] + 2, globals()['mousey'] - 1), globals()['color'])
      load.putpixel((globals()['mousex'], globals()['mousey'] - 2), globals()['color'])
      load.putpixel((globals()['mousex'] - 1, globals()['mousey'] - 2), globals()['color'])
      load.putpixel((globals()['mousex'] + 1, globals()['mousey'] - 2), globals()['color'])
    render = ImageTk.PhotoImage(load)
    img = Label(root, image=render)
    img.image = render
    img.place(x=0, y=0)
"""
def leftclick(event):
    global img
    global load
    global render
    print("LeftClick")
    print(event.x, event.y)
    if (globals()['size'] == 'smallest'):
      load.putpixel((event.x, event.y), globals()['color'])
    if (globals()['size'] == 'small'):
      load.putpixel((event.x, event.y), globals()['color'])
      load.putpixel((event.x, event.y + 1), globals()['color'])
      load.putpixel((event.x + 1, event.y), globals()['color'])
      load.putpixel((event.x - 1, event.y), globals()['color'])
      load.putpixel((event.x, event.y - 1), globals()['color'])
    if (globals()['size'] == 'medium'):
      load.putpixel((event.x, event.y), globals()['color'])
      load.putpixel((event.x + 1, event.y), globals()['color'])
      load.putpixel((event.x + 2, event.y), globals()['color'])
      load.putpixel((event.x - 1, event.y), globals()['color'])
      load.putpixel((event.x - 2, event.y), globals()['color'])
      load.putpixel((event.x, event.y + 1), globals()['color'])
      load.putpixel((event.x - 1, event.y + 1), globals()['color'])
      load.putpixel((event.x + 1, event.y + 1), globals()['color'])
      load.putpixel((event.x, event.y + 2), globals()['color'])
      load.putpixel((event.x, event.y - 1), globals()['color'])
      load.putpixel((event.x - 1, event.y - 1), globals()['color'])
      load.putpixel((event.x + 1, event.y - 1), globals()['color'])
      load.putpixel((event.x, event.y - 2), globals()['color'])
    if (globals()['size'] == 'large'):
      load.putpixel((event.x, event.y), globals()['color'])
      load.putpixel((event.x + 1, event.y), globals()['color'])
      load.putpixel((event.x + 2, event.y), globals()['color'])
      load.putpixel((event.x + 3, event.y), globals()['color'])
      load.putpixel((event.x - 1, event.y), globals()['color'])
      load.putpixel((event.x - 2, event.y), globals()['color'])
      load.putpixel((event.x - 3, event.y), globals()['color'])
      load.putpixel((event.x, event.y + 1), globals()['color'])
      load.putpixel((event.x - 1, event.y + 1), globals()['color'])
      load.putpixel((event.x + 1, event.y + 1), globals()['color'])
      load.putpixel((event.x - 2, event.y + 1), globals()['color'])
      load.putpixel((event.x + 2, event.y + 1), globals()['color'])
      load.putpixel((event.x, event.y + 2), globals()['color'])
      load.putpixel((event.x - 1, event.y + 2), globals()['color'])
      load.putpixel((event.x + 1, event.y + 2), globals()['color'])
      load.putpixel((event.x, event.y - 1), globals()['color'])
      load.putpixel((event.x - 1, event.y - 1), globals()['color'])
      load.putpixel((event.x + 1, event.y - 1), globals()['color'])
      load.putpixel((event.x - 2, event.y - 1), globals()['color'])
      load.putpixel((event.x + 2, event.y - 1), globals()['color'])
      load.putpixel((event.x, event.y - 2), globals()['color'])
      load.putpixel((event.x - 1, event.y - 2), globals()['color'])
      load.putpixel((event.x + 1, event.y - 2), globals()['color'])
    render = ImageTk.PhotoImage(load)
    img.destroy()
    img = Label(root, image=render)
    img.image = render
    del render
    img.place(x=0, y=0)
    globals()['count'] += 1
#root.bind("<Button-1>", leftclick)
root.bind("<B1-Motion>", leftclick)
#root.bind('<Motion>', motion)
root.mainloop()