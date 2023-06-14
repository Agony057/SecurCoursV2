from tkinter import *
from tkinter import ttk
import tkinter.messagebox as mbox
from bdd import *

fenetre = Tk()

# Fonction de mise à jour des données de la liste de gauche en fonction de la classe sélectionnée
def update_data():
    # recupération du nom de la classe
    classe = nom_classe.get().replace("{", "").replace("}", "")

    if classe == "Toutes_les_classes":
        eleves = liste_eleve_avec_casier()
    else:
        # recuperation de liste d'eleve de la classe du dropdown
        eleves = liste_eleve_avec_casier_par_classe(classe)

    # on efface la liste pré-existante
    my_tree.delete(*my_tree.get_children())

    # on insère les eleves un par un dans la liste
    for eleve in eleves:
        my_tree.insert(parent='', index='end',values=(eleve[0], eleve[1], eleve[2]))

# Fonction appelée lorsque vous sélectionnez un élément de la liste de gauche
def on_tree_select(event):
    selected_item = my_tree.focus()  # Récupère l'élément sélectionné
    values = my_tree.item(selected_item, 'values')  # Récupère les valeurs de l'élément sélectionné


# Fonction pour afficher les Radiobuttons avec les valeurs nom et prenom
def display_radiobuttons(nom, prenom):
    # Efface les anciens Radiobuttons
    for widget in sous_div2.winfo_children():
        widget.destroy()


# Fonction de mise à jour des données de la liste de gauche lors du changement de classe sélectionnée
def on_class_select(*args):
    update_data()


def page_casier():
    div.pack(padx=20)
    div2.pack()


def construction_page_casier():
    forget_all()
    page_casier()
    select_classes.current(4)
    update_data()


def forget_all():
    forget_page_accueil()
    forget_page_eleve()
    forget_page_casier()


def forget_page_casier():
    div.pack_forget()
    div2.pack_forget()

def forget_page_eleve():
    print("effacerpagecasier")



def forget_page_accueil():
    label.pack_forget()
    testbouton.pack_forget()


def construction_accueil():
    forget_all()
    accueil()


def accueil():
    label.pack(pady=20, padx=20)
    testbouton.pack()


def retour_accueil():
    # result_retour = mbox.askyesno("Confirmation", "Etes-vous sûr de vouloir quitter ?")
    # if result_retour:
    construction_accueil()


# Badge
#################################################################################################

label = Label(fenetre, text="Veuillez passez votre badge")
label.pack(pady=20, padx=20)
# label.pack()
# fenetre.geometry("800*600")
# label.place(relx=0.5, rely=0.5, anchor=CENTER)
testbouton = Button(fenetre, text="testbouton", command=construction_page_casier)
testbouton.pack()

#################################################################################################


# Casier
#################################################################################################

div = Frame(fenetre)
div.pack(padx=20)  # Ajout du padding à gauche et à droite de 20 pixels
div2 = Frame(fenetre)
div2.pack()

sous_div1 = Frame(div2, height=200)
sous_div1.grid(row=0, column=0, sticky="nsew")

sous_div2 = Frame(div2)
sous_div2.grid(row=0, column=1, sticky="nsew")

# Crée les nouveaux Radiobuttons
var = StringVar()
radio1 = Radiobutton(sous_div2, text="a oublié son badge", variable=var, value="a_oublie_son_badge")
radio2 = Radiobutton(sous_div2, text="ouvrir casier clé", variable=var, value="ouvrir_casier_cle")
radio3 = Radiobutton(sous_div2, text="ouvrir casier téléphone", variable=var, value="ouvrir_casier_telephone")

var.set(None)

radio1.pack(anchor=W)
radio2.pack(anchor=W)
radio3.pack(anchor=W)

# DropDownMenu
nom_classe = StringVar(div)
# nom_classe.set("")  # Valeur par défaut

options = liste_classe_eleve()

select_classes = ttk.Combobox(div, textvariable=nom_classe, values=options, state="readonly")
select_classes.pack(side=LEFT)
select_classes.bind("<<ComboboxSelected>>", on_class_select)

# BLANK
blank_label = Label(div, width=50)
blank_label.pack(side=LEFT)

# BtnEleve
button1 = Button(div, text="Elèves")
button1.pack(side=LEFT)

# BLANK
blank_label = Label(div, width=10)
blank_label.pack(side=LEFT)

# BtnAccueil
button2 = Button(div, text="Accueil", command=retour_accueil)
button2.pack(side=LEFT)

# Liste de gauche
my_tree = ttk.Treeview(sous_div1)
my_tree['columns'] = ("Id", "nom", "prenom")
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Id", anchor=W, width=80)
my_tree.column("nom", anchor=W, width=150)
my_tree.column("prenom", anchor=W, width=150)
my_tree.heading("Id", text="N° Casier")
my_tree.heading("nom", text="Nom")
my_tree.heading("prenom", text="Prenom")
my_tree.bind("<<TreeviewSelect>>", on_tree_select)  # Appelle la fonction lorsqu'un élément est sélectionné
my_tree.pack(side=LEFT)

#################################################################################################


# Eleve
#################################################################################################




#################################################################################################


# Construction page d'accueil
#################################################################################################

forget_all()
construction_accueil()

#################################################################################################


fenetre.mainloop()
