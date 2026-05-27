import tkinter as tk
from tkinter import messagebox

# Funktion zur Überprüfung der Benutzernamen
def check_names():
    # Liste aus dem Eingabefeld holen (durch Komma getrennt)
    names = entry.get().split(",")
    valid_names = []
    invalid_names = []
    
    for name in names:
        name = name.strip()  # Leerzeichen entfernen
        if len(name) > 3 and " " not in name:
            valid_names.append(name)
        else:
            invalid_names.append(name)
    
    # Ergebnis in einem Popup anzeigen
    result = f"Gültige Namen: {', '.join(valid_names)}\nUngültige Namen: {', '.join(invalid_names)}"
    messagebox.showinfo("Ergebnis", result)

# GUI erstellen
root = tk.Tk()
root.title("Benutzernamen Prüfer")
root.geometry("400x150")

# Eingabeaufforderung
label = tk.Label(root, text="Benutzernamen eingeben (mit Komma trennen):")
label.pack(pady=10)

# Eingabefeld
entry = tk.Entry(root, width=50)
entry.pack()

# Prüfen-Button
button = tk.Button(root, text="Prüfen", command=check_names)
button.pack(pady=10)

# Fenster starten
root.mainloop()
