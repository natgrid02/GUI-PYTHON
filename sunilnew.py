import numpy as np
from tkinter import *
import tkinter.messagebox
from  tkinter import messagebox
import re
from PIL import Image, ImageTk


def mini_max(A,B):
    e3.delete(0,'end')
    A = e1.get()
    A = A.split(',')
    B = e2.get()
    B = B.split(',')
    list = []
    for i in range(len(A)):
        D = min(float(A[i]),float(B[i]))
        list.append(D)
        d = max(list)
    e3.insert(END, (str(d),list))
    
def max_prod(A,B):
    e3.delete(0,'end')
    A = e1.get()
    A = A.split(',')
    B = e2.get()
    B = B.split(',')
    list = []
    for i in range(len(A)):
        D = round((float(A[i])*float(B[i])),3)
        list.append(D)
        d = max(list)
    e3.insert(END, (str(d),list))
    
def ponnen(A,B):
    e3.delete(0,'end')
    A = e1.get()
    A = A.split(',')
    B = e1.get()
    B = B.split(',')
    list = []
    for i in range(len(A)):
        D = round((float(A[i])*float(B[i])),3)
        list.append(D)
        d = (list)
    e3.insert(END, (str(d)))
    
    
def tollen(A,B):
    e3.delete(0,'end')
    A = e1.get()
    A = A.split(',')
    B = e1.get()
    B = B.split(',')
    list = []
    for i in range(len(A)):
        D = round((float(A[i])*float(B[i])*-1),3)
        list.append(D)
        d = (list)
    e3.insert(END, (str(d)))


def reset():
    e1.delete(0, 'end') 
    e2.delete(0, 'end')
    e3.delete(0, 'end')    


def iExit():
    iExit=tkinter.messagebox.askyesno("Fuzzy Implications & Inference","Confirm if you want to exit")
    if iExit>0:
     root.destroy()
     return    

root = Tk()
root.title("Fuzzy Implications & Inferences")
load = Image.open("x9.jpg")
background_image = ImageTk.PhotoImage(load,master=root)
background_label = Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)
e1 = Entry(root,font = 30,bd = 5)
e1.place(relx = 0.1, rely = 0.4, relwidth=0.35, relheight=0.07)
e1.insert(0,"         FUZZY SET 1")
e2 = Entry(root,font = 40,bd = 5,)
e2.place(relx = 0.5, rely = 0.4, relwidth=0.35, relheight=0.07)
e2.insert(0,"         FUZZY SET 2")
e3 = Entry(root,font = 40,bd = 5,)
e3.place(relx = 0.3, rely = 0.5, relwidth=0.3, relheight=0.07)
e3.insert(0,"          RESULT")   


title=Label(root,text = 'FUZZY IMPLICATION AND INFERENCE',bg='black',font=('arial',13,'bold'),fg='white')
title.place(x=100,y=10)
button_1 = Button(root,text=' MAXPRO',bg= 'lightgreen', fg= 'black', width='20', bd='3',activebackground= 'green',font = 20,padx = 20,pady = 10,command =lambda:max_prod(e1.get(),e2.get()))
button_2 = Button(root,text=' MAXMIN',bg= 'yellow', fg= 'black', width='20', bd='3',activebackground= 'yellow',font = 20,padx = 30,pady = 10,command =lambda:mini_max(e1.get(),e2.get()))
button_3 = Button(root,text=' TOLLENS',bg= 'orange', fg= 'black', width='60', bd='3',activebackground= 'orange',font = 20,padx = 60,pady = 5,command =lambda:ponnen(e1.get(),e2.get()))
button_4 = Button(root,text=' PONNENS',bg= 'silver', fg= 'black', width='60', bd='3',activebackground= 'silver',font = 20,padx = 60,pady = 5,command =lambda:tollen(e1.get(),e2.get()))
button_5 = Button(root,text='RESET',bg= 'black', fg= 'white', width='20', bd='0',activebackground= 'steelblue',font = 30,padx = 30,pady = 5,command =reset)
button_6 = Button(root,text='EXIT',bg= 'black', fg= 'white', width='20', bd='0',activebackground= 'steelblue',font = 30,padx = 30,pady = 5,command =iExit)
button_1.place(relx=0.2, rely = 0.7,relheight=0.05, relwidth=0.2)
button_2.place(relx=0.5, rely = 0.7,relheight=0.05, relwidth=0.2)
button_3.place(relx=0.2, rely = 0.8,relheight=0.05, relwidth=0.2)
button_4.place(relx=0.5, rely = 0.8,relheight=0.05, relwidth=0.2)
button_5.place(relx=0.8, rely = 0.95,relheight=0.05, relwidth=0.2)
button_6.place(relx=0.0, rely = 0.95,relheight=0.05, relwidth=0.2)
root.geometry("500x450+10+10")
root.mainloop()
