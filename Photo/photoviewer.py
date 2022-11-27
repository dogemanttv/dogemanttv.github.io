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
from PIL import Image, ImageTk
root = tk.Tk()
root.title("Photo Viewer")
root.geometry("800x500")
root.resizable(False, False) 
def openfile():
    print('Opening File Picker...')
    filetypes = (
        ('All files', '*.*'),
        ('PNG files', '*.png'),
        ('JPG files', '*.jpg'),
        ('JPEG files', '*.jpeg')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    print("File picked: " + filename)
    root.title("Photo Viewer: " + filename)
    load = Image.open(filename)
    resizedimg = load.resize((600, 338))
    render = ImageTk.PhotoImage(resizedimg)
    img = Label(root, image=render)
    img.image = render
    img.place(x=100, y=50)
openPhoto = tk.Button(root, text="Open Photo", command=openfile)
openPhoto.place(x=350,y=400)
root.mainloop()