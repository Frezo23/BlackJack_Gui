import random
import tkinter as tk 
from tkinter import *
from PIL import ImageTk, Image


def get_cards(color,number,croupier_sum):

    color = random.randint(1,4)
    number = random.randint(1,13)

    