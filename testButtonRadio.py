import tkinter as tk

# Création de la fenêtre principale
window = tk.Tk()

# Variable pour stocker la valeur sélectionnée
selected_option = tk.StringVar()

# Fonction appelée lorsqu'une option est sélectionnée
def option_selected():
    print("Option sélectionnée :", selected_option.get())

# Création des boutons radio
radio_button1 = tk.Radiobutton(window, text="Option 1", variable=selected_option, value="Option 1", command=option_selected)
radio_button1.pack()

radio_button2 = tk.Radiobutton(window, text="Option 2", variable=selected_option, value="Option 2", command=option_selected)
radio_button2.pack()

radio_button3 = tk.Radiobutton(window, text="Option 3", variable=selected_option, value="Option 3", command=option_selected)
radio_button3.pack()

# Afficher la fenêtre
window.mainloop()
