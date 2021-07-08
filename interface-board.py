from tkinter import *

import webbrowser


def open_github():
    webbrowser.open_new("https://github.com/jeroval/POIN-2021-filestools/tree/main")


def open_dons():
    webbrowser.open_new("https://streamelements.com/jerovaljerome/tip")

# Creation de premiere fenetre laisser au début
root = Tk()


# personalisation de la fenetre
root.title ("Coleoptera")
root.geometry("1280x720")
root.minsize (480,360)
root.iconbitmap("logo-coleoptera.ico")
root.config(background='#292929')

# ajout du texte titre
label_title = Label(root, text="Coleoptera s'occupe des fichiers inutiles pour vous ! Version Alpha test", font=("Calibri", 14), bg='black', fg='white', bd=1)
label_title.pack(side=TOP)

#Creation de la boite à boutons
frame = Frame(root, bg='black')

# Bouton A - Parametres
bouton_a_git = Button (frame, text = "Paramètres", font=("Calibri", 14), bg='#010B8B', fg='white', bd=1, relief=SUNKEN)
bouton_a_git.pack()
# Bouton B - Logs
bouton_b_git = Button (frame, text = "Logs", font=("Calibri", 14), bg='#010B8B', fg='white', bd=1, relief=SUNKEN)
bouton_b_git.pack()
# Bouton C - Actions
bouton_c_git = Button (frame, text = "Recommandations", font=("Calibri", 14), bg='#010B8B', fg='white', bd=1, relief=SUNKEN)
bouton_c_git.pack()
# Bouton D - Lancer le scan
bouton_d_git = Button (frame, text = "Démarrer l'analyse", font=("Calibri", 14), bg='#010B8B', fg='white', bd=1, relief=SUNKEN)
bouton_d_git.pack()
# Bouton E - Stopper le scan
bouton_e_git = Button (frame, text = "Stoper l'analyse", font=("Calibri", 14), bg='#010B8B', fg='white', bd=1, relief=SUNKEN)
bouton_e_git.pack()
# Bouton F - Git
bouton_f_git = Button (frame, text = "A propos", font=("Calibri", 14), bg='#010B8B', fg='white', bd=1, relief=SUNKEN, command=open_github)
bouton_f_git.pack()
# Bouton G - Dons
bouton_g_git = Button (frame, text = "Soutenez-nous ici", font=("Calibri", 14), bg='#010B8B', fg='white', bd=1, relief=SUNKEN, command=open_dons)
bouton_g_git.pack()

#Fermeture de la boite à boutons
frame.pack(side=LEFT)


# afficher la page laisser à la fin
root.mainloop()





