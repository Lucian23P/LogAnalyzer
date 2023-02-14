from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog

def changecolor():
    color = colorchooser.askcolor()
    print(color)
    colorHex = color[1]
    window.config(bg=colorHex) ##e0b761

def submit():
    input = text.get("1.0", END)
    print(input)

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
    #file = open(filepath, 'w')
    if file is None: #   this line covers the case in which the user won't choose any file and exits the prompt
        return

window = Tk()
#button = Button(text="color!", command=changecolor)
window.geometry("420x520")

menubar = Menu(window)
window.config(menu=menubar)

Filemenu = Menu(menubar, tearoff=0)
Viewmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=Filemenu)
menubar.add_cascade(label="View", menu=Viewmenu)
Filemenu.add_command(label="Open File", command=openfile)
Filemenu.add_command(label="Save File", command=save)
Filemenu.add_separator()
Filemenu.add_command(label="Exit", command=quit)
Viewmenu.add_command(label="Color", command=changecolor)

#button_save = Button(window, text="save", command=save)
#button_file = Button(window, text="file", command=openfile)
text = Text(window)
button_s = Button(window, text="submit", command=submit)

window.minsize(300, 500) # sets the window minimum size to 300x500px
#button_save.pack(side = TOP)
text.pack(side = TOP)
#button.pack(side = BOTTOM)
#button_file.pack(side = BOTTOM)
button_s.pack(side = BOTTOM)
window.mainloop()