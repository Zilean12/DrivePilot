
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import Toplevel, Label, messagebox
import os
from datetime import datetime
import tkinter as tk
import datetime
import pickle
import sys
import os
import GUItest01

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# connecting to upload python file
def upload():
    from upload import Uploaded  
    new_window = root
    app = Uploaded(new_window)

#  connecting to the download file
def download():
    from Download import Downloads 
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    app = Downloads(window, creds) 

# connecting to delete 
def Delete():
    from Delete import Deleteds 
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    app = Deleteds(window, creds) 

# connecting to View 
def View():
    from View import viewers  
    new_window = Toplevel(window)  
    app = viewers(new_window) 
    
# connecting to file Detail 
def fileDetail():
    from fileDetail import Detail  
    new_window = root
    app = Detail(new_window)

# connecting to Share 
def Share():
    from Share import Sender  
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    app = Sender(window, creds) 

# connecting to Search 
def Search():
    from Search import Finder  
    new_window = root
    app = Finder(new_window)

# connecting to Activity 
def Activity():
    from Activity import loger  
    new_window = root
    app = loger(new_window)

# connecting to List 
def List():
    from List import lists 
    new_window = root
    app = lists(new_window)

# connecting to Floder 
def FolderDetail():
    from FolderDetail import fold  
    new_window = root
    app = fold(new_window)

# connecting to Account 
def Account():
    from Account import AccountDE 
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    app = AccountDE(window, creds) 

# connecting to Storage 
def Storage():
    from Storage import Storages  
    new_window = root
    app = Storages(new_window)

# connecting to History 
def History():
    from History import Hist  
    new_window = root
    app = Hist(new_window)

# Access to ur location 
def location():
    from location import IPInfo  
    new_window = root
    app = IPInfo(new_window)

# Define a function to display the current date
def display_date():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    canvas.create_text(
        780.5166015625,61.1995849609375,
        anchor="nw",
        text=f"Date: {current_date}",
        fill="#FBF5F5",
        font=("FugazOne Regular", 18 * -1)
        )

# closing 
def close_window_and_confirm(window):
    def confirm_close():
        if messagebox.askokcancel("Close Program", "Are you sure you want to close the program?"):
            window.destroy()
    
    confirm_window = Toplevel(window)
    confirm_window.geometry("200x100")
    confirm_window.title("Confirm Close")
    
    label = Label(confirm_window, text="Close the program?")
    label.pack(pady=20)
    
    confirm_button = Button(confirm_window, text="Confirm", command=confirm_close)
    confirm_button.pack()

window = Tk()
window.geometry("1075x584")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 584,
    width = 1075,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.016845703125,
    0.0,
    1076.31396484375,
    584.0,
    fill="#000000",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    59.0,
    91.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=696.0,
    y=50.0,
    width=46.0,
    height=45.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=644.5166015625,
    y=51.0,
    width=43.4833984375,
    height=44.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=History,
    relief="flat"
)
button_3.place(
    x=48.0,
    y=263.0,
    width=43.0,
    height=39.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=Storage,
    relief="flat"
)
button_4.place(
    x=42.0,
    y=203.0,
    width=43.0,
    height=46.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=39.0,
    y=142.0,
    width=50.0,
    height=46.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=Account,
    relief="flat"
)
button_6.place(
    x=42.0,
    y=360.0,
    width=43.0,
    height=39.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png")
)
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: close_window_and_confirm(window),  # Open confirm window
    relief="flat"
)
button_7.place(
    x=46.0,
    y=483.0,
    width=43.0,
    height=39.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=location,
    relief="flat"
)
button_8.place(
    x=46.0,
    y=315.0,
    width=43.0,
    height=39.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=List,
    relief="flat"
)
button_9.place(
    x=198.0,
    y=257.05731201171875,
    width=187.11767578125,
    height=47.468505859375
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=View,
    relief="flat"
)
button_10.place(
    x=193.0,
    y=168.05731201171875,
    width=192.62158203125,
    height=47.47601318359375
)

canvas.create_text(
    780.5166015625,
    61.1995849609375,
    anchor="nw",
    text="Date:",
    fill="#FBF5F5",
    font=("FugazOne Regular", 18 * -1)
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=fileDetail,
    relief="flat"
)
button_11.place(
    x=469.930908203125,
    y=258.0,
    width=196.13824462890625,
    height=48.0
)

canvas.create_text(
    173.51220703125,
    61.1995849609375,
    anchor="nw",
    text="Welcome Back,",
    fill="#F9F0F0",
    font=("FugazOne Regular", 25 * -1)
)

button_image_12 = PhotoImage(
    file=relative_to_assets("button_12.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=Activity,
    relief="flat"
)
button_12.place(
    x=192.0003662109375,
    y=347.0001220703125,
    width=196.075927734375,
    height=52.999908447265625
)

button_image_13 = PhotoImage(
    file=relative_to_assets("button_13.png"))
button_13 = Button(
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=download,
    relief="flat"
)
button_13.place(
    x=473.0,
    y=163.00274658203125,
    width=193.0054931640625,
    height=50.25384521484375
)

button_image_14 = PhotoImage(
    file=relative_to_assets("button_14.png"))
button_14 = Button(
    image=button_image_14,
    borderwidth=0,
    highlightthickness=0,
    command=Search,
    relief="flat"
)
button_14.place(
    x=472.0032958984375,
    y=348.7420959472656,
    width=193.9967041015625,
    height=49.2578125
)

button_image_15 = PhotoImage(
    file=relative_to_assets("button_15.png"))
button_15 = Button(
    image=button_image_15,
    borderwidth=0,
    highlightthickness=0,
    command=Delete,
    relief="flat"
)
button_15.place(
    x=751.5272216796875,
    y=163.00341796875,
    width=195.54043579101562,
    height=46.99658203125
)

button_image_16 = PhotoImage(
    file=relative_to_assets("button_16.png"))
button_16 = Button(
    image=button_image_16,
    borderwidth=0,
    highlightthickness=0,
    command=FolderDetail,
    relief="flat"
)
button_16.place(
    x=753.0,
    y=257.156982421875,
    width=192.826171875,
    height=50.099365234375
)

button_image_17 = PhotoImage(
    file=relative_to_assets("button_17.png"))
button_17 = Button(
    image=button_image_17,
    borderwidth=0,
    highlightthickness=0,
    command=Share,
    relief="flat"
)
button_17.place(
    x=752.9323120117188,
    y=353.0,
    width=193.135498046875,
    height=47.0
)

button_image_18 = PhotoImage(
    file=relative_to_assets("button_18.png"))
button_18 = Button(
    image=button_image_18,
    borderwidth=0,
    highlightthickness=0,
    command=upload,
    relief="flat"
)
button_18.place(
    x=753.0032958984375,
    y=463.00274658203125,
    width=194.06439208984375,
    height=46.99725341796875
)

canvas.create_rectangle(
    163.5166015625,
    111.1995849609375,
    945.5166015625,
    113.1995849609375,
    fill="#FFF9F9",
    outline="")

def display_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    time_label.config(text=current_time)
    time_label.after(1000, display_time)

time_label = tk.Label(window, text="Time: ", font=("FugazOne Regular", 18 * -1), bg="#FBF5F5")
time_label.place(x=980.820327252, y=540.1995849609375)

# Call the function to display the Date and Time
display_time()
display_date()


window.resizable(False, False)
window.mainloop()
