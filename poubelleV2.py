import tkinter as tk
import tkinter.messagebox as mbox

def afficher_message_warning():
    # Créer une fenêtre de message d'avertissement
    message_box = mbox._show("Avertissement", "Ceci est un message d'avertissement.", mbox.WARNING, parent=fenetre)

    # Fonction pour fermer la fenêtre du message d'avertissement
    def fermer_message():
        message_box.destroy()

    # Définir le délai en millisecondes
    delai = 1  # 5000 ms = 5 secondes

    # Planifier la fermeture de la fenêtre après le délai spécifié
    afficher_message_warning().after(delai, fermer_message)

fenetre = tk.Tk()

# Bouton pour afficher le message d'avertissement
bouton_avertissement = tk.Button(fenetre, text="Afficher Avertissement", command=afficher_message_warning)
bouton_avertissement.pack()

fenetre.mainloop()
