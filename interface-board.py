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

label_title = Label(window, text="Coleoptera s'occupe des fichiers inutiles pour vous", font=("Calibri", 17), bg='#B0DEFF', fg='white', bd=1, relief=SUNKEN)
label_title.grid(row=0,column=0)

# Bouton A - menu

bouton_a_menu = Button (text = "zone de texte", font=("Calibri", 12), bg='#B0DEFF', fg='white', bd=1, relief=SUNKEN)
bouton_a_menu.pack()

# afficher la entre
window.mainloop()