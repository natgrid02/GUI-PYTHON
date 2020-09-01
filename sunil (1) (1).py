from tkinter import *
from PIL import ImageTk,Image
import numpy as np
import matplotlib
import re

class MyWindow:
    
    def __init__(self, win):
        self.title=Label(win,text = 'FUZZY IMPLICATION AND INFERENCE',bg='honeydew',font=('arial',13,'bold'),fg='black')
        self.lbl1=Label(win, text='FUZZY SET 1------------------------------------->',fg = 'blue',font=('arial',8,'bold'))
        self.lbl2=Label(win, text='FUZZY SET 2------------------------------------->',fg = 'blue',font=('arial',8,'bold'))
        self.lbl3=Label(win, text='ZADEH RULE',fg = 'brown',font=('arial',8,'bold'))
        self.lbl4=Label(win, text='MODUS TOLLENS',fg = 'brown',font=('arial',8,'bold'))
        self.lbl5=Label(win, text='RECORD NUMBER',fg = 'black',font=('arial',8,'bold'))
        self.lbl6=Label(win, text='DATE',fg = 'black',font=('arial',8,'bold'))
        
        
        
        self.t1=Entry(bd=5)
        self.t2=Entry(bd=4)
        self.t3=Entry(bd=5)
        self.t4=Entry(bd=5)
        self.t5=Entry(bd=5)
        self.t6=Entry(bd=1)
        self.t7=Entry(bd=1)
        self.t8=Entry(bd=5)
        
##  button label
        self.btn1 = Button(win, text='maxMin execute')
        self.btn2 = Button(win, text='maxProduct execute')
        self.btn3 = Button(win, text='Modus  Tollen')
        self.btn4 = Button(win, text='Modus  Ponnens')
       
#        
# label space
      
        self.title.place(x=100, y=50)
        self.lbl1.place(x=80, y=200)
        self.t1.place(x=350, y=200)
        
        self.lbl2.place(x=80, y=250)
        self.t2.place(x=350, y=250)
        
        self.lbl5.place(x=0, y=0)
        self.t6.place(x=100, y=0)
        
        self.lbl6.place(x=320, y=0)
        self.t7.place(x=360, y=0)

#Button intialization 
        self.b1=Button(win, text='MAXMIN',bg= 'yellow', fg= 'black', width='12', bd='3', command=self.maxMin)
        self.b2=Button(win, text='MAXPRO',bg= 'green', fg= 'black', width='12', bd='3')
        self.b3=Button(win, text='MODUS TOLLENS',bg= 'orange', fg= 'black', width='12', bd='3')
        self.b4=Button(win, text='MODUS PONNENS',bg= 'silver', fg= 'black', width='12', bd='3')
        self.b2.bind('<Button-1>', self.minmax)
        self.b3.bind('<Button-1>', self.modus)
        self.b4.bind('<Button-1>', self.ponens)
      
