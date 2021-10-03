from tkinter import *
import webbrowser as wb
from PIL import ImageTk, Image
from pyautogui import click
from pyautogui import press
from keyboard import write
from time import sleep
import pyautogui
import os
import time
import tkinter
import subprocess
a=Tk()
a.minsize(800,700)
a.maxsize(800,700)
a.title("Whatsapp Automation")
a.iconbitmap("Whatsapp_image.ico")
#a["bg"]="white"
a1=Label(a,text="========================================================================================================").place(x=-1,y=0)
image1 = Image.open("whatsapp_image.jpg").resize((300,300))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=250, y=80)

image1 = Image.open("auto1.jpg").resize((285,480))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=0, y=100)

image1 = Image.open("auto1.jpg").resize((285,480))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=510, y=100)

image1 = Image.open("auto2.jpg").resize((800,300))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=0, y=550)


def send_msg():
    x1=var1.get()
    x2=var2.get()
    subprocess.call("C:\\Users\\acer\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(5)
    click(x=242, y=112)
    write(x1)
    sleep(2)
    click(x=228, y=178)
    sleep(2)
    click(x=563, y=692)
    sleep(2)
    write(x2)
    sleep(2)
    press('enter')
def voice():
    x1=var1.get()
    subprocess.call("C:\\Users\\acer\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(5)
    click(x=242, y=112)
    write(x1)
    sleep(2)
    click(x=228, y=178)
    sleep(1)
    click(x=1208, y=55)
def video():
    x1=var1.get()
    subprocess.call("C:\\Users\\acer\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(5)
    click(x=242, y=112)
    write(x1)
    sleep(2)
    click(x=228, y=178)
    sleep(1)
    click(x=1160, y=54)
def profile():
    subprocess.call("C:\\Users\\acer\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(2)
    click(x=34,y=57)
def view_status():
    subprocess.call("C:\\Users\\acer\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(2)
    click(x=273, y=56)
lab=Label(a,text="Whatsapp Automation",font=("Arial",35,"bold"),fg="white",bg="darkblue").place(x=150,y=20)
text=Label(a,text="User Name",font=("Arial",22,"bold")).place(x=320,y=380)
var1=StringVar()
input_1=Entry(a,font=("Arial",20),borderwidth = 7,textvariable=var1,bg="grey").place(x=240,y=420)
text=Label(a,text="Message",font=("Arial",22,"bold")).place(x=330,y=475)
var2=StringVar()
input_2=Entry(a,font=("Arial",20),borderwidth = 7,textvariable=var2,bg="grey").place(x=240,y=520)
btn1=Button(a,text="Send Message",bd=10,bg="yellow",font=("Arial",10,"bold"),command=send_msg).place(x=200,y=585)
btn2=Button(a,text="Video Call",bd=10,bg="yellow",font=("Arial",10,"bold"),command=video).place(x=370,y=585)
btn3=Button(a,text="Voice Call",bd=10,bg="yellow",font=("Arial",10,"bold"),command=voice).place(x=510,y=585)
btn4=Button(a,text="View Profile",bd=15,bg="lime",font=("Arial",10,"bold"),command=profile).place(x=10,y=25)
btn5=Button(a,text="View Status",bd=15,bg="lime",font=("Arial",10,"bold"),command=view_status).place(x=670,y=25)
a1=Label(a,text="========================================================================================================").place(x=0,y=640)
a.mainloop()

