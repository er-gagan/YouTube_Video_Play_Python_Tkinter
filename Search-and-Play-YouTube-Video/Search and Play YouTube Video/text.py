from tkinter import *
root=Tk()
def msg():
    print("Hello")
    b1["state"] = DISABLED
b1 = Button(root,text="Click",command=msg)
b1.pack()

root.mainloop()