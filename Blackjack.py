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

### cards images

### karo

kw1 = ImageTk.PhotoImage(Image.open('kw1.png'))
kw2 = ImageTk.PhotoImage(Image.open('kw2.png'))
kw3 = ImageTk.PhotoImage(Image.open('kw3.png'))
kw4 = ImageTk.PhotoImage(Image.open('kw4.png'))
kw5 = ImageTk.PhotoImage(Image.open('kw5.png'))
kw6 = ImageTk.PhotoImage(Image.open('kw6.png'))
kw7 = ImageTk.PhotoImage(Image.open('kw7.png'))
kw8 = ImageTk.PhotoImage(Image.open('kw8.png'))
kw9 = ImageTk.PhotoImage(Image.open('kw9.png'))
kw10 = ImageTk.PhotoImage(Image.open('kw10.png'))
kwA = ImageTk.PhotoImage(Image.open('kwA.png'))
kwK = ImageTk.PhotoImage(Image.open('kwK.png'))
kwQ = ImageTk.PhotoImage(Image.open('kwQ.png'))
kwJ = ImageTk.PhotoImage(Image.open('kwJ.png'))

### serce

se1 = ImageTk.PhotoImage(Image.open('se1.png'))
se2 = ImageTk.PhotoImage(Image.open('se2.png'))
se3 = ImageTk.PhotoImage(Image.open('se3.png'))
se4 = ImageTk.PhotoImage(Image.open('se4.png'))
se5 = ImageTk.PhotoImage(Image.open('se5.png'))
se6 = ImageTk.PhotoImage(Image.open('se6.png'))
se7 = ImageTk.PhotoImage(Image.open('se7.png'))
se8 = ImageTk.PhotoImage(Image.open('se8.png'))
se9 = ImageTk.PhotoImage(Image.open('se9.png'))
se10 = ImageTk.PhotoImage(Image.open('se10.png'))
seA = ImageTk.PhotoImage(Image.open('seA.png'))
seK = ImageTk.PhotoImage(Image.open('seK.png'))
seQ = ImageTk.PhotoImage(Image.open('seQ.png'))
seJ = ImageTk.PhotoImage(Image.open('seJ.png'))

### pik

pi1 = ImageTk.PhotoImage(Image.open('pi1.png'))
pi2 = ImageTk.PhotoImage(Image.open('pi2.png'))
pi3 = ImageTk.PhotoImage(Image.open('pi3.png'))
pi4 = ImageTk.PhotoImage(Image.open('pi4.png'))
pi5 = ImageTk.PhotoImage(Image.open('pi5.png'))
pi6 = ImageTk.PhotoImage(Image.open('pi6.png'))
pi7 = ImageTk.PhotoImage(Image.open('pi7.png'))
pi8 = ImageTk.PhotoImage(Image.open('pi8.png'))
pi9 = ImageTk.PhotoImage(Image.open('pi9.png'))
pi10 = ImageTk.PhotoImage(Image.open('pi10.png'))
piA = ImageTk.PhotoImage(Image.open('piA.png'))
piK = ImageTk.PhotoImage(Image.open('piK.png'))
piQ = ImageTk.PhotoImage(Image.open('piQ.png'))
piJ = ImageTk.PhotoImage(Image.open('piJ.png'))

### trefl

tr1 = ImageTk.PhotoImage(Image.open('tr1.png'))
tr2 = ImageTk.PhotoImage(Image.open('tr2.png'))
tr3 = ImageTk.PhotoImage(Image.open('tr3.png'))
tr4 = ImageTk.PhotoImage(Image.open('tr4.png'))
tr5 = ImageTk.PhotoImage(Image.open('tr5.png'))
tr6 = ImageTk.PhotoImage(Image.open('tr6.png'))
tr7 = ImageTk.PhotoImage(Image.open('tr7.png'))
tr8 = ImageTk.PhotoImage(Image.open('tr8.png'))
tr9 = ImageTk.PhotoImage(Image.open('tr9.png'))
tr10 = ImageTk.PhotoImage(Image.open('tr10.png'))
trA = ImageTk.PhotoImage(Image.open('trA.png'))
trK = ImageTk.PhotoImage(Image.open('trK.png'))
trQ = ImageTk.PhotoImage(Image.open('trQ.png'))
trJ = ImageTk.PhotoImage(Image.open('trJ.png'))

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