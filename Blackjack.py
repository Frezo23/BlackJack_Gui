import tkinter as tk 
from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox
from tkinter import Menu
from tkinter import ttk
import os
from cryptography.fernet import Fernet
import random
import datetime

### variables

money = 25
bet = 1500
bet_take = 0

betsh = str(bet) + '$'
moneysh = str(money) + '$'

### creating window

root = Tk()
root.geometry("900x900")
root.title('Blackjack')
root.iconphoto(False, tk.PhotoImage(file='icon.png'))
root.resizable(False,False)

### image download

img1 = ImageTk.PhotoImage(Image.open('img.png'))
img2 = ImageTk.PhotoImage(Image.open('img1.png'))
img3 = ImageTk.PhotoImage(Image.open('img2.png'))
img4 = ImageTk.PhotoImage(Image.open('img3.png'))

up = ImageTk.PhotoImage(Image.open('up.png'))
down = ImageTk.PhotoImage(Image.open('down.png'))

nocard = ImageTk.PhotoImage(Image.open('nocard.png'))

coins = ImageTk.PhotoImage(Image.open('coins.png'))
coins1 = ImageTk.PhotoImage(Image.open('coins1.png'))
coins2 = ImageTk.PhotoImage(Image.open('coins2.png'))
coins3 = ImageTk.PhotoImage(Image.open('coins3.png'))
coins4 = ImageTk.PhotoImage(Image.open('coins4.png'))
coins5 = ImageTk.PhotoImage(Image.open('coins5.png'))
coins6 = ImageTk.PhotoImage(Image.open('coins6.png'))

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


### FUNCTIONS ###

def coinshow():
    global money, bet

    if bet <= 20:
        coinlbl.configure(image=coins1)
    elif bet >= 21 and bet <= 100:
        coinlbl.configure(image=coins2)
    elif bet >= 101 and bet <= 500:
        coinlbl.configure(image=coins3)
    elif bet >= 501 and bet <= 1000:
        coinlbl.configure(image=coins4)
    elif bet >= 1001 and bet <= 1500:
        coinlbl.configure(image=coins5)
    elif bet >= 1501 :
        coinlbl.configure(image=coins6)

def add():
    global bet, money

    if bet <= money - 1:
        bet += 1
        betsh = str(bet) + '$'
        betlbl1.configure(text=betsh)
        bid_amount.configure(text=betsh)
        coinshow()
def low():
    global bet, money

    if bet - 1 >= 0:
        bet -= 1
        betsh = str(bet) + '$'
        betlbl1.configure(text=betsh)
        bid_amount.configure(text=betsh)
        coinshow()

def bid_cm():
    global money, bet, bet_take

    if bet <= money:
        bet_take = bet
        money -= bet
        moneysh = str(money) + '$'
        moneylbl1.configure(text=moneysh)
        bid_amount.configure(text=bet)
        coinshow()


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

upbtn = tk.Button(root,bg='#d5d5d5',image=up,border='0',command=add)
upbtn.place(x=50,y=680)

downbtn = tk.Button(root,bg='#d5d5d5',image=down,border='0',command=low)
downbtn.place(x=50,y=810)

bidbtn = tk.Button(root,bg='#d5d5d5',image=img4,border='0',command=bid_cm)
bidbtn.place(x=550,y=820)

betlbl = tk.Label(root,bg='#d5d5d5',image=img1)
betlbl.place(x=15,y=760)
betlbl1 = tk.Label(root,bg='#515151',text=betsh,font=('Arial Bold', 18),fg='white')
betlbl1.place(x=25,y=770)



### card decks 

## deck for player
set1lbl = tk.Label(root,bg='#139415',image=kw1)
set1lbl.place(x=250,y=580)

set2lbl = tk.Label(root,bg='#139415',image=kw1)
set2lbl.place(x=310,y=580)

set3lbl = tk.Label(root,bg='#139415',image=kw1)
set3lbl.place(x=370,y=580)

set4lbl = tk.Label(root,bg='#139415',image=kw1)
set4lbl.place(x=430,y=580)

set5lbl = tk.Label(root,bg='#139415',image=kw1)
set5lbl.place(x=490,y=580)

set6lbl = tk.Label(root,bg='#139415',image=kw1)
set6lbl.place(x=550,y=580)

set7lbl = tk.Label(root,bg='#139415',image=kw1)
set7lbl.place(x=610,y=580)

## deck for croupier

set1lbl1 = tk.Label(root,bg='#139415',image=kw1)
set1lbl1.place(x=250,y=280)

set2lbl2 = tk.Label(root,bg='#139415',image=kw1)
set2lbl2.place(x=310,y=280)

set3lbl3 = tk.Label(root,bg='#139415',image=kw1)
set3lbl3.place(x=370,y=280)

set4lbl4 = tk.Label(root,bg='#139415',image=kw1)
set4lbl4.place(x=430,y=280)

set5lbl5 = tk.Label(root,bg='#139415',image=kw1)
set5lbl5.place(x=490,y=280)

set6lbl6 = tk.Label(root,bg='#139415',image=kw1)
set6lbl6.place(x=550,y=280)

set7lbl7 = tk.Label(root,bg='#139415',image=kw1)
set7lbl7.place(x=610,y=280)

### coin display

coinlbl = tk.Label(root,image=coins,bg='#139415')
coinlbl.place(x=120,y=480)

bid_amount = tk.Label(root,bg='#139415',text='',font=('Arial Bold', 18),fg='white')
bid_amount.place(x=140,y=450)

root.mainloop()