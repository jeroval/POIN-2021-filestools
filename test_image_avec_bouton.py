from tkinter import *


def analyse():
    global logs_samples
    can3.delete(ALL)
    can3.create_image(700, 398, image=logs_samples)


fen1 = Tk()


global logs_samples
can3 = Canvas(fen1, width=1280, height=720, bg='white')
can3.pack()
logs_samples = PhotoImage(file='sample_logs.PNG')
CLESOL = Button(fen1, text='afficher', command=analyse)
CLESOL.pack(expand=YES)


fen1.mainloop()