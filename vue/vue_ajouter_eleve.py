from tkinter import *
from tkinter import ttk
from bdd import *




# Fonction de mise à jour des données de la liste de gauche lors du changement de classe sélectionnée
def on_class_select(*args):
    update_data()


# Fonction de mise à jour des données de la liste de gauche en fonction de la classe sélectionnée
def update_data():
    selected_class = valeur_defaut_combobox_eleve.get()
    # Mettez à jour les données de la liste de gauche en fonction de la classe sélectionnée
    if selected_class == "2AMA Seconde Bac Pro TMA":
        # Efface les anciennes données
        my_tree_eleve.delete(*my_tree_eleve.get_children())
        # Insère de nouvelles données
        my_tree_eleve.insert(parent='', index='end', iid=0, values=(1, "tijou", "allan"))
        my_tree_eleve.insert(parent='', index='end', iid=1, values=(2, "viardot", "tibo"))
    elif selected_class == "1TMA Première Bac Pro TMA":
        # Efface les anciennes données
        my_tree_eleve.delete(*my_tree_eleve.get_children())
        # Insère de nouvelles données
        my_tree_eleve.insert(parent='', index='end', iid=0, values=(3, "dupont", "pierre"))
        my_tree_eleve.insert(parent='', index='end', iid=1, values=(4, "martin", "sophie"))



fenetre = Tk()

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
valeur_defaut_combobox_eleve = StringVar(div_vue_eleve)
liste_valeur_combobox_eleve = liste_classe_eleve()
select_classes = ttk.Combobox(div_vue_eleve, textvariable=valeur_defaut_combobox_eleve, values=liste_valeur_combobox_eleve, width=30)
select_classes.pack(side=LEFT)
select_classes.bind("<<ComboboxSelected>>", on_class_select)

# BLANK
blank_label = Label(div_vue_eleve, width=50)
blank_label.pack(side=LEFT)

# BtnEleve
btn_vers_casier = Button(div_vue_eleve, text="Gestion casier")
btn_vers_casier.pack(side=LEFT)

# BLANK
blank_label = Label(div_vue_eleve, width=10)
blank_label.pack(side=LEFT)

# BtnQuitter
btn_accueil_eleve = Button(div_vue_eleve, text="Accueil")
btn_accueil_eleve.pack(side=LEFT)

# Liste de gauche
my_tree_eleve = ttk.Treeview(sous_div_vue_eleve1)
my_tree_eleve['columns'] = ("Id", "nom", "prenom")
my_tree_eleve.column("#0", width=0, stretch=NO)
my_tree_eleve.column("Id", anchor=W, width=80)
my_tree_eleve.column("nom", anchor=W, width=150)
my_tree_eleve.column("prenom", anchor=W, width=150)
my_tree_eleve.heading("Id", text="Id")
my_tree_eleve.heading("nom", text="Nom")
my_tree_eleve.heading("prenom", text="Prenom")
my_tree_eleve.pack(side=LEFT)

# BtnAjouter
btnAddEleve = Button(div_vue_eleve3, text="Valider")
btnAddEleve.grid(row=0, column=0)

# ScanBadge
btnScanUidEleve = Button(div_vue_eleve3, text="Scan Badge")
btnScanUidEleve.grid(row=0, column=1)

# BtnAnnuler
btn_annuler_eleve = Button(div_vue_eleve3, text="Annuler")
btn_annuler_eleve.grid(row=1, column=0)

#entry + lbl UID
lbl_uid_new_eleve = Label(div_vue_eleve3, text="UID:")
lbl_uid_new_eleve.grid(row=1, column=1)

entry_uid_new_eleve = Entry(div_vue_eleve3)
entry_uid_new_eleve.grid(row=1, column=2)

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
new_eleve_class = ttk.Combobox(div_vue_eleve3, textvariable=variable_new_eleve_class, values=options_new_eleve_class, width=20)
new_eleve_class.grid(row=0, column=9)

fenetre.mainloop()
