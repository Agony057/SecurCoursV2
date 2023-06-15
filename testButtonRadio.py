from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox as mbox

from ListClasse import ListClasse
from bdd import *


# fonction eleves
#####################################################################################################################################################################

# Fonction de mise à jour des données de la liste de gauche en fonction de la classe sélectionnée
def update_data_vue_eleve():
    # recupération du nom de la classe
    classe = valeur_defaut_combobox_eleve.get()

    if classe == "Toutes_les_classes":
        eleves = liste_eleve()
    else:
        # recuperation de liste d'eleve de la classe du dropdown
        eleves = liste_eleve_par_classe(classe)

    # on efface la liste pré-existante
    my_tree_eleve.delete(*my_tree_eleve.get_children())

    # on insère les eleves un par un dans la liste
    for eleve in eleves:
        my_tree_eleve.insert(parent='', index='end', values=(eleve[0], eleve[1], eleve[2]))

# Fonction appelée lorsque vous sélectionnez un élément de la liste de gauche
def on_tree_eleve_select(event):
    selected_item = my_tree_eleve.focus()  # Récupère l'élément sélectionné
    if len(selected_item) > 0:
        id = my_tree_eleve.item(selected_item, 'values')[1]  # Récupère les valeurs de l'élément sélectionné
        recuperer_info_avec_id(id)


# Fonction de mise à jour des données de la liste de gauche lors du changement de classe sélectionnée
def on_class_eleve_select(*args):
    update_data_vue_eleve()


########################################################################################################################################################


# fonction casier
########################################################################################################################################################

# Fonction de mise à jour des données de la liste de gauche en fonction de la classe sélectionnée
def update_data_casier():
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
    # Désactiver bouton valider tant qu'aucune ligne n'est sélectionné
    button_valider_casier.configure(state="disabled")


# Fonction appelée lorsque vous sélectionnez un élément de la liste de gauche
def on_tree_casier_select(event):
    button_valider_casier.configure(state="normal")


# Fonction de mise à jour des données de la liste de gauche lors du changement de classe sélectionnée
def on_class_casier_select(*args):
    # Désactiver bouton valider tant qu'aucune ligne n'est sélectionné
    update_data_casier()
    # button_valider_casier.configure(state="disabled")


def casier_click_on_valider():
    # Récupère l'élément sélectionné
    selected_item = my_tree_casier.focus()
    # Récupère les valeurs de l'élément sélectionné
    casier_values = my_tree_casier.item(selected_item, 'values')
    mbox.showwarning("information",casier_values[0] + " "+ str(choix_radio_btn_casier.get()))
    print(casier_values[0] + " " + casier_values[1] + " " + casier_values[2] + " " + str(choix_radio_btn_casier.get()))
    # Désactiver bouton valider tant qu'aucune ligne n'est sélectionné
    button_valider_casier.configure(state="disabled")

########################################################################################################################################################


# fonction verfication formulaire
########################################################################################################################################################

def verif_uid(uid):
    res = False
    id = label_id_eleve.cget("text")
    if len(uid) == 0 or uid == "":
        res = True
        lbl_error_uid.grid_forget()
    elif len(uid) <= 16 and uid.replace("-", "").isdigit():
        if uid_existe(uid) == 1 and len(id) == 0:
            utilisateur = identite_utilisateur_uid(uid)
            result_uid = mbox.askyesno("UID utilisé", "L'UID scanné est utilisé, \n "
                                                    f"Voulez vous remplacer l'utilisateur {utilisateur} ?")
            error = "UID utilisé"
            if result_uid:
                res = True
                lbl_error_uid.grid(row=2, column=0, columnspan=10)
                efface_uid(uid)
        else:
            res = True
            lbl_error_uid.grid_forget()
    else:
        error = "UID ne doit pas dépasser 16 caractères"

    if not res:
        lbl_error_uid.configure(text=error)
        lbl_error_uid.grid(row=2, column=0, columnspan=10)

    return res

def verif_nom(nom):
    res = False
    nomrepl = nom.replace("-", "")
    nomrepl = nomrepl.replace(" ", "")
    if len(nom) >= 2 and nomrepl.isalpha():
        res = True
        lbl_error_nom.grid_forget()
    else:
        lbl_error_nom.grid(row=3, columnspan=10)
        lbl_error_nom.configure(text="2 caractères minimum et uniquement des lettres")
    return res


def verif_prenom(prenom):
    res = False
    prenomrepl = prenom.replace("-", "")
    prenomrepl = prenomrepl.replace(" ", "")
    if len(prenom) >= 2 and prenomrepl.isalpha():
        res = True
        lbl_error_prenom.grid_forget()
    else:
        lbl_error_prenom.grid(row=5, columnspan=10)
        lbl_error_prenom.configure(text="2 caractères minimum et uniquement des lettres")
    return res


def verif_classe(classe):
    verifClasse = classe in ListClasse.LIBELLE.value
    res = False
    if verifClasse:
        res = True
        lbl_error_classe.grid_forget()
    else:
        lbl_error_classe.grid(row=7, columnspan=10)
        lbl_error_classe.configure(text="Erreur dans le libellé de la classe")
    return res


def verif_casier(casier):
    res = False
    id = label_id_eleve.cget("text")
    if len(casier) == 0:
        res = True
        lbl_error_casier.grid_forget()
    elif casier.isdigit():
        if 1 <= int(casier) <= 6:
            if demande_casier(casier) > 0 and len(id) == 0:
                utilisateur = identite_utilsateur_casier(casier)
                result_casier = mbox.askyesno("Casier occupé", "Le casier selectionné est occupé, \n "
                                               f"Voulez vous remplacer l'utilisateur {utilisateur} ?")
                error = "Casier occupé"
                if result_casier:
                    res = True
                    lbl_error_casier.grid_forget()
                    efface_casier(casier)
            else:
                casier_libre_occupe(casier)
                res = True
                lbl_error_casier.grid_forget()
        else:
            error = "Numero de casier inexistant"
    else:
        error = "numero de casier doit etre un entier !"
    if not res:
        lbl_error_casier.grid(row=9, columnspan=10)
        lbl_error_casier.configure(text=error)
    return res

########################################################################################################################################################


# fonction formulaire eleve
########################################################################################################################################################

def verification_Entrer(event):
    verifier_donnee_formulaire()


def verifier_donnee_formulaire():
    res = False
    uid = entry_uid_new_eleve.get().strip()
    nom = entryNomAjoutEleve.get().upper().strip()
    prenom = entryPrenomAjoutEleve.get().capitalize().strip()
    casier = entryNoCasierAjoutEleve.get().strip()
    classe = new_eleve_class.get()

    if verif_uid(uid) & verif_nom(nom) & verif_prenom(prenom) & verif_classe(classe) & verif_casier(casier):
        print()
        print("Fin validation")
        print()
        res = True
        validation(uid, nom, prenom, classe, casier)
    else:
        mbox.showerror("Erreur !", message="Corrigez les erreurs !")
    return res


def creation_identifiant(nom):
    base_id = nom[:10].upper()
    chiffre = 1
    identifiant = base_id + str(chiffre)

    # On vérifie si l'identifiant existe déjà dans la base de données
    while identifiant_existe(identifiant) == 1:
        identifiant = base_id + str(chiffre)
        chiffre += 1

    return identifiant


def validation(uid, nom, prenom, classe, casier):
    count = demande_ajout(nom, prenom, classe)
    id = label_id_eleve.cget("text")
    res = False
    if count > 0 and len(id) == 0:
        result_eleve = mbox.askyesno("Elève existant !", "Il existe au moins un élève avec le même nom et le même prénom dans cette classe. \n"
                                           "Continuer l'ajout ?")
        if result_eleve:
            print("yes")
            res = True
    else:
        result_final = mbox.askyesno("Confirmation avant ajout", f"uid : {uid} \n nom : {nom} \n "
                                                           f"prenom : {prenom} \n "
                                                           f"classe : {classe} \n "
                                                           f"casier : {casier} \n "
                                                           f"Est-ce correct ?")
        if result_final:
            print("yes")
            res = True
    if res:
        if len(id) > 0:
            supprimer_eleve(id)

        identifiant = creation_identifiant(nom)
        ajout_eleve(uid, identifiant, nom, prenom, classe, casier)
        clear_formulaire_eleve()
        update_data_vue_eleve()

def ajout_on_click():
    verifier_donnee_formulaire()


def supprimer_on_click():
    id = label_id_eleve.cget("text")
    if len(id) > 0:
        utilisateur = obtenir_info_avec_id(id)
        confirm = mbox.askyesno("Attention suppression imminente !",
                                f"Vous vous apprêtez à supprimer l'élève {utilisateur[1], utilisateur[2], utilisateur[4]}."
                                f"Supprimer ?")
        if confirm:
            supprimer_eleve(id)
            clear_formulaire_eleve()
            update_data_vue_eleve()


