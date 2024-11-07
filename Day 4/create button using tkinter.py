from  tkinter import *
window=Tk()
window.configure(bg='red')
b1=Button(window,text="RED",bg='blue')
b1.pack()
window.title('hello python')
window.geometry("300x200+400+30")
window.mainloop()