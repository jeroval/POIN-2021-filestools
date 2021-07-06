from tkinter import *

# Creation de premiere fenetre
window = Tk()

# personalisation de la fenetre
window.title ("Coleoptera")
window.geometry("1280x720")
window.minsize (480,360)
window.iconbitmap("logo-coleoptera.ico")
window.config(background='#B0DEFF')

# ajout du texte
label_title = Label(window, text="Coleoptera voit les fichiers inutles et vous averti", font=("Calibri", 20), bg='#B0DEFF', fg='white')
label_title.grid(row=0,column=0)


# afficher la fenetre
window.mainloop()