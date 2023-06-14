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


# Fonction de mise à jour des données de la liste de gauche lors du changement de classe sélectionnée
def on_class_select(*args):
    update_data()


def page_casier():
    div_vue_casier.pack(padx=20)
    div_vue_casier2.pack()
    select_classes.current(4)
    update_data()


def construction_page_casier():
    forget_all()
    page_casier()


def forget_all():
    forget_page_accueil()
    forget_page_eleve()
    forget_page_casier()


def forget_page_casier():
    div_vue_casier.pack_forget()
    div_vue_casier2.pack_forget()


def forget_page_eleve():
    div_vue_eleve.pack_forget()
    div_vue_eleve2.pack_forget()
    div_vue_eleve3.pack_forget()


def construction_page_eleve():
    forget_all()
    page_eleve()


def page_eleve():
    div_vue_eleve.pack(padx=20, pady=10)  # Ajout du padding à gauche et à droite de 20 pixels
    div_vue_eleve2.pack(pady=25)
    div_vue_eleve3.pack(pady=10)


def forget_page_accueil():
    label_principal.pack_forget()
    testbouton.pack_forget()


def construction_accueil():
    forget_all()
    accueil()


def accueil():
    label_principal.pack(pady=20, padx=20)
    testbouton.pack()


def retour_accueil():
    # result_retour = mbox.askyesno("Confirmation", "Etes-vous sûr de vouloir quitter ?")
    # if result_retour:
    construction_accueil()


# Badge
#################################################################################################

label_principal = Label(fenetre, text="Veuillez passez votre badge")
label_principal.pack(pady=20, padx=20)
# label_principal.pack()
# fenetre.geometry("800*600")
# label_principale.place(relx=0.5, rely=0.5, anchor=CENTER)
testbouton = Button(fenetre, text="testbouton", command=construction_page_casier)
testbouton.pack()

#################################################################################################


# Casier
#################################################################################################

div_vue_casier = Frame(fenetre)
div_vue_casier.pack(padx=20)  # Ajout du padding à gauche et à droite de 20 pixels
div_vue_casier2 = Frame(fenetre)
div_vue_casier2.pack()

sous_div_vue_casier1 = Frame(div_vue_casier2, height=200)
sous_div_vue_casier1.grid(row=0, column=0, sticky="nsew")

sous_div_vue_casier2 = Frame(div_vue_casier2)
sous_div_vue_casier2.grid(row=0, column=1, sticky="nsew")

# Crée les nouveaux Radiobuttons
choix_radio_casier = StringVar()
radio_casier1 = Radiobutton(sous_div_vue_casier2, text="a oublié son badge", variable=choix_radio_casier, value="a_oublie_son_badge")
radio_casier2 = Radiobutton(sous_div_vue_casier2, text="ouvrir casier clé", variable=choix_radio_casier, value="ouvrir_casier_cle")
radio_casier3 = Radiobutton(sous_div_vue_casier2, text="ouvrir casier téléphone", variable=choix_radio_casier, value="ouvrir_casier_telephone")

choix_radio_casier.set('a_oublie_son_badge')

radio_casier1.pack(anchor=W)
radio_casier2.pack(anchor=W)
radio_casier3.pack(anchor=W)

# DropDownMenu
nom_classe = StringVar(div_vue_casier)

options = liste_classe_eleve()

select_classes = ttk.Combobox(div_vue_casier, textvariable=nom_classe, values=options)
select_classes.pack(side=LEFT)
select_classes.bind("<<ComboboxSelected>>", on_class_select)

# BLANK
blank_label = Label(div_vue_casier, width=50)
blank_label.pack(side=LEFT)

# BtnEleve
button_vers_page_eleve = Button(div_vue_casier, text="Elèves", command=construction_page_eleve())
button_vers_page_eleve.pack(side=LEFT)

# BLANK
blank_label = Label(div_vue_casier, width=10)
blank_label.pack(side=LEFT)

# BtnAccueil
button_vers_accueil_depuis = Button(div_vue_casier, text="Accueil", command=retour_accueil)
button_vers_accueil_depuis.pack(side=LEFT)

