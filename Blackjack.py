import tkinter as tk 
from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox
from tkinter import Menu
from tkinter import ttk
import os

### variables

money = '3142'

moneysh = money + '$'

root = Tk()
root.geometry("900x900")
root.title('Blackjack')
root.iconphoto(False, tk.PhotoImage(file='icon.png'))
root.resizable(False,False)

### image download

img1 = ImageTk.PhotoImage(Image.open('img.png'))
img2 = ImageTk.PhotoImage(Image.open('img1.png'))
img3 = ImageTk.PhotoImage(Image.open('img2.png'))

### image cards

kw1 = ImageTk.PhotoImage(Image.open('kw1.png'))

### widgets

bg = tk.PhotoImage(file='bg.png')  ### Background image
label_for_image= Label(root, image=bg)
label_for_image.place(x=0,y=0)

moneylbl = tk.Label(root,bg='#d5d5d5',image=img1)
moneylbl.place(x=220,y=800)
moneylbl1 = tk.Label(root,bg='#515151',text=moneysh,font=('Arial Bold', 18),fg='white')
moneylbl1.place(x=230,y=812)

hitbtn = tk.Button(root,bg='#d5d5d5',image=img2,border='0')
hitbtn.place(x=550,y=750)

standbtn = tk.Button(root,bg='#d5d5d5',image=img3,border='0')
standbtn.place(x=730,y=750)

cardlbl1 = tk.Label(root,bg='#139415',image=kw1,border='0')
cardlbl1.place(x=400,y=550)


root.mainloop()