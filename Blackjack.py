import tkinter as tk 
from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox
from tkinter import Menu
from tkinter import ttk
import os

root = Tk()
root.geometry("900x900")
root.title('Blackjack')
root.iconphoto(False, tk.PhotoImage(file='icon.png'))
root.resizable(False,False)

bg = tk.PhotoImage(file='bg.png')  ### Background image
label_for_image= Label(root, image=bg)
label_for_image.place(x=0,y=0)

print()

root.mainloop()