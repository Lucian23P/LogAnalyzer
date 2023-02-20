#   imports ///////////////////////////////////////////////////////////////////////////////////////////////////////////
import random
from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import ttk
import time
from tkinter.ttk import *
import random
import smtplib


# global variables ////////////////////////////////////////////////////////////////////////////////////////////////////
# email_service global variables:
email_sender = ""  # set_email_sender()
email_receiver = ""  # set_email_receiver()
email_sender_password = ""  # set_email_sender_password()
email_subject = ""  # set_email_subject()
email_body = ""  # set_email_body()
email_message = ""  # set email message


#   functions declarations and definitions ////////////////////////////////////////////////////////////////////////////
def changecolor():
    color = colorchooser.askcolor()
    print(color)
    colorHex = color[1]
    window.config(bg=colorHex)  ##e0b761


def submit():
    email_message = text.get("1.0", END)
    create_email_window()


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


def print_coordinates1():
    print("Cursor location: " + str(Event.x) + "," + str(Event.y))


def email_send():
    # email functionality
    server1 = smtplib.SMTP("smtp.gmail.com", 587)
    server1.starttls()
    server1.login(email_sender, email_sender_password)
    print("Logged in...")
    server1.sendmail(email_sender, email_receiver, email_message)


def create_email_window():
    new_window = Toplevel()

    label_email_sender = Label(new_window, text="Sender", width=16)
    label_email_receiver = Label(new_window, text="Receiver")
    label_email_password = Label(new_window, text="Password")
    label_email_subject = Label(new_window, text="Subject")

    email_sender_EB = Entry(new_window, width=50)
    email_receiver_EB = Entry(new_window, width=50)
    email_sender_password_EB = Entry(new_window, width=50)
    email_subject_EB = Entry(new_window, width=50)

    button_send_email = Button(new_window, text="Send E-mail")  # , command=email_send)

    email_sender_EB.insert(0, '@gmail.com')
    email_receiver_EB.insert(0, '@gmail.com')
    email_sender_password_EB.config(show="$")

    # email_grid:
    label_email_sender.grid(row=0, column=0)
    label_email_password.grid(row=1, column=0)
    label_email_receiver.grid(row=2, column=0)
    label_email_subject.grid(row=3, column=0)

    email_sender_EB.grid(row=0, column=1)
    email_receiver_EB.grid(row=2, column=1)
    email_sender_password_EB.grid(row=1, column=1)
    email_subject_EB.grid(row=3, column=1)
    button_send_email.grid(row=4, column=0, columnspan=2)

    email_sender = email_sender_EB.get()
    email_receiver = email_receiver_EB.get()
    email_sender_password = email_sender_password_EB.get()
    email_subject = email_subject_EB.get()
    email_body = """Hello {},
    {}
    Have a good day,
    {}
    """.format(email_receiver, email_message, email_sender)

    new_window.geometry("430x112")


#   main window declaration //////////////////////////////////////////////////////////////////////////////////////////
window = Tk()

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
#button_send_email.pack()

#   main window configuration ////////////////////////////////////////////////////////////////////////////////////////
window.minsize(1280, 720)  # sets the window minimum size to 1024x768px
window.geometry("1280x720")
window.title("Log Analyzer")
window.config(menu=menubar)

# keys and mouse actions /////////////////////////////////////////////////////////////////////////////////////////////
window.bind("<Key>", functionevent1) # pairs a key press event with a function
#window.bind("Motion", print_coordinates1()) # motion is used for coordinates of the cursor
#window.bind("Button-1", functionevent3()) # binds mouse button 1
#window.bind("Enter", print_coordinates_click())
#window.bind("Release", print_coordinates_releaseclick())


#   mainloop /////////////////////////////////////////////////////////////////////////////////////////////////////////
window.mainloop()


"""
from tkinter import *

email_sender = ""  # set_email_sender()
email_receiver = ""  # set_email_receiver()
email_sender_password = ""  # set_email_sender_password()
email_subject = ""  # set_email_subject()
email_body = ""  # set_email_body()
email_message = ""  # set email message

def submitbody():
    email_sender = email_sender_EB.get()
    email_receiver = email_receiver_EB.get()
    email_sender_password = email_sender_password_EB.get()
    email_subject = email_subject_EB.get()
 #   email_body = """"""Hello {},
        {}
        Have a good day,
        {}
        """""".format(email_receiver, email_message, email_sender)
    print(email_body)

new_window = Tk()
label_email_sender = Label(new_window, text="Sender", width=16)
label_email_receiver = Label(new_window, text="Receiver")
label_email_password = Label(new_window, text="Password")
label_email_subject = Label(new_window, text="Subject")

email_sender_EB = Entry(new_window, width=50)
email_receiver_EB = Entry(new_window, width=50)
email_sender_password_EB = Entry(new_window, width=50)
email_subject_EB = Entry(new_window, width=50)

button_send_email = Button(new_window, text="Send E-mail",  command=submitbody) #, command=email_send)

email_sender_EB.insert(0, '@gmail.com')
email_receiver_EB.insert(0, '@gmail.com')
email_sender_password_EB.config(show="$")

# email_grid:
label_email_sender.grid(row=0, column=0)
label_email_password.grid(row=1, column=0)
label_email_receiver.grid(row=2, column=0)
label_email_subject.grid(row=3, column=0)

email_sender_EB.grid(row=0, column=1)
email_receiver_EB.grid(row=1, column=1)
email_sender_password_EB.grid(row=2, column=1)
email_subject_EB.grid(row=3, column=1)
button_send_email.grid(row=4, column=0, columnspan=2)

#button_body = Button(new_window, text="scrie", command=submitbody)

#button_body.pack()
new_window.geometry("430x112")
new_window.mainloop()

"""