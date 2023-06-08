import tkinter as tk
import tkinter.messagebox as mbox
from tkinter import font
from ListClasse import ListClasse
from PIL import ImageTk, Image
from bdd import *


def affichage_uid(id):
    res = ""
    for index, valeur in enumerate(id):
        print(index, valeur)
        if index == 3 or index == 7:
            res += "-" + valeur
        if index != 3 and index != 7:
            res += valeur
    print(res)
    return res


# Fonction déclenchée par l'appui sur le bouton SCAN
def lecture_uid():
    id = entry_Uid.get()
    print("Scan")
    # id = lecture() qui doit retourner l'uid (Max 16 chiffres)
    if id != "012-3456-789" and id == "987-6543-210":
        id = "0123456789"
    else:
        id = "9876543210"
    id = affichage_uid(id)
    entry_Uid.configure(state="normal")
    entry_Uid.delete(0, tk.END)
    entry_Uid.insert(tk.END, id)
    entry_Uid.configure(state="readonly")
    print("Lecture terminée")


def retour():
    result_retour = mbox.askyesno("Confirmation", "Etes-vous sûr de vouloir quitter ?")
    if result_retour:
        window.quit()


def verif_uid(uid):
    res = False
    if len(uid) == 0 or uid == "":
        res = True
        label_Uid_Error.grid_forget()
    elif len(uid) <= 16:
        if uid_existe(uid) == 1:
            utilisateur = identite_utilisateur_uid(uid)
            result_uid = mbox.askyesno("UID utilisé", "L'UID scanné est utilisé, \n "
                                                    f"Voulez vous remplacer l'utilisateur {utilisateur} ?")
            error = "UID utilisé"
            if result_uid:
                res = True
                label_Uid_Error.grid_forget()
                efface_uid(uid)
        else:
            res = True
            label_Uid_Error.grid_forget()
    else:
        error = "UID ne doit pas dépasser 16 caractères"

    if not res:
        label_Uid_Error.configure(text=error)
        label_Uid_Error.grid(row=1, columnspan=3, pady=10, padx=10)

    return res


def verif_nom(nom):
    res = False
    nomrepl = nom.replace("-", "")
    nomrepl = nomrepl.replace(" ", "")
    if len(nom) >= 2 and nomrepl.isalpha():
        res = True
        label_Nom_Error.grid_forget()
    else:
        label_Nom_Error.grid(row=3, columnspan=3, pady=10, padx=10)
        label_Nom_Error.configure(text="2 caractères minimum et uniquement des lettres")
    return res


def verif_prenom(prenom):
    res = False
    prenomrepl = prenom.replace("-", "")
    prenomrepl = prenomrepl.replace(" ", "")
    if len(prenom) >= 2 and prenomrepl.isalpha():
        res = True
        label_Prenom_Error.grid_forget()
    else:
        label_Prenom_Error.grid(row=5, columnspan=3, pady=10, padx=10)
        label_Prenom_Error.configure(text="2 caractères minimum et uniquement des lettres")
    return res


def verif_classe(classe):
    verifClasse = classe in ListClasse.LIBELLE.value
    res = False
    if verifClasse:
        res = True
        label_Classe_Error.grid_forget()
    else:
        label_Classe_Error.grid(row=7, columnspan=3, pady=10, padx=10)
        label_Classe_Error.configure(text="Erreur dans le libellé de la classe")
    return res


def verif_casier(casier):
    res = False
    if len(casier) == 0:
        res = True
        label_Casier_Error.grid_forget()
    elif casier.isdigit():
        if 1 <= int(casier) <= 2:
            if demande_casier(casier) > 0:
                utilisateur = identite_utilsateur_casier(casier)
                result_casier = mbox.askyesno("Casier occupé", "Le casier selectionné est occupé, \n "
                                               f"Voulez vous remplacer l'utilisateur {utilisateur} ?")
                error = "Casier occupé"
                if result_casier:
                    res = True
                    label_Casier_Error.grid_forget()
                    efface_casier(casier)
            else:
                casier_libre_occupe(casier)
                res = True
                label_Casier_Error.grid_forget()
        else:
            error = "Numero de casier inexistant"
    else:
        error = "numero de casier doit etre un entier !"
    if not res:
        label_Casier_Error.grid(row=9, columnspan=3, pady=10, padx=10)
        label_Casier_Error.configure(text=error)
    return res


def verification():
    # Recuperation des informations
    res = False
    uid = entry_Uid.get().strip()
    nom = entryNom.get().upper().strip()
    prenom = entryPrenom.get().capitalize().strip()
    classe = entryClasse.get().capitalize().strip()
    casier = entryNoCasier.get().strip()

    print("Verif")  # Pour visualiser à quelle étape nous sommes

    if verif_uid(uid) & verif_nom(nom) & verif_prenom(prenom) & verif_classe(classe) & verif_casier(casier):
        print()
        print("Fin validation")
        print()
        res = True
        validation(uid, nom, prenom, classe, casier)
    else:
        mbox.showerror("Erreur !", message="Corrigez les erreurs !")
    return res


