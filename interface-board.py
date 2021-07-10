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

#Creation de la boite à logo
framea = Frame(root, bg='black')

# ajout du texte titre
label_title_a = Label(framea, text="Coleoptera s'occupe des fichiers inutiles pour vous ! ", font=("Calibri", 14), bg='black', fg='white', bd=1)
label_title_a.pack()

# Ajout du logo principal sur la fenetre image a
width = 100
height = 100
image_a = PhotoImage(file="coleoptera.png").zoom(1).subsample(1)
canvas = Canvas(framea, width=width, height=height, bg='#292929')
canvas.create_image(width/2, height/2, image=image_a)
canvas.pack()

#Fermeture de la boite à logo
framea.pack(side=TOP)

#Creation de la boite à boutons
frameb = Frame(root, bg='black')

# Bouton A - Parametres
bouton_a = Button (frameb, text ="Vos réglages ici", font=("Calibri", 14), bg='#010B8B', fg='white', bd=1, relief=SUNKEN)
bouton_a.pack()
# Bouton B - Logs
bouton_b = Button (frameb, text ="Suivi des actions", font=("Calibri", 14), bg='#010B8B', fg='white', bd=1, relief=SUNKEN)
bouton_b.pack()
# Bouton C - Actions
bouton_c = Button (frameb, text ="Recommandations", font=("Calibri", 14), bg='#010B8B', fg='white', bd=1, relief=SUNKEN)
bouton_c.pack()
# Bouton D - Lancer le scan
bouton_d = Button (frameb, text ="Démarrer l'analyse", font=("Calibri", 14), bg='#010B8B', fg='white', bd=1, relief=SUNKEN)
bouton_d.pack()
# Bouton E - Stopper le scan
bouton_e = Button (frameb, text ="Stoper l'analyse", font=("Calibri", 14), bg='#010B8B', fg='white', bd=1, relief=SUNKEN)
bouton_e.pack()
# Bouton F - Git
bouton_f = Button (frameb, text ="A propos du logiciel", font=("Calibri", 14), bg='#010B8B', fg='white', bd=1, relief=SUNKEN, command=open_github)
bouton_f.pack()
# Bouton G - Dons
bouton_g = Button (frameb, text ="Soutenez-nous ici", font=("Calibri", 14), bg='#010B8B', fg='white', bd=1, relief=SUNKEN, command=open_dons)
bouton_g.pack()

#Fermeture de la boite à boutons
frameb.pack(side=LEFT)

label_title_b = Label(root, text="Version Alpha test", font=("Calibri", 14), bg='#292929', fg='white', bd=1)
label_title_b.pack(side=BOTTOM)

# afficher la page laisser à la fin
root.mainloop()





