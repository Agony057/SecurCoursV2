from tkinter import *
from tkinter import ttk
from bdd import *

# Fonction de mise à jour des données de la liste de gauche en fonction de la classe sélectionnée
def update_data_casier():
    # Désactiver bouton valider tant qu'aucune ligne n'est sélectionné
    button_valider.configure(state="disabled")

    # recupération du nom de la classe
    classe = valeur_defaut_combobox_casier.get()

    if classe == "Toutes_les_classes":
        eleves = liste_eleve_avec_casier()
    else:
        # recuperation de liste d'eleve de la classe du dropdown
        eleves = liste_eleve_avec_casier_par_classe(classe)

    # on efface la liste pré-existante
    my_tree_casier.delete(*my_tree_casier.get_children())

    # on insère les eleves un par un dans la liste
    for eleve in eleves:
        my_tree_casier.insert(parent='', index='end', values=(eleve[0], eleve[1], eleve[2]))


# Fonction appelée lorsque vous sélectionnez un élément de la liste de gauche
def on_tree_casier_select(event):
    button_valider.configure(state="normal")


# Fonction de mise à jour des données de la liste de gauche lors du changement de classe sélectionnée
def on_class_casier_select(*args):
    # Désactiver bouton valider tant qu'aucune ligne n'est sélectionné
    button_valider.configure(state="disabled")
    update_data_casier()


def casier_click_on_valider():
    # Désactiver bouton valider tant qu'aucune ligne n'est sélectionné
    button_valider.configure(state="disabled")
    # Récupère l'élément sélectionné
    selected_item = my_tree_casier.focus()
    # Récupère les valeurs de l'élément sélectionné
    casier_values = my_tree_casier.item(selected_item, 'values')
    print(casier_values[0] + " " + casier_values[1] + " " + casier_values[2] + " " + str(choix_radio_btn_casier.get()))


fenetre = Tk()

div_page_casier = Frame(fenetre)
div_page_casier.pack(padx=20, pady=10)  # Ajout du padding à gauche et à droite de 20 pixels
div2_page_casier = Frame(fenetre)
div2_page_casier.pack(pady=25)

sous_div1_page_casier = Frame(div2_page_casier, height=200)
sous_div1_page_casier.grid(row=0, column=0, sticky="nsew")

sous_div2_page_casier = Frame(div2_page_casier)
sous_div2_page_casier.grid(row=0, column=1, sticky="nsew", pady=25)

# DropDownMenu
valeur_defaut_combobox_casier = StringVar(div_page_casier)
liste_valeur_combobox_casier = liste_classe_eleve()

select_casier_classes = ttk.Combobox(div_page_casier, textvariable=valeur_defaut_combobox_casier, values=liste_valeur_combobox_casier, width=30, state="readonly")
select_casier_classes.pack(side=LEFT)
select_casier_classes.bind("<<ComboboxSelected>>", on_class_casier_select)
select_casier_classes.current(4)

# BLANK
blank_label = Label(div_page_casier,text="MODE ADMIN", width=50)
blank_label.pack(side=LEFT)

# BtnEleve
btn_eleve = Button(div_page_casier, text="Gestion elèves")
btn_eleve.pack(side=LEFT)

# BLANK
blank_label = Label(div_page_casier, width=10)
blank_label.pack(side=LEFT)

# BtnQuitter
btn_accueil_casier = Button(div_page_casier, text="Accueil")
btn_accueil_casier.pack(side=LEFT)

# Liste de gauche
my_tree_casier = ttk.Treeview(sous_div1_page_casier)
my_tree_casier['columns'] = ("NoCasier", "nom", "prenom")
my_tree_casier.column("#0", width=0, stretch=NO)
my_tree_casier.column("NoCasier", anchor=W, width=80)
my_tree_casier.column("nom", anchor=W, width=150)
my_tree_casier.column("prenom", anchor=W, width=150)
my_tree_casier.heading("NoCasier", text="N° Casier")
my_tree_casier.heading("nom", text="Nom")
my_tree_casier.heading("prenom", text="Prenom")
my_tree_casier.bind("<<TreeviewSelect>>", on_tree_casier_select)  # Appelle la fonction lorsqu'un élément est sélectionné
my_tree_casier.pack(side=LEFT)

# Crée les Radiobuttons
choix_radio_btn_casier = StringVar()
choix_radio_btn_casier.set("a_oublie_son_badge")
btn_radio_oublie_badge = Radiobutton(sous_div2_page_casier, text="a oublié son badge", variable=choix_radio_btn_casier, value="a_oublie_son_badge")
btn_radio_oublie_cle = Radiobutton(sous_div2_page_casier, text="ouvrir casier clé", variable=choix_radio_btn_casier, value="ouvrir_casier_cle")
btn_radio_oublie_telephone = Radiobutton(sous_div2_page_casier, text="ouvrir casier téléphone", variable=choix_radio_btn_casier, value="ouvrir_casier_telephone")

btn_radio_oublie_badge.pack(anchor=W)
btn_radio_oublie_cle.pack(anchor=W)
btn_radio_oublie_telephone.pack(anchor=W)

button_valider = Button(sous_div2_page_casier, text="Valider", state="disabled", command=casier_click_on_valider)
button_valider.pack(side=BOTTOM)

update_data_casier()
fenetre.mainloop()
