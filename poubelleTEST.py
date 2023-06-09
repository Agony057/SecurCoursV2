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
    elements = liste_eleve_par_classe(classe)
    # Ajouter les nouveaux éléments à la liste
    for element in elements:
        liste.insert(tk.END, element)

# Liste des options de la liste déroulante
options = liste_classe_eleve()

# Création de la liste déroulante
dropdown = ttk.Combobox(window, values=options, width=40)
dropdown.pack()

# Associer la fonction de sélection à l'événement "<<ComboboxSelected>>"
dropdown.bind("<<ComboboxSelected>>", selection_change)


def afficher_selection():
    # Récupérer l'élément sélectionné dans la liste
    index = liste.curselection()
    if index:
        element = liste.get(index)
        print("Élément sélectionné :", element[1])

# Créer une liste
liste = tk.Listbox(window, selectmode=tk.SINGLE, width=40, height=25, justify='center', cursor='hand2')
liste.pack()

# Ajouter des éléments à la liste en fonction de l'option initiale sélectionnée
classe_initiale = dropdown.get().split(" ")[0]
elements = liste_eleve()
for element in elements:
    liste.insert(tk.END, element)

# Bouton pour afficher la sélection
bouton_afficher = tk.Button(window, text="Afficher la sélection", command=afficher_selection)
bouton_afficher.pack()

# Afficher la fenêtre
window.mainloop()
