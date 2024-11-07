from tkinter import *
window=Tk()
lb1=Label(window, text="this is label widget",fg='red',font=("Helvetica",16))
lb2=Label(window, text="this is label widget",fg='red',font=("Helvetica",16))
lb1.place(x=60, y=50)
lb2.place(x=60, y=50)
window.title('hello python')
window.geometry("300x200+10+10")
window.mainloop()