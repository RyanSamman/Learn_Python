from tkinter import *
import sys

root = Tk()
root.title("Number Processor")
root.geometry("300x460")

x = "Insert a number"
guiFrame1 = Frame(root)
guiFrame2 = Frame(root)
guiFrame1.grid(row=1, sticky=W)
guiFrame2.grid(row=2, sticky=W)


def updater(var1):
    global x
    x = var1.get()
    output.delete(1.0, END)
    output.insert(END, x)
    print(x)


def refresher(output):
    output.delete(1.0, END)


Label(guiFrame1, text="Enter a number: ", width=20).grid(row=1, column=1, sticky=W)
input_box = Entry(guiFrame1, textvariable=x, width=20)
input_box.grid(row=1, column=2)
Button(guiFrame1, text="Run", command=lambda: updater(input_box), width=20).grid(row=2, column=2)
Button(guiFrame1, text="QUIT", fg="red", command=root.destroy, width=20).grid(row=2, column=1)
output = Text(guiFrame2, width=40, background="light gray")
output.grid(row=3, column=1)
Button(root, text="Restart", command=lambda: refresher(output), width=42).grid(row=3, sticky=W)



root.mainloop()