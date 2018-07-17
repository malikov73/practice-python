"""
expirements with recurion in a python
"""
import sys
from tkinter import Button, mainloop


def sumtree(L):
    tmp = 0
    for x in L:
        if not isinstance(x, list):
            print("q")
            tmp += x
        else:
            print("w")
            tmp += sumtree(x)
    print("e")
    return tmp


#print(sumtree([1, 1, 1, [1, 1, [1, [1, 1], 1], 1], 1]))

x = Button(
    text="Press me",
    command=(lambda: sys.stdout.write("Spam\n")))
x.pack()
mainloop()
