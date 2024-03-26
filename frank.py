import tkinter as tk
from tkinter import ttk
import webbrowser

class CalculatorApp:
    def __init__(self, root):
        self.root = root  # Ajout de la référence à la fenêtre principale
        self.dark_theme = True  # Ajout d'une variable pour suivre le thème actuel
        root.title("Calculatrice")
        root.geometry("300x400")
        root.configure(bg="black")

        self.result_var = tk.StringVar()
        self.create_widgets(root)

    def create_widgets(self, root):
        # Affichage du résultat
        result_entry = ttk.Entry(root, textvariable=self.result_var, font=("Arial", 20), justify="right", state="disabled")
        result_entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Boutons pour les chiffres et opérations
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, col) in buttons:
            btn = ttk.Button(root, text=text, command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, sticky="nsew")

        # Bouton "C" pour effacer les calculs
        clear_btn = ttk.Button(root, text="C", command=self.clear_result)
        clear_btn.grid(row=5, column=3, sticky="nsew")

        # Bouton pour changer de thème
        theme_btn = ttk.Button(root, text="Changer de thème", command=self.toggle_theme)
        theme_btn.grid(row=5, column=0, columnspan=3, sticky="nsew")

        # Bouton pour ouvrir le lien du jeu 
        pokemon_btn = ttk.Button(root, text="Jouer à Pokémon Rouge", command=self.open_pokemon_link)
        pokemon_btn.grid(row=6, column=0, columnspan=4, sticky="nsew")

        # Configuration du redimensionnement des boutons
        for i in range(7):
            root.grid_rowconfigure(i, weight=1)
            root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, value):
        if value == "=":
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Erreur")
        else:
            current_text = self.result_var.get()
            self.result_var.set(current_text + value)

    def clear_result(self):
        self.result_var.set("")

    def toggle_theme(self):
        if self.dark_theme:
            self.dark_theme = False
            self.change_theme("black", "white")
        else:
            self.dark_theme = True
            self.change_theme("white", "black")

    def change_theme(self, bg_color, fg_color):
        for widget in self.root.winfo_children():
            widget.configure(bg=bg_color, fg=fg_color)

    def open_pokemon_link(self):
        webbrowser.open("https://www.gameslol.net/pokemon-rouge-feu-954.html")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()