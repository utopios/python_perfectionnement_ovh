import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Application démo")
fenetre.geometry("300x150")

label = tk.Label(fenetre, text="Je suis un label")
label.pack(pady=10)

bouton = tk.Button(fenetre, text="Je suis un bouton")
bouton.pack(pady=10)

fenetre.mainloop()