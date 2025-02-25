import tkinter as tk
from tkinter import messagebox
fenetre = tk.Tk()
fenetre.title("Application démo")
fenetre.geometry("300x150")

label = tk.Label(fenetre, text="Je suis un label")
label.pack(pady=10)

def saluer():
    messagebox.showinfo("Bonjour tout le monde")

bouton = tk.Button(fenetre, text="Je suis un bouton", command=saluer)
bouton.pack(pady=10)

fenetre.mainloop()