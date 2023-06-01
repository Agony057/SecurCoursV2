import tkinter as tk
import tkinter.messagebox as mbox
from tkinter import font
from ListClasse import ListClasse
from PIL import ImageTk, Image
from bdd import *


window = tk.Tk()

# Chargement de l'image PNG
image = Image.open("ressources/casier.jpg")

# Création d'un objet PhotoImage à partir de l'image
photo = ImageTk.PhotoImage(image)

# Création d'un widget Canvas de la même taille que l'image
canvas = tk.Canvas(window, width=image.width, height=image.height)

# Affichage de l'image sur le canvas en tant que fond
canvas.create_image(0, 0, image=photo, anchor=tk.NW)

# Placement du canvas dans la fenêtre
# canvas.grid(row=0, column=0, rowspan=12, columnspan=4)

# Creation d'une police plus grande
grandePolice = font.Font(size=30)
# Configuration de la nouvelle police pour tous les widgets de la fenêtre
window.option_add("*Font", grandePolice)

# UID
label_NoCarte = tk.Label(window, text="UID :")
label_NoCarte.grid(row=0, column=0)
# label_NoCarte.pack()

entry_Uid = tk.Entry(window, state="readonly")
entry_Uid.bind("<Return>", verification_Entrer)
entry_Uid.grid(row=0, column=1)

button_Uid = tk.Button(window, text="Scan", command=lecture_uid, background="lightblue", cursor="hand2")
button_Uid.grid(row=0, column=2)

label_Uid_Error = tk.Label(window, foreground="red")

# Nom
label_Nom = tk.Label(window, text="Nom :")
label_Nom.grid(row=2, column=0)

entryNom = tk.Entry(window)
entryNom.bind("<Return>", verification_Entrer)
entryNom.grid(row=2, column=1)

label_Nom_Error = tk.Label(window, foreground="red")

# Prenom
label_Prenom = tk.Label(window, text="Prenom :")
label_Prenom.grid(row=4, column=0)

entryPrenom = tk.Entry(window)
entryPrenom.bind("<Return>", verification_Entrer)
entryPrenom.grid(row=4, column=1)

label_Prenom_Error = tk.Label(window, foreground="red")

# Classe
label_Classe = tk.Label(window, text="Classe :")
label_Classe.grid(row=6, column=0)

entryClasse = tk.Entry(window)
entryClasse.bind("<Return>", verification_Entrer)
entryClasse.grid(row=6, column=1)

label_Classe_Error = tk.Label(window, foreground="red")

# Casier
label_NoCasier = tk.Label(window, text="N° Casier :")
label_NoCasier.grid(row=8, column=0)

entryNoCasier = tk.Entry(window)
entryNoCasier.bind("<Return>", verification_Entrer)
entryNoCasier.grid(row=8, column=1)

label_Casier_Error = tk.Label(window, foreground="red")

# Valider
button_Valider = tk.Button(window, text="Valider", command=verification,
                           background="lightgreen", cursor="hand2", width=7)
button_Valider.grid(row=10, columnspan=3)

# Retour
button_Retour = tk.Button(window, text="Annuler", command=retour,
                          background="orange", cursor="hand2", width=7)
button_Retour.grid(row=11, columnspan=3)

window.mainloop()
