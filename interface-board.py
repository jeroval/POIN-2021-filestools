from tkinter import *
from tkinter.filedialog import *
import webbrowser
import logging
import threading
import datetime
import queue
import logging
import signal
import time
import threading
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import ttk, VERTICAL, HORIZONTAL, N, S, E, W



#Les Fonctions==============================================================================
def open_github():
    webbrowser.open_new("https://github.com/jeroval/POIN-2021-filestools/tree/main")

def open_dons():
    webbrowser.open_new("https://streamelements.com/jerovaljerome/tip")


# Creation de premiere fenêtre laisser au début=============================================
root = Tk()


# Personalisation de la fenêtre ============================================================
root.title ("Coleoptera")
root.geometry("1280x720")
root.minsize (480,360)
root.iconbitmap("logo-coleoptera.ico")
root.config(background='#292929')


#Creation de la boite à logo frame A =======================================================
frame_a = Frame(root, bg='black')

# ajout du texte titre
label_title_a = Label(frame_a, text="Coleoptera s'occupe des fichiers inutiles pour vous ! ", font=("Calibri", 13), bg='black', fg='white', bd=1)
label_title_a.pack()
# Ajout du logo principal sur la fenetre image a
width = 100
height = 100
image_a = PhotoImage(file="coleoptera.png").zoom(1).subsample(1)
canvas = Canvas(frame_a, width=width, height=height, bg='#292929')
canvas.create_image(width/2, height/2, image=image_a)
canvas.pack()

frame_a.pack(side=TOP)
# Fermeture de la boite à logo frame A ========================================================


# Creation de la boite à boutons frame B ======================================================
frame_b = Frame(root, bg='black')

# Bouton B - Lancer le scan
bouton_b = Button (frame_b, text =" |> Démarrer l'analyse", font=("Calibri", 13), bg='#010B8B', fg='white', bd=1, relief=SUNKEN)
bouton_b.pack()
# Bouton D - Logs
bouton_d = Button (frame_b, text ="Accès aux logs", font=("Calibri", 13), bg='#010B8B', fg='white', bd=1, relief=SUNKEN)
bouton_d.pack()
# Bouton E - Actions
bouton_e = Button (frame_b, text ="Résultats d'analyse", font=("Calibri", 13), bg='#010B8B', fg='white', bd=1, relief=SUNKEN)
bouton_e.pack()
# Bouton F - Git
bouton_f = Button (frame_b, text ="(!) A propos du logiciel", font=("Calibri", 13), bg='#010B8B', fg='white', bd=1, relief=SUNKEN, command=open_github)
bouton_f.pack()
# Bouton G - Dons
bouton_g = Button (frame_b, text ="Soutenez-nous ici", font=("Calibri", 13), bg='#010B8B', fg='white', bd=1, relief=SUNKEN, command=open_dons)
bouton_g.pack()
# Bouton C - Quitter
bouton_c = Button (frame_b, text ="X Quitter", font=("Calibri", 13), bg='#010B8B', fg='white', bd=1, relief=SUNKEN, command=root.destroy)
bouton_c.pack()

frame_b.pack(side=LEFT)
# Fermeture de la boite à boutons frame B =========================================================


#Creation de la boite à réglages frame C ======================================================
frame_c = Frame(root, bg='black')

#Emplacement souhaité
folder = Label(frame_c, text="Définissez l'emplacement à analyser : Exemple C:/Users/Jeroval/Documents", font=("Calibri", 13))
input_a = Entry(frame_c)
folder.pack()
input_a.pack()
#Taille minimale
size = Label(frame_c, text="Taille minimale à prendre en compte en Mo : Exemple : 100", font=("Calibri", 13))
input_b = Entry(frame_c)
size.pack()
input_b.pack()
#Age du fichier
age = Label(frame_c, text="Fichier non ouvert depuis plus tant de jours : Exemple : 365", font=("Calibri", 13))
input_c = Entry(frame_c)
age.pack()
input_c.pack()

frame_c.pack(expand=YES)
# Fermeture de la boite à réglages C ===========================================================


# Note sur la version de l'application =========================================================
label_title_b = Label(root, text="Version Alpha test", font=("Calibri", 14), bg='#292929', fg='white', bd=1)
label_title_b.pack(side=BOTTOM)

# Afficher la page laisser à la fin ============================================================
root.mainloop()




