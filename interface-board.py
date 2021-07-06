from tkinter import *

import webbrowser


def open_github():
    webbrowser.open_new("https://github.com/jeroval/POIN-2021-filestools/tree/main")


# Creation de premiere fenetre laisser au début
window = Tk()


# personalisation de la fenetre
window.title ("Coleoptera")
window.geometry("1280x720")
window.minsize (480,360)
window.iconbitmap("logo-coleoptera.ico")
window.config(background='#0B008D')

# ajout du texte
label_title = Label(window, text="Coleoptera s'occupe des fichiers inutiles pour vous !", font=("Calibri", 10), bg='purple', fg='white', bd=1, relief=SUNKEN)
label_title.pack(side=BOTTOM)

# Bouton A - Parametres
bouton_a_git = Button (text = "Paramètres", font=("Calibri", 20), bg='#0C5A00', fg='white', bd=1, relief=SUNKEN)
bouton_a_git.pack(side=LEFT)
# Bouton B - Logs
bouton_a_git = Button (text = "Logs", font=("Calibri", 20), bg='#0C5A00', fg='white', bd=1, relief=SUNKEN)
bouton_a_git.pack(side=LEFT)
# Bouton C - Actions
bouton_a_git = Button (text = "Actions", font=("Calibri", 20), bg='#0C5A00', fg='white', bd=1, relief=SUNKEN)
bouton_a_git.pack(side=LEFT)
# Bouton E - Git
bouton_a_git = Button (text = "A propos", font=("Calibri", 20), bg='#0C5A00', fg='white', bd=1, relief=SUNKEN, command=open_github)
bouton_a_git.pack(side=LEFT)


# afficher la page laisser à la fin
window.mainloop()





