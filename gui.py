'''Create a GUI to explain the various concepts covered in Fuzzy implications and fuzzy inference
import tkinter 
Top = tkinter.Tk()
Top.mainloop()'''

import numpy as np

                              #zadeh rule

def maxmin(p, q):
    z = []
    for p1 in p:                                                               #element in tuple
        for q1 in q:                                                           #element in tuple
            z.append(max(np.minimum(p1,q1)))                                   #append to z
    return np.array(z).reshape((p.shape[0], q.shape[0]))                       #arranging the matrix
    print (maxmin(p,q))

def minmax(p,q):
    z = []
    for p1 in p:                                                               #element in tuple
        for q1 in q:                                                           #element in tuple
            z.append(max(np.divide(p1,q1)))                                    #append to z
    return np.array(z).reshape((p.shape[0], q.shape[0]))                       #arranging the matrix 


p = np.array([[1.2,2.3,5.9,5.4], [4.4,5.7,4.6,4.1]])
q = np.array([[1.2,.1,6.1,6.5],   [2.8,2.5,3.4,.1]])

y=maxmin(p,q)

print (z) 
print (minmax(p,q))


