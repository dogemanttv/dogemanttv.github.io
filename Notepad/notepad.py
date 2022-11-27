from curses.textpad import Textbox
from email.mime import base
import tkinter as tk
from tkinter import Menu, PhotoImage, Text
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import re
import zlib,base64
import os
import tempfile
root = tk.Tk()
root.title("Notepad")

ICON = (b"")

_, ICON_PATH = tempfile.mkstemp()
with open(ICON_PATH, 'wb') as icon_file:
    icon_file.write(ICON)
root.iconbitmap(default=ICON_PATH)
def resource_path(relative):
    return os.path.join(
        os.environ.get(
            "_MEIPASS2",
            os.path.abspath(".")
        ),
        relative
    )
#root.tk.call('wm', 'iconphoto', root._w, base64.b64decode(base64icon))
root.geometry("500x500")
def save():
    global savedfilename
    print('Saving...')
    text=Notepad.get("1.0","end-1c")
    #check if you already opened a file to set as default name
    if ('openedfilename' in globals()):
        filepicker=fd.asksaveasfile(initialfile = openedfilename,defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")],mode='w')
        try:
            filepicker.write(text)
            filepicker.close()
            root.title("Notepad: " + filepicker.name) 
            savedfilename = filepicker.name.split('/').pop()
        except:
            print ("Write Error!")
    elif ('savedfilename' in globals()):
        filepicker=fd.asksaveasfile(initialfile = savedfilename,defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")],mode='w')
        try:
            filepicker.write(text)
            filepicker.close()
            root.title("Notepad: " + filepicker.name)
            savedfilename = filepicker.name.split('/').pop()
        except:
            print ("Write Error!")
    else:
        filepicker=fd.asksaveasfile(initialfile = '.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")],mode='w')
        try:
            filepicker.write(text)
            filepicker.close()
            root.title("Notepad: " + filepicker.name)
            savedfilename = filepicker.name.split('/').pop()
        except :
            print ("Write Error!")
def openfile():
    print('Opening File Picker...')
    filetypes = (
        ('All files', '*.*'),
        ('text files', '*.txt')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    print("File picked: " + filename)
    root.title("Notepad: " + filename)
    global openedfilename
    openedfilename = filename.split('/').pop()
    Notepad.delete("1.0","end-1c")
    Notepad.insert("end-1c", open(filename,'r').read())
#a = Label(root, text ="Hello World")
#a.pack()
#btn = Button(root, text = "Save" ,fg = "black", command=save)
#btn.pack()
Notepad = Text(root)
Notepad.pack(expand=True, fill='both')
menubar = Menu(root)
root.config(menu=menubar)
fileMenu = Menu(menubar, tearoff=False)
fileMenu.add_command(label="Save",command=save)
fileMenu.add_command(label="Open",command=openfile)
fileMenu.add_command(label="Exit",command=root.destroy)
menubar.add_cascade(label="File", menu=fileMenu)
root.mainloop()
