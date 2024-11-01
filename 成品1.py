from tkinter import *

def btn_hit():
    if x.get() == "":
        x.set("I like tkinter")
    else:
        x.set("")

root = Tk()
root.title("Tkinter Demo")

x = StringVar()
label = Label(root, textvariable=x, fg="blue", bg="lightyellow",
              font="Verdana 16 bold",
              width=25, height=2)
label.pack()

btn = Button(root, text="Click me", command=btn_hit)
btn.pack()

root.mainloop()
