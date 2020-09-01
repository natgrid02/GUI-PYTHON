import numpy as np

def maxMin(x, y):
    z = []
    for x1 in x:
        for y1 in y.T:
            z.append(max(np.minimum(x1, y1)))
    return np.array(z).reshape((x.shape[0], y.shape[1]))


def maxProduct(x, y):
    z = []
    for x1 in x:
        for y1 in y.T:
            z.append(max(np.multiply(x1, y1)))
    return np.array(z).reshape((x.shape[0], y.shape[1]))


r1 = np.array([[1, 0,5], [.3, .2,4], [0, .5,7]])
r2 = np.array([[.6, .6,2], [0, .6,5], [0, .1,3]])
r3 = np.array([[1, 0.2,2], [0, 1,2], [.7, 0,5]])

print (maxMin(r1, r2)) 
print (maxProduct(r1, r2))

print (maxMin(r1, r3))
print (maxProduct(r1, r3))

print (maxMin(r1, maxMin(r2, r3)))
print (maxProduct(r1, maxProduct(r2, r3))) 

p = np.array([[1.2,2.3,5.9,5.4], [4.4,5.7,4.6,4.1]])
q = np.array([[1.2,.1,6.1,6.5], [2.8,2.5,3.4,.1]])

'''tk.Label(master, text="5").grid(row=8, column=0)'''


