from tkinter import *

import webbrowser


def open_github():
    webbrowser.open_new("https://github.com/jeroval/POIN-2021-filestools/tree/main")


# Creation de premiere fenetre laisser au début
root = Tk()


# personalisation de la fenetre
root.title ("Coleoptera")
root.geometry("1280x720")
root.minsize (480,360)
root.iconbitmap("logo-coleoptera.ico")
root.config(background='#292929')

# ajout du texte
label_title = Label(root, text="Coleoptera s'occupe des fichiers inutiles pour vous ! Version Alpha test", font=("Calibri", 10), bg='purple', fg='white', bd=1, relief=SUNKEN)
label_title.pack(side=BOTTOM)

# Bouton A - Parametres
bouton_a_git = Button (text = "Paramètres", font=("Calibri", 20), bg='#0C5A00', fg='white', bd=1, relief=SUNKEN)
bouton_a_git.pack(side=LEFT)
# Bouton B - Logs
bouton_a_git = Button (text = "Logs", font=("Calibri", 20), bg='#0C5A00', fg='white', bd=1, relief=SUNKEN)
bouton_a_git.pack(side=LEFT)
# Bouton C - Actions
bouton_a_git = Button (text = "Recommandations", font=("Calibri", 20), bg='#0C5A00', fg='white', bd=1, relief=SUNKEN)
bouton_a_git.pack(side=LEFT)
# Bouton D - Lancer le scan
bouton_a_git = Button (text = "Démarrer l'analyse", font=("Calibri", 20), bg='#0C5A00', fg='white', bd=1, relief=SUNKEN)
bouton_a_git.pack(side=RIGHT)
# Bouton E - Stopper le scan
bouton_a_git = Button (text = "Stoper l'analyse", font=("Calibri", 20), bg='#0C5A00', fg='white', bd=1, relief=SUNKEN)
bouton_a_git.pack(side=RIGHT)
# Bouton F - Git
bouton_a_git = Button (text = "A propos", font=("Calibri", 20), bg='#0C5A00', fg='white', bd=1, relief=SUNKEN, command=open_github)
bouton_a_git.pack(side=LEFT)


# afficher la page laisser à la fin
root.mainloop()





