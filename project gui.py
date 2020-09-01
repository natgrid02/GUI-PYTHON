import tkinter as tk 

master = tk.Tk() 

master.title("FUZZY IMPLICATIONS") 

master.geometry("500x250") 

                                                                               # label to enter name 
tk.Label(master, text="RECORD NUMBER").grid(row=0, column=0) 
                                                                               # label for reg number 
tk.Label(master, text="DATE").grid(row=0, column=3) 
                                                                               #ENTER INPUTS
e1 = tk.Entry(master) 
e2 = tk.Entry(master)
e3 = tk.Entry(master) 
e4 = tk.Entry(master) 
e5 = tk.Entry(master) 
                                                                               #input as  set
tk.Label(master, text="SET 1").grid(row=8, column=0) 
tk.Label(master, text="SET 2").grid(row=16, column=0)
tk.Label(master, text="OUTPUT SET").grid(row=24, column=3)
tk.Label(master, text="FINAL SET").grid(row=19, column=0)
 
                                                                               # inputs coloumn
tk.Label(master, text="fuzzy ip1").grid(row=7, column=3) 
tk.Label(master, text="fuzzy ip2").grid(row=15, column=3)
                                                                               # e grid 
e1.grid(row=0, column=1) 
e2.grid(row=0, column=5)
e3.grid(row=19, column=3) 
e4.grid(row=8, column=3) 
e5.grid(row=16, column=3) 
                                                                               # button
button1=tk.Button(master, text="execute", bg="red", command=display) 
button1.grid(row=18, column=3) 


master.mainloop() 


