from tkinter import *
from tkinter import ttk
#-------Fonction select sur la table----------
def on_tree_select(event):
    # Obtient l'identifiant de l'élément sélectionné
    selected_item = my_tree.focus()


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
my_tree = ttk.Treeview(sous_div1)

#definition des colonnes
my_tree['column'] = ("Id","élèves")

my_tree.column("#0", width=0,stretch=NO)
my_tree.column("Id",anchor=W, width=80)
my_tree.column("élèves",anchor=W, width=80)

my_tree.heading("Id", text="Id")
my_tree.heading("élèves", text="Elèves")

my_tree.insert(parent='',index='end',iid=0,values=(1,"tijou allan"))
my_tree.insert(parent='',index='end',iid=1,values=(2,"viardot tibo"))
my_tree.pack()

#-------liste de droite----------

#Checklist
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()

check1 = Checkbutton(sous_div2, text="a oublié son badge", variable=var1)


check2 = Checkbutton(sous_div2, text="ouvrir casier clé", variable=var2)


check3 = Checkbutton(sous_div2, text="ouvrir casier téléphone", variable=var3)


# Lie la fonction `on_tree_select` à l'événement de sélection d'un élément dans la table
# Remplacez `my_tree` par votre propre référence à votre widget de liste
my_tree.bind("<<TreeviewSelect>>", on_tree_select)

fenetre.mainloop()