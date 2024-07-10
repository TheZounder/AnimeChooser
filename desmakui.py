import tkinter as tk
from tkinter import ttk
import io
from random import choice

def choose():
    unreadlist = io.open("animelist.txt", "rb")
    dirtylist = unreadlist.readlines()
    cleanlist = [line.strip().decode('UTF-8') for line in dirtylist]

    chosen = choice(cleanlist)
    label.config(text=chosen)

window = tk.Tk()
window.geometry("860x809")
window.title("Anime Chooser!")

backimage = tk.PhotoImage(file = "ahegao.png")
backlabel = tk.Label(window, image=backimage)
backlabel.place(x=0, y=0, relwidth=1, relheight=1)

button = ttk.Button( 
    window, 
    text="Choose an anime for me!", 
    command=choose,
    padding=10
)

button.pack(pady=50)

label = tk.Label(
    window,
    text="Anime will be displayed here",
    borderwidth=2,
    relief="solid",
    padx=25,
    pady=25
)
label.pack(pady=20)

window.mainloop()