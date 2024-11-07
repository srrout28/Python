from  tkinter import *
win=Tk()
win.title('indian flag')
lb1=Label(win,text='          ',bg='orange')
lb2=Label(win,text='          ',bg='white')
lb3=Label(win,text='          ',bg='green')
lb1.place(x=20,y=60)
lb2.place(x=20,y=80)
lb3.place(x=20,y=100)
win.geometry("300x300+260+100")
win.mainloop()

