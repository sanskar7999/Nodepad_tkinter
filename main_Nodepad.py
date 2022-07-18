from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as tmsg
import os

from click import command 

def new():
    root.title(" Untitled - Notepad")
    file = None
    text.delete(1.0 , END)

def openfile():
    global file
    file = filedialog.askopenfilename(defaultextension=".txt"  ,filetypes=[("All Files" , "*.*") , ("Text Documents" , "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        text.delete(1.0  ,END)
       
        f =open(file , "r")
        text.insert(1.0 , f.read())
        f.close()

def savefile():
    global file
    file = filedialog.asksaveasfilename( initialfile= "untitledtxt",defaultextension=".txt"  ,filetypes=[("All Files" , "*.*") , ("Text Documents" , "*.txt")])

    if file == "":
        file = None
    else:
        f = open (file, "w")
        f.write(text.get(1.0, END) )
        f.close()

        
        root.title(os.path.basename(file) + " - Notepad")
 

def saveasfile():
    global file
    if file:
        f = open(file , 'w')
        f.write(text.get(1.0  ,END))
        f.close()
    
            
def cut():
    text.event_generate(("<<Cut>>"))

def copy():
    text.event_generate(("<<Copy>>"))

def paste():

    text.event_generate(("<<Paste>>"))


def about():
    tmsg.showinfo("About us" , "This nodepad made by sanskar sahu")
    

root = Tk()
root.title(" Untitled - Notepad")
# root.iconbitmap("apple.ico")

#-----This is menu bar------
mainmenu = Menu(root)

# ----------- file menu ----
sub_menu = Menu(mainmenu , tearoff=0)
sub_menu.add_command(label="new file"  ,command=new)
sub_menu.add_command(label="open file" , command=openfile)
sub_menu.add_separator()
sub_menu.add_command(label="Save" , command=savefile)
sub_menu.add_command(label="Save as" , command=saveasfile)
sub_menu.add_separator()
sub_menu.add_command(label="exit" , command=quit)
mainmenu.add_cascade(label="File" , menu=sub_menu)

# ----------- edit menu ----
edit_menu = Menu(mainmenu , tearoff=0)
edit_menu.add_command(label="cut" , command=cut)
edit_menu.add_command(label="copy" , command=copy)
edit_menu.add_command(label="Paste" , command=paste)
mainmenu.add_cascade(label="Edit" , menu=edit_menu)

    


# ---------help menu---

help_menu = Menu(mainmenu , tearoff=0)
help_menu.add_command(label="about us" , command=about)
mainmenu.add_cascade(label="Help" , menu=help_menu)

root.config(menu=mainmenu)


#------- scrollbar -----------
scrol = Scrollbar()
scrol.pack(side=RIGHT , fill=Y)
text= Text(root ,font=("lucida" , 13), yscrollcommand=scrol.set )
text.pack( expand=True,fill=BOTH)
scrol.config(command=text.yview)

root.mainloop()