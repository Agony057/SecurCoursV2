from tkinter import *
from tkinter import ttk

fenetre = Tk()
fenetre.resizable(width=TRUE, height=TRUE)

div = Frame(fenetre)
div.pack(padx=20,pady=10)  # Ajout du padding à gauche et à droite de 20 pixels
div2 = Frame(fenetre)
div2.pack(pady=25)
div3 = Frame(fenetre)
div3.pack(pady=10)

sous_div1 = Frame(div2, height=200)
sous_div1.grid(row=0, column=0, sticky="nsew")

sous_div2 = Frame(div2)
sous_div2.grid(row=0, column=1, sticky="nsew",pady=25)

# Fonction de mise à jour des données de la liste de gauche en fonction de la classe sélectionnée
def update_data():
    selected_class = variable.get()
    # Mettez à jour les données de la liste de gauche en fonction de la classe sélectionnée
    if selected_class == "2AMA Seconde Bac Pro TMA":
        # Efface les anciennes données
        my_tree.delete(*my_tree.get_children())
        # Insère de nouvelles données
        my_tree.insert(parent='', index='end', iid=0, values=(1, "tijou", "allan"))
        my_tree.insert(parent='', index='end', iid=1, values=(2, "viardot", "tibo"))
    elif selected_class == "1TMA Première Bac Pro TMA":
        # Efface les anciennes données
        my_tree.delete(*my_tree.get_children())
        # Insère de nouvelles données
        my_tree.insert(parent='', index='end', iid=0, values=(3, "dupont", "pierre"))
        my_tree.insert(parent='', index='end', iid=1, values=(4, "martin", "sophie"))

    # Ajoutez des conditions pour les autres classes



# DropDownMenu
variable = StringVar(div)
variable.set("Sélectionner une classe")  # Valeur par défaut

options = ["Sélectionner une classe", "2AMA Seconde Bac Pro TMA", "1TMA Première Bac Pro TMA", "1MEN 1ère CAP MF", "TMEN Terminale CAP MF"]

# Fonction de mise à jour des données de la liste de gauche lors du changement de classe sélectionnée
def on_class_select(*args):
    update_data()

select_classes = ttk.Combobox(div, textvariable=variable, values=options,width=30)
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

# BtnQuitter
button2 = Button(div, text="Quitter")
button2.pack(side=LEFT)
#GRID

# BtnAjouter
btnAdd = Button(div3, text="Valider")
btnAdd.grid(row=0, column=0)

# ScanBadge
btnScan = Button(div3, text="Scan Badge")
btnScan.grid(row=0, column=1)

#entry + lbl nom
lblNom = Label(div3, text="Nom:")
lblNom.grid(row=0, column=3)

entryNom = Entry(div3)
entryNom.grid(row=0, column=4)

#entry + lbl prenom
lblPrenom = Label(div3, text="Prenom:")
lblPrenom.grid(row=0, column=5)

entryPrenom = Entry(div3)
entryPrenom.grid(row=0, column=6)

#entry + lbl NCasier
lblNCasier = Label(div3, text="N° Casier:")
lblNCasier.grid(row=0, column=7)

entryNCasier = Entry(div3)
entryNCasier.grid(row=0, column=8)

# DropDownMenu
variable_new_eleve_class = StringVar(div3)
variable_new_eleve_class.set("Sélectionner une classe")  # Valeur par défaut

options_new_eleve_class = ["Sélectionner une classe", "2AMA Seconde Bac Pro TMA", "1TMA Première Bac Pro TMA", "1MEN 1ère CAP MF", "TMEN Terminale CAP MF"]
new_eleve_class = ttk.Combobox(div3, textvariable=variable_new_eleve_class, values=options_new_eleve_class, width=20)
new_eleve_class.grid(row=0, column=9)

# BtnAnnuler
btnAnnuler = Button(div3, text="Annuler")
btnAnnuler.grid(row=1, column=0)

#entry + lbl IUD
lblIUD = Label(div3, text="IUD:")
lblIUD.grid(row=1, column=1)

entryIUD = Entry(div3)
entryIUD.grid(row=1, column=2)


# Liste de gauche
my_tree = ttk.Treeview(sous_div1)
my_tree['columns'] = ("Id", "nom", "prenom")
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Id", anchor=W, width=80)
my_tree.column("nom", anchor=W, width=150)
my_tree.column("prenom", anchor=W, width=150)
my_tree.heading("Id", text="Id")
my_tree.heading("nom", text="Nom")
my_tree.heading("prenom", text="Prenom")

my_tree.pack(side=LEFT)

fenetre.mainloop()