def verification_Entrer(event):
    verification()


def creation_identifiant(nom, prenom):
    base_id = nom.upper()
    chiffre = 1
    identifiant = base_id + str(chiffre)

    # On vérifie si l'identifiant existe déjà dans la base de données
    while identifiant_existe(identifiant) == 1:
        identifiant = base_id + str(chiffre)
        chiffre += 1

    return identifiant


def validation(uid, nom, prenom, classe, casier):
    count = demande_ajout(nom, prenom, classe)
    if count > 0:
        result_eleve = mbox.askyesno("Elève existant !", "Il existe au moins un élève avec le même nom et le même prénom dans cette classe. \n"
                                           "Continuer l'ajout ?")
        if result_eleve:
            print("yes")
            identifiant = creation_identifiant(nom, prenom)
            ajout(uid, identifiant, nom, prenom, classe, casier)
    else:
        result_final = mbox.askyesno("Confirmation avant ajout", f"uid : {uid} \n nom : {nom} \n "
                                                           f"prenom : {prenom} \n "
                                                           f"classe : {classe} \n "
                                                           f"casier : {casier} \n "
                                                           f"Est-ce correct ?")
        if result_final:
            print("yes")
            identifiant = creation_identifiant(nom, prenom)
            ajout(uid, identifiant, nom, prenom, classe, casier)

def switch_to_second_page():
    # Destruction des éléments de la première page
    label_NoCarte.grid_forget()
    label_Nom.grid_forget()
    label_Prenom.grid_forget()
    label_Classe.grid_forget()
    label_NoCasier.grid_forget()

    entry_Uid.grid_forget()
    entryNom.grid_forget()
    entryPrenom.grid_forget()
    entryClasse.grid_forget()
    entryNoCasier.grid_forget()

    button_Retour.grid_forget()
    button_Uid.grid_forget()
    button_Valider.grid_forget()
    button_suivant.grid_forget()


    # Création des éléments de la deuxième page
    label2 = tk.Label(window, text="Deuxième page")
    label2.grid(row=55, columnspan=3)
    label_NoCarte.grid(row=56, column=0)
    label_Nom.grid(row=57, column=0)
    label_Prenom.grid(row=58, column=0)
    label_Classe.grid(row=59, column=0)
    label_NoCasier.grid(row=60, column=0)

    entry_Uid.grid(row=56, column=1)
    entryNom.grid(row=57, column=1)
    entryPrenom.grid(row=58, column=1)
    entryClasse.grid(row=59, column=1)
    entryNoCasier.grid(row=60, column=1)

    button_Uid.grid(row=56, column=2)
    button_Valider.grid(row=61, columnspan=3)
    button_Retour.grid(row=62, columnspan=3)




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
grandePolice = font.Font(size=25)
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
label_Prenom.grid(row=4, column=0, pady=10, padx=10)

entryPrenom = tk.Entry(window)
entryPrenom.bind("<Return>", verification_Entrer)
entryPrenom.grid(row=4, column=1, pady=10, padx=10)

label_Prenom_Error = tk.Label(window, foreground="red")

# Classe
label_Classe = tk.Label(window, text="Classe :")
label_Classe.grid(row=6, column=0, pady=10, padx=10)

entryClasse = tk.Entry(window)
entryClasse.bind("<Return>", verification_Entrer)
entryClasse.grid(row=6, column=1, pady=10, padx=10)

label_Classe_Error = tk.Label(window, foreground="red")

# Casier
label_NoCasier = tk.Label(window, text="N° Casier :")
label_NoCasier.grid(row=8, column=0, pady=10, padx=10)

entryNoCasier = tk.Entry(window)
entryNoCasier.bind("<Return>", verification_Entrer)
entryNoCasier.grid(row=8, column=1, pady=10, padx=10)

label_Casier_Error = tk.Label(window, foreground="red")

# Valider
button_Valider = tk.Button(window, text="Valider", command=verification,
                           background="lightgreen", cursor="hand2", width=7)
button_Valider.grid(row=10, columnspan=3, pady=10, padx=10)

# Retour
button_Retour = tk.Button(window, text="Annuler", command=retour,
                          background="orange", cursor="hand2", width=7)
button_Retour.grid(row=11, columnspan=3, pady=10, padx=10)

# Suivant
button_suivant = tk.Button(window, text="Suivant", command=switch_to_second_page,
                          background="orange", cursor="hand2", width=7)
button_suivant.grid(row=12, columnspan=3, pady=10, padx=10)

window.mainloop()
