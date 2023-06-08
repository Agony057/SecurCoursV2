from tkinter import *
from tkinter import ttk

fenetre = Tk()  # Génération de la fenêtre
fenetre.resizable(width=TRUE, height=TRUE)

div = Frame(fenetre, bg="blue")
div.pack()
div2 = Frame(fenetre)
div2.pack()

sous_div1 = Frame(div2,  height=200, bg="red")
sous_div1.grid(row=0, column=0, sticky="nsew")  # Utilisation de grid pour occuper toute la largeur disponible

sous_div2 = Frame(div2,  height=200, bg="yellow")
sous_div2.grid(row=0, column=1, sticky="nsew")  # Utilisation de grid pour occuper toute la largeur disponible

div2.columnconfigure(0, weight=1)  # Redimensionne la colonne 0
div2.columnconfigure(1, weight=1)  # Redimensionne la colonne 1

#------OptionMenu-----------------
variable = StringVar(div)
variable.set("2AMA Seconde Bac Pro TMA")  # Valeur par défaut

options = ("2AMA Seconde Bac Pro TMA", "1TMA Première Bac Pro TMA", "1MEN 1ère CAP MF", "TMEN Terminale CAP MF")
select_classes = OptionMenu(div, variable, *options)
select_classes.pack(side=LEFT)

#-----BLANK----------------------
blank_label = Label(div, width=5)  # Création d'un espace vide avec une largeur fixe
blank_label.pack(side=LEFT)
#------BtnGestion-----------------
button1 = Button(div, text="Elèves")
button1.pack(side=LEFT)

button2 = Button(div, text="Quitter")
button2.pack(side=LEFT)

#-------liste de gauche----------
my_tree = ttk.Treeview(fenetre)

#definition des colonnes
my_tree['colonnes'] = ("Id","élèves")

my_tree.column("Id",anchor=W, width=80)
my_tree.column("élèves",anchor=W, width=80)

fenetre.mainloop()