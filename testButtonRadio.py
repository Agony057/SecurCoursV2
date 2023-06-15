from tkinter import *
from tkinter import ttk
import tkinter.messagebox as mbox
from bdd import *


# fonction eleves
#####################################################################################################################################################################

# Fonction de mise à jour des données de la liste de gauche en fonction de la classe sélectionnée
def update_data_vue_eleve():
    # recupération du nom de la classe
    classe = valeur_defaut_combobox_eleve.get()

    if classe == "Toutes_les_classes":
        eleves = liste_eleve_avec_casier()
    else:
        # recuperation de liste d'eleve de la classe du dropdown
        eleves = liste_eleve_avec_casier_par_classe(classe)

    # on efface la liste pré-existante
    my_tree_eleve.delete(*my_tree_eleve.get_children())

    # on insère les eleves un par un dans la liste
    for eleve in eleves:
        my_tree_eleve.insert(parent='', index='end', values=(eleve[0], eleve[1], eleve[2]))

# Fonction appelée lorsque vous sélectionnez un élément de la liste de gauche
def on_tree_eleve_select(event):
    selected_item = my_tree_eleve.focus()  # Récupère l'élément sélectionné
    values = my_tree_eleve.item(selected_item, 'values')  # Récupère les valeurs de l'élément sélectionné


# Fonction de mise à jour des données de la liste de gauche lors du changement de classe sélectionnée
def on_class_eleve_select(*args):
    update_data_vue_eleve()

########################################################################################################################################################


# fonction casier
########################################################################################################################################################



########################################################################################################################################################


# fonction clear formulaire
########################################################################################################################################################

def clear_formulaire_eleve():
    entry_uid_new_eleve.selection_clear()
    entryNomAjoutEleve.select_clear()
    entryPrenomAjoutEleve.selection_clear()
    entryNoCasierAjoutEleve.selection_clear()
    new_eleve_class.set("Selection de la classe")


########################################################################################################################################################

# fonction forget
########################################################################################################################################################

def forget_all():
    forget_page_accueil()
    forget_page_eleve()
    forget_page_casier()


def forget_page_casier():
    # div_vue_casier.pack_forget()
    # div_vue_casier2.pack_forget()
    print("effacer vue casier")


def forget_page_eleve():
    div_vue_eleve.pack_forget()
    div_vue_eleve2.pack_forget()
    div_vue_eleve3.pack_forget()


def forget_page_accueil():
    label_principal.pack_forget()
    testbouton.pack_forget()

########################################################################################################################################################


# fonction construction de page
########################################################################################################################################################

def construction_page_casier():
    forget_all()
    page_casier()


def construction_page_eleve():
    forget_all()
    page_eleve()


def construction_accueil():
    forget_all()
    accueil()


def page_casier():
    div_vue_eleve.pack(padx=20)
    div_vue_eleve2.pack()
    select_eleve_classes.current(4)
    # update_data_vue_casier()


def page_eleve():
    div_vue_eleve.pack(padx=20, pady=10)  # Ajout du padding à gauche et à droite de 20 pixels
    div_vue_eleve2.pack(pady=25)
    div_vue_eleve3.pack(padx=10, pady=10)
    select_eleve_classes.current(4)
    new_eleve_class.set("Selection de la classe")
    update_data_vue_eleve()


def accueil():
    label_principal.pack(pady=20, padx=20)
    testbouton.pack()

########################################################################################################################################################


# fonction retour
########################################################################################################################################################

def retour_accueil():
    result_retour = mbox.askyesno("Confirmation", "Etes-vous sûr de vouloir quitter le mode ADMIN ?")
    if result_retour:
        construction_accueil()

########################################################################################################################################################


fenetre = Tk()

# Badge Accueil
#########################################################################################################################################################

label_principal = Label(fenetre, text="Veuillez passez votre badge")
label_principal.pack(pady=20, padx=20)
testbouton = Button(fenetre, text="simulation carte admin", command=construction_page_eleve)
testbouton.pack()

#################################################################################################################################################################


# Casier
#######################################################################################################################################################



####################################################################################################################################################################


# Eleve
################################################################################################################################################################

div_vue_eleve = Frame(fenetre)
div_vue_eleve.pack(padx=20, pady=10)  # Ajout du padding à gauche et à droite de 20 pixels
div_vue_eleve2 = Frame(fenetre)
div_vue_eleve2.pack(pady=25)
div_vue_eleve3 = Frame(fenetre)
div_vue_eleve3.pack(padx=10, pady=10)

sous_div_vue_eleve1 = Frame(div_vue_eleve2, height=200)
sous_div_vue_eleve1.grid(row=0, column=0, sticky="nsew")
sous_div_vue_eleve2 = Frame(div_vue_eleve2)
sous_div_vue_eleve2.grid(row=0, column=1, sticky="nsew", pady=25)

# DropDownMenu
valeur_defaut_combobox_eleve = StringVar(div_vue_eleve)
liste_valeur_combobox_eleve = liste_classe_eleve()
select_eleve_classes = ttk.Combobox(div_vue_eleve, textvariable=valeur_defaut_combobox_eleve, values=liste_valeur_combobox_eleve, width=30, state="readonly")
select_eleve_classes.pack(side=LEFT)
select_eleve_classes.bind("<<ComboboxSelected>>", on_class_eleve_select)

# BLANK
blank_label_eleve = Label(div_vue_eleve, text="MODE ADMIN", width=50)
blank_label_eleve.pack(side=LEFT)

# BtnEleve
btn_vers_casier = Button(div_vue_eleve, text="Gestion casier", width=11, background="lightgrey")
btn_vers_casier.pack(side=LEFT)

# BLANK
blank_label_eleve = Label(div_vue_eleve, width=10)
blank_label_eleve.pack(side=LEFT)

# BtnQuitter
btn_accueil_eleve = Button(div_vue_eleve, text="Accueil", command=retour_accueil, width=11, background="lightgrey")
btn_accueil_eleve.pack(side=LEFT)

# Liste de gauche
my_tree_eleve = ttk.Treeview(sous_div_vue_eleve1)
my_tree_eleve['columns'] = ("NoCasier", "nom", "prenom")
my_tree_eleve.column("#0", width=0, stretch=NO)
my_tree_eleve.column("NoCasier", anchor=W, width=80)
my_tree_eleve.column("nom", anchor=W, width=150)
my_tree_eleve.column("prenom", anchor=W, width=150)
my_tree_eleve.heading("NoCasier", text="N° casier")
my_tree_eleve.heading("nom", text="Nom")
my_tree_eleve.heading("prenom", text="Prenom")
my_tree_eleve.pack(side=LEFT)

# ScanBadge
btnScanUidEleve = Button(div_vue_eleve3, text="Scanner Badge", width=12, background="lightgrey")
btnScanUidEleve.grid(row=0, column=0)

#entry + lbl UID
lbl_uid_new_eleve = Label(div_vue_eleve3, text="UID:")
lbl_uid_new_eleve.grid(row=0, column=1)

entry_uid_new_eleve = Entry(div_vue_eleve3)
entry_uid_new_eleve.grid(row=0, column=2)

#entry + lbl nom
lblNomAjoutEleve = Label(div_vue_eleve3, text="Nom:")
lblNomAjoutEleve.grid(row=0, column=3)

entryNomAjoutEleve = Entry(div_vue_eleve3)
entryNomAjoutEleve.grid(row=0, column=4)

#entry + lbl prenom
lblPrenomAjoutEleve = Label(div_vue_eleve3, text="Prenom:")
lblPrenomAjoutEleve.grid(row=0, column=5)

entryPrenomAjoutEleve = Entry(div_vue_eleve3)
entryPrenomAjoutEleve.grid(row=0, column=6)

#entry + lbl NCasier
lblNoCasierAjoutEleve = Label(div_vue_eleve3, text="N° Casier:")
lblNoCasierAjoutEleve.grid(row=0, column=7)

entryNoCasierAjoutEleve = Entry(div_vue_eleve3)
entryNoCasierAjoutEleve.grid(row=0, column=8)

# DropDownMenu
variable_new_eleve_class = StringVar(div_vue_eleve3)
options_new_eleve_class = liste_classe_eleve_reel()
new_eleve_class = ttk.Combobox(div_vue_eleve3, textvariable=variable_new_eleve_class, values=options_new_eleve_class, width=20, state="readonly")
new_eleve_class.grid(row=0, column=9)

# BtnVider
btn_vider_champ_eleve = Button(div_vue_eleve3, text="Vider", width=10, background="lightgrey", command=clear_formulaire_eleve)
btn_vider_champ_eleve.grid(row=1, column=7)

# BtnAjouter
btnModifierEleve = Button(div_vue_eleve3, text="Modifier", width=10, background="lightgrey") # #0BDB65
btnModifierEleve.grid(row=1, column=8)

# BtnAjouter
btnAddEleve = Button(div_vue_eleve3, text="Valider", width=10, background="lightgrey") # #05EE07
btnAddEleve.grid(row=1, column=9)

##########################################################################################################################################################


# Construction page d'accueil
####################################################################################################################################################

forget_all()
construction_accueil()

################################################################################################################################################


fenetre.mainloop()