# Liste de gauche
my_tree = ttk.Treeview(sous_div_vue_casier1)
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

div_vue_eleve = Frame(fenetre)
div_vue_eleve.pack(padx=20, pady=10)  # Ajout du padding à gauche et à droite de 20 pixels
div_vue_eleve2 = Frame(fenetre)
div_vue_eleve2.pack(pady=25)
div_vue_eleve3 = Frame(fenetre)
div_vue_eleve3.pack(pady=10)

sous_div_vue_eleve1 = Frame(div_vue_eleve2, height=200)
sous_div_vue_eleve1.grid(row=0, column=0, sticky="nsew")

sous_div_vue_eleve2 = Frame(div_vue_eleve2)
sous_div_vue_eleve2.grid(row=0, column=1, sticky="nsew", pady=25)

# DropDownMenu
variable = StringVar(div_vue_eleve)

options = liste_classe_eleve()

select_classes = ttk.Combobox(div_vue_eleve, textvariable=variable, values=options, width=30)
select_classes.pack(side=LEFT)
select_classes.bind("<<ComboboxSelected>>", on_class_select)

# BLANK
blank_label = Label(div_vue_eleve, width=50)
blank_label.pack(side=LEFT)

# BtnEleve
button1 = Button(div_vue_eleve, text="Elèves")
button1.pack(side=LEFT)

# BLANK
blank_label = Label(div_vue_eleve, width=10)
blank_label.pack(side=LEFT)

# BtnQuitter
button2 = Button(div_vue_eleve, text="Quitter")
button2.pack(side=LEFT)
#GRID

# BtnAjouter
btnAdd = Button(div_vue_eleve3, text="Valider")
btnAdd.grid(row=0, column=0)

# ScanBadge
btnScan = Button(div_vue_eleve3, text="Scan Badge")
btnScan.grid(row=0, column=1)

#entry + lbl nom
lblNom = Label(div_vue_eleve3, text="Nom:")
lblNom.grid(row=0, column=3)

entryNom = Entry(div_vue_eleve3)
entryNom.grid(row=0, column=4)

#entry + lbl prenom
lblPrenom = Label(div_vue_eleve3, text="Prenom:")
lblPrenom.grid(row=0, column=5)

entryPrenom = Entry(div_vue_eleve3)
entryPrenom.grid(row=0, column=6)

#entry + lbl NCasier
lblNCasier = Label(div_vue_eleve3, text="N° Casier:")
lblNCasier.grid(row=0, column=7)

entryNCasier = Entry(div_vue_eleve3)
entryNCasier.grid(row=0, column=8)

# DropDownMenu
variable_new_eleve_class = StringVar(div_vue_eleve3)
variable_new_eleve_class.set("Sélectionner une classe")  # Valeur par défaut

options_new_eleve_class = liste_classe_eleve()
new_eleve_class = ttk.Combobox(div_vue_eleve3, textvariable=variable_new_eleve_class, values=options_new_eleve_class, width=20)
new_eleve_class.grid(row=0, column=9)

# BtnAnnuler
btnAnnuler = Button(div_vue_eleve3, text="Annuler")
btnAnnuler.grid(row=1, column=0)

#entry + lbl IUD
lblUID = Label(div_vue_eleve3, text="UID:")
lblUID.grid(row=1, column=1)

entryUID = Entry(div_vue_eleve3)
entryUID.grid(row=1, column=2)


# Liste de gauche
my_tree = ttk.Treeview(sous_div_vue_eleve1)
my_tree['columns'] = ("Id", "nom", "prenom")
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Id", anchor=W, width=80)
my_tree.column("nom", anchor=W, width=150)
my_tree.column("prenom", anchor=W, width=150)
my_tree.heading("Id", text="Id")
my_tree.heading("nom", text="Nom")
my_tree.heading("prenom", text="Prenom")

my_tree.pack(side=LEFT)

#################################################################################################


# Construction page d'accueil
#################################################################################################

forget_all()
construction_accueil()

#################################################################################################


fenetre.mainloop()
