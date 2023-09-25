from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser
import os
import sys
from datetime import datetime
from datetime import date
root = tk.Tk()
root.geometry('1000x648+150+0')
root.title("Agence Touristique")
root.iconbitmap("b.ico")
root.resizable(False,False)
title = Label(root , text='Méga Travel', fg='#073657', bg='#99ddef' , font=('Arial',16,'bold') )
title.pack(fill=X)
def open_website():
    url = "https://www.facebook.com/hamzamegatravel"  # Remplacez par l'URL du site web que vous souhaitez ouvrir
    webbrowser.open(url)
    
F1 = Frame(root , width=300 , height=650 , bg='#99ddef')
F1.place(x=700, y=40 )
photo = PhotoImage(file='photo.png')
imo = Label(root,image=photo)
imo.place(width=690 , heigh=370 , x='5' , y='40'  )

photo1 = PhotoImage(file='a.png')
imo1 = Label(F1,image=photo1)
imo1.place(width=300 , heigh=180 , x='0' , y='0'  )
B1 = Button(F1,text='Compte Facebook' , width=26 , height=2, fg='white',bg='#1e56ae', font=('tajwal',11,'bold'), command=open_website)
B1.place(x=30,y=220)
B2 = Button(F1,text='Site web' , width=26 , height=2, fg='white',bg='#1e56ae', font=('tajwal',11,'bold'))
B2.place(x=30,y=290)
B3 = Button(F1,text='Compte Gmail' , width=26 , height=2, fg='white',bg='#1e56ae', font=('tajwal',11,'bold'))
B3.place(x=30,y=360)
B4 = Button(F1,text='Compte Telegrame' , width=26 , height=2, fg='white',bg='#1e56ae', font=('tajwal',11,'bold'))
B4.place(x=30,y=430)
B5 = Button(F1,text='Information sur logiciel' , width=26 , height=2, fg='white',bg='#1e56ae', font=('tajwal',11,'bold'))
B5.place(x=30,y=500)

F2 = Frame(root ,width=690 , height=228 , bg='#99ddef' )
F2.place( x=5 , y=415 )

def update_time():
    current_time = datetime.now().strftime('%H:%M:%S')
    time_label.config(text=current_time)
    F2.after(1000, update_time)
time_label = Label(F2, font=("Arial", 13))
time_label.place(x='15' , y='10')

update_time()

def update_date():
    current_date = date.today().strftime('%d/%m/%Y')
    date_label.config(text=current_date)
    F2.after(86400000, update_date) 

date_label = Label(F2, font=("Arial", 13))
date_label.place(x='590' , y='10')
update_date()

B6= Button(F2,text='Ouvrir Logiciel ' , width=50 , height=2, fg='white',bg='#1e56ae', font=('tajwal',11,'bold'))
B6.place(x=115,y=70)


root.mainloop()


