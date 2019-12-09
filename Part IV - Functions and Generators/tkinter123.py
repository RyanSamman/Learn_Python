from tkinter import Button, mainloop  # Tkinter in 2.X

x = Button(
    text='Press me',
    command=(lambda: print('Omar is stupid')))  # 3.X: print()

x.pack()
mainloop()
