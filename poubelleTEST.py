import tkinter as tk
from tkinter import ttk, messagebox

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



# Éléments de la grille
# label1 = tk.Entry(window, text="Élément 1")
# label1.grid(row=1, column=0, padx=10, pady=10)  # Espacement de 10 pixels
#
# label2 = tk.Entry(window, text="Élément 2")
# label2.grid(row=1, column=1, padx=10, pady=10)  # Espacement de 10 pixels
#
# label3 = tk.Entry(window, text="Élément 3")
# label3.grid(row=2, column=0, padx=10, pady=10)  # Espacement de 10 pixels
#
# label4 = tk.Entry(window, text="Élément 4")
# label4.grid(row=2, column=1, padx=10, pady=10)  # Espacement de 10 pixels


import tkinter.messagebox as mbox

def afficher_message_warning():
    messagebox.showwarning("Avertissement", "Ceci est un message d'avertissement.")

    # Définir le délai en millisecondes
    delai = 5000  # 5000 ms = 5 secondes

    # Fonction pour masquer le message d'avertissement après le délai
    def masquer_message():
        message_box.destroy()

    # Créer une fenêtre de message d'avertissement
    message_box = mbox._show("Avertissement", "Ceci est un message d'avertissement", mbox.WARNING)

    # Définir le rappel après le délai
    message_box.after(delai, masquer_message)


# Bouton pour afficher le message d'avertissement
bouton_avertissement = tk.Button(window, text="Afficher Avertissement", command=afficher_message_warning)
bouton_avertissement.pack()


# Afficher la fenêtre
window.mainloop()
