#   imports ///////////////////////////////////////////////////////////////////////////////////////////////////////////
import random
from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import ttk
import time
from tkinter.ttk import *
import random


#   functions declarations and definitions ////////////////////////////////////////////////////////////////////////////
def changecolor():
    color = colorchooser.askcolor()
    print(color)
    colorHex = color[1]
    window.config(bg=colorHex)  ##e0b761


def submit():
    input = text.get("1.0", END)
    print(input)


def download():
    print("sal")
    x = 1
    while x <= 100:
        coef = random.randrange(0, 6)
        progressbar1['value'] += coef + 1
        window.update_idletasks()
        time.sleep(0.1)
        x = x + coef + 1
    progressbar1['value'] = 0


def openfile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\lpadurean\\PycharmProjects\\pythonProject\\",
                                          title="open your file mister",
                                          filetypes=(("text files", "*.txt"), ("all files,", "*.*")))
    print(filepath)
    file = open(filepath, 'r')
    print(file.read())
    #
    file.close()


def save():
    file = filedialog.asksaveasfile(defaultextension='.txt',
                                    filetypes=[("Text file", ".txt"), ("HTML file", ".html")])
    filetext = str(text.get("1.0", END))
    file.write(filetext)
    file.close()
    # file = open(filepath, 'w')
    if file is None:  # this line covers the case in which the user won't choose any file and exits the prompt
        return


def functionevent1(event):
    print("ai apasat tasta: " + event.keysym)


#   main window declaration //////////////////////////////////////////////////////////////////////////////////////////
window = Tk()

#   widget declarations and configuration
button = Button(text="download", command=download)
text = Text(window)
button_s = Button(window, text="submit", command=submit)
menubar = Menu(window)
notebook = ttk.Notebook(window)
frame_download_progressbar = Frame(window)
progressbar1 = Progressbar(frame_download_progressbar, orient=HORIZONTAL, length=333)
tab1 = Frame(notebook)
tab2 = Frame(notebook)
notebook.add(tab1, text="tab1")
notebook.add(tab2, text="tab2")
Filemenu = Menu(menubar, tearoff=0)
Viewmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=Filemenu)
menubar.add_cascade(label="View", menu=Viewmenu)
Filemenu.add_command(label="Open File", command=openfile)
Filemenu.add_command(label="Save File", command=save)
Filemenu.add_separator()
Filemenu.add_command(label="Exit", command=quit)
Viewmenu.add_command(label="Color", command=changecolor)

#   packing /// placing //////////////////////////////////////////////////////////////////////////////////////////////
button.pack(side=BOTTOM)
frame_download_progressbar.place(x=933, y=688)  # to be redone
notebook.pack(expand=TRUE, fill="both")
text.pack(side=TOP)
button_s.pack(side=BOTTOM)
progressbar1.pack(pady=5)

#   main window configuration ////////////////////////////////////////////////////////////////////////////////////////
window.bind("<Key>", functionevent1)
window.minsize(1280, 720)  # sets the window minimum size to 1024x768px
window.geometry("1280x720")
window.title("Log Analyzer")
window.config(menu=menubar)

#   mainloop /////////////////////////////////////////////////////////////////////////////////////////////////////////
window.mainloop()
