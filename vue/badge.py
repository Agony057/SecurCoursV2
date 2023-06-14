# coding: utf-8

from tkinter import *

def accueil():
    fenetre = Tk()

    label_accueil = Label(fenetre, text="Veuillez passez votre badge")
    # label.pack(pady=20, padx=20)
    label_accueil.pack()
    fenetre.geometry("400x300")
    label_accueil.place(relx=0.5, rely=0.5, anchor=CENTER)

    fenetre.mainloop()