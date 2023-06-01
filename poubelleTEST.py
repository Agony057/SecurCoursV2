import tkinter as tk
from tkinter import ttk

# Création de la fenêtre principale
window = tk.Tk()

# Fonction appelée lors de la sélection d'un élément dans la liste déroulante
def selection_change(event):
    selected_item = dropdown.get()
    print("Élément sélectionné :", selected_item)

# Liste des options de la liste déroulante
options = ["Option 1", "Option 2", "Option 3", "Option 4"]

# Création de la liste déroulante
dropdown = ttk.Combobox(window, values=options)
dropdown.pack()

# Associer la fonction de sélection à l'événement "<<ComboboxSelected>>"
dropdown.bind("<<ComboboxSelected>>", selection_change)

# Afficher la fenêtre
window.mainloop()