##button place     
        self.b1.place(x=90, y=300)
        self.b2.place(x=190, y=300)
        self.b3.place(x=90, y=375)
        self.b4.place(x=190, y=375)
        
        self.lbl3.place(x=375, y=275)
        self.t3.place(x=350, y=300)
        
        
        self.lbl4.place(x=375, y=350)
        self.t4.place(x=350, y=375)
        
        
   
        
    def maxMin(self):
        self.t3.delete(0, 'end')
        # z = []
        #  for p1 in p:                                                               #element in tuple
        #     for q1 in q:                                                           #element in tuple
        #         c=z.append(max(np.minimum(p1,q1)))                                   #append to z
        # return np.array(z).reshape((p.shape[0], q.shape[0])) )  
    
       
        R = 2
        C = 2
        
        num1=(self.t1.get()) 
        a = list(map(int, num1.split())) 
        matrix1 = np.array(a).reshape(R, C)
        print(matrix1)
        
        num2=(self.t2.get()) 
        b = list(map(int, num2.split())) 
        matrix2 = np.array(b).reshape(R, C)
        print(matrix2)
        
        p = np.array(matrix1)
        print(p)
        q = np.array(matrix2)
        print(q)
      
        list1 = []
        for i in range(len(matrix1)):
            for i in range(len(matrix2)):
                D = max(int(a[i]),int(b[i]))
                list1.append(D)
                #np.array(D).reshape(R,C)
                print(D)
                d = max(list1)
                print(d)
        self.t3.insert(END, str(d))
        
        
    
    #function2
    def minmax(self,event):
        self.t3.delete(0, 'end')
        
        
        R = 2
        C = 2
        
        num1=(self.t1.get()) 
        a = list(map(int, num1.split())) 
        matrix1 = np.array(a).reshape(R, C)
        print(matrix1)
        
        num2=(self.t2.get()) 
        b = list(map(int, num2.split())) 
        matrix2 = np.array(b).reshape(R, C)
        print(matrix2)
        
        p = np.array(a)
        print(p)
        q = np.array(b)
        print(q)
        
        
        
        
        list1 = []
        for i in range(len(matrix1)):
            for i in range(len(matrix2)):
                D =  np.divide(int(a[i]),int(b[i]))
                list1.append(D)
                #np.array(D).reshape(R,C)
                print(D)
                d = max(list1)
        self.t3.insert(END, str(d))
        
        
        '''z = []
        for p1 in p:                                                               #element in tuple
            for q1 in q:                                                           #element in tuple
                z.append(max(np.minimum(p1,q1)))                                   #append to z
        return np.array(z).reshape((p.shape[0], q.shape[0]))
    y = minmax(self,event)
    self.t3.insert(END, str(y))'''
        
        '''R = 3
        C = 3
        num1=(self.t1.get())
         
        a = list(map(float, num1.split())) 
        matrix1 = np.array(a).reshape(R, C)
        
        num2=(self.t2.get())
         
        b = list(map(float, num2.split())) 
        matrix2 = np.array(a).reshape(R, C)
    
        p = np.array(matrix1)
        print(p)
        q = np.array(matrix2)
        print(q)
       
        r=p+q
        r=1-r
        self.t3.insert(END, str(r))'''
            
    #function3
    def modus(self,event):
        self.t4.delete(0, 'end')
        z = []
        # for p1 in p:                                                               #element in tuple
        #     for q1 in q:                                                           #element in tuple
        #         z.append(max(np.divide(p1,q1)))                                    #append to z
        # return np.array(z).reshape((p.shape[0], q.shape[0]))                       #arranging the matrix 
        
        R = 2
        C = 2
        
        num1=(self.t1.get()) 
        a = list(map(int, num1.split())) 
        matrix1 = np.array(a).reshape(R, C)
        print(matrix1)
        
        num2=(self.t2.get()) 
        b = list(map(int, num2.split())) 
        matrix2 = np.array(b).reshape(R, C)
        print(matrix2)
        
        p = np.array(a)
        print(p)
        q = np.array(b)
        print(q)
        z=[]
    
        result=p*q
        #l=result*-1
        self.t4.insert(END, str(result))
        
    def ponens(self,event):
        self.t4.delete(0, 'end')
        z = []
        # for p1 in p:                                                               #element in tuple
        #     for q1 in q:                                                           #element in tuple
        #         z.append(max(np.divide(p1,q1)))                                    #append to z
        # return np.array(z).reshape((p.shape[0], q.shape[0]))                       #arranging the matrix 
        
        R = 2
        C = 2
        num1=(self.t1.get())
         
        a = list(map(int, num1.split())) 
        matrix1 = np.array(a).reshape(R, C)
        
        num2=(self.t2.get())
         
        b = list(map(int, num2.split())) 
        matrix2 = np.array(b).reshape(R, C)
    
        p = np.array(matrix1)
        print(p)
        q = np.array(matrix2)
        print(q)
        z = []
    
        l=p*q
        result=l*-1
        self.t4.insert(END, str(result))
      
window=Tk()
window.title('Fuzzy Implications')
window.geometry("480x450+10+10")
load = Image.open("x4.jpg")
background_image = ImageTk.PhotoImage(load, master=window)
background_label = Label(window, image=background_image)
background_label.place(relwidth=1, relheight=1)
mywin=MyWindow(window)
window.mainloop()
      