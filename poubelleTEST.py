import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import font
from ListClasse import ListClasse
from PIL import ImageTk, Image
from bdd import *

# Création de la fenêtre principale
window = tk.Tk()

# Fonction appelée lors de la sélection d'un élément dans la liste déroulante
def selection_change(event):
    classe = dropdown.get().split(" ")[0]
    update_list(classe)


# Fonction pour mettre à jour la liste en fonction de la classe sélectionnée
def update_list(classe):
    # Effacer les anciens éléments de la liste
    liste.delete(0, tk.END)
    # Obtenir les nouveaux éléments en fonction de la classe sélectionnée
    elements = liste_eleve_avec_casier_par_classe(classe)
    # Ajouter les nouveaux éléments à la liste
    for element in elements:
        liste.insert(tk.END, element)


def valider_selection():
    # Récupérer l'élément sélectionné dans la liste
    index = liste.curselection()
    if index:
        element = liste.get(index)
        print("Élément sélectionné :", element[1] + " " + selected_option.get())


# Variable pour stocker la valeur sélectionnée
selected_option = tk.StringVar()
selected_option.set("N'a pas de carte")  # Définit la valeur sélectionnée par défaut


# Fonction appelée lorsqu'une option est sélectionnée
# def option_selected():
    # print("Option sélectionnée :", selected_option.get())


# Liste des options de la liste déroulante
options = liste_classe_eleve()

# Création de la liste déroulante
dropdown = ttk.Combobox(window, values=options, width=40)
dropdown.grid(row=0, column=0, padx=10, pady=10)
# Associer la fonction de sélection à l'événement "<<ComboboxSelected>>"
dropdown.bind("<<ComboboxSelected>>", selection_change)

# Créer une liste
liste = tk.Listbox(window, selectmode=tk.SINGLE, width=43, height=20, cursor='hand2')
liste.grid(row=1, column=0, rowspan=3, padx=10, pady=10)

# Ajouter des éléments à la liste en fonction de l'option initiale sélectionnée
classe_initiale = dropdown.get().split(" ")[0]
elements = liste_eleve_avec_casier()
for element in elements:
    liste.insert(tk.END, element)

liste.selection_set(0)


# Création des boutons radio
radio_button1 = tk.Radiobutton(window, text="N'a pas de carte", variable=selected_option, value="N'a pas de carte", width=20)
radio_button1.grid(row=1, column=1)

radio_button2 = tk.Radiobutton(window, text="N'a pas de téléphone", variable=selected_option, value="N'a pas de téléphone", width=20)
radio_button2.grid(row=2, column=1)

radio_button3 = tk.Radiobutton(window, text="N'a pas de clef", variable=selected_option, value="N'a pas de clef", width=20)
radio_button3.grid(row=3, column=1)

# Bouton pour afficher la sélection
bouton_valider = tk.Button(window, text="Valider", command=valider_selection)
bouton_valider.grid(row=1, column=2, rowspan=3)

# Afficher la fenêtre
window.mainloop()