def clear_formulaire_eleve():
    label_id_eleve.configure(text="")
    entry_uid_new_eleve.delete(0, tk.END)
    entryNomAjoutEleve.delete(0, tk.END)
    entryPrenomAjoutEleve.delete(0, tk.END)
    entryNoCasierAjoutEleve.delete(0, tk.END)
    new_eleve_class.set("Selection de la classe")


def recuperer_info_avec_id(id):
    info_eleve = obtenir_info_avec_id(id)
    remplir_formulaire_ajout_eleve(info_eleve)


def remplir_formulaire_ajout_eleve(eleve):
    clear_formulaire_eleve()
    if eleve[0] is not None:
        entry_uid_new_eleve.insert(tk.END, eleve[0])
    entryNomAjoutEleve.insert(tk.END, eleve[1])
    entryPrenomAjoutEleve.insert(tk.END, eleve[2])
    if eleve[3] is not None:
        entryNoCasierAjoutEleve.insert(tk.END, eleve[3])
    new_eleve_class.set(eleve[4])
    label_id_eleve.configure(text=eleve[5])

########################################################################################################################################################

# fonction forget
########################################################################################################################################################

def forget_all():
    forget_page_accueil()
    forget_page_eleve()
    forget_page_casier()


def forget_page_casier():
    div_page_casier.pack_forget()
    div2_page_casier.pack_forget()


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
    div_page_casier.pack(padx=20, pady=10)
    div2_page_casier.pack(pady=25)
    select_casier_classes.current(4)
    update_data_casier()


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
testbouton = Button(fenetre, text="simulation carte admin", command=construction_page_casier)
testbouton.pack()

#################################################################################################################################################################


# Casier
#######################################################################################################################################################

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
btn_eleve = Button(div_page_casier, text="Gestion elèves", command=construction_page_eleve)
btn_eleve.pack(side=LEFT)

# BLANK
blank_label = Label(div_page_casier, width=10)
blank_label.pack(side=LEFT)

# BtnQuitter
btn_accueil_casier = Button(div_page_casier, text="Accueil", command=retour_accueil)
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

button_valider_casier = Button(sous_div2_page_casier, text="Valider", state="disabled", command=casier_click_on_valider)
button_valider_casier.pack(side=BOTTOM)

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
btn_vers_casier = Button(div_vue_eleve, text="Gestion casier", width=11, background="lightgrey", command=construction_page_casier)
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
my_tree_eleve.heading("nom", text="id")
my_tree_eleve.heading("prenom", text="Prenom")
my_tree_eleve.pack(side=LEFT)
my_tree_eleve.bind("<<TreeviewSelect>>", on_tree_eleve_select)

# ScanBadge
btnScanUidEleve = Button(div_vue_eleve3, text="Scanner Badge", width=12, background="lightgrey")
btnScanUidEleve.grid(row=0, column=0)

#entry + lbl UID
lbl_uid_new_eleve = Label(div_vue_eleve3, text="UID:")
lbl_uid_new_eleve.grid(row=0, column=1)

entry_uid_new_eleve = Entry(div_vue_eleve3)
entry_uid_new_eleve.grid(row=0, column=2)

#label id eleve
label_id_eleve = Label(div_vue_eleve3, text="")

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

# BtnSupprimer
btn_supprimer_eleve = Button(div_vue_eleve3, text="Supprimer", width=10, background="#D21F3C", command=supprimer_on_click)
btn_supprimer_eleve.grid(row=1, column=7)

# BtnVider
btn_vider_champ_eleve = Button(div_vue_eleve3, text="Vider", width=10, background="lightgrey", command=clear_formulaire_eleve)
btn_vider_champ_eleve.grid(row=1, column=8)

# BtnAjouter
btnAddEleve = Button(div_vue_eleve3, text="Valider", width=10, background="lightgreen", command=ajout_on_click) # #05EE07
btnAddEleve.grid(row=1, column=9)

# Liste d'erreur
lbl_error_uid = Label(div_vue_eleve3, text="", fg="red")
lbl_error_nom = Label(div_vue_eleve3, text="", fg="red")
lbl_error_prenom = Label(div_vue_eleve3, text="", fg="red")
lbl_error_casier = Label(div_vue_eleve3, text="", fg="red")
lbl_error_classe = Label(div_vue_eleve3, text="", fg="red")

##########################################################################################################################################################


# Construction page d'accueil
####################################################################################################################################################

forget_all()
construction_accueil()

################################################################################################################################################


fenetre.mainloop()
