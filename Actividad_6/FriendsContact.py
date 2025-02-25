import tkinter as tk
from tkinter import messagebox
import os

class FriendsContact:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda de Contactos")
        self.root.geometry("500x180")

        
        tk.Label(root, text="Nombre").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(root, text="Número").grid(row=1, column=0, padx=5, pady=5)

        self.name_entry = tk.Entry(root, width=35)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.number_entry = tk.Entry(root, width=35)
        self.number_entry.grid(row=1, column=1, padx=5, pady=5)

        button_frame = tk.Frame(root)
        button_frame.grid(row=2, column=0, columnspan=2, pady=10)

        buttons = [
            ("Crear", self.create_contact),
            ("Leer", self.read_contact),
            ("Actualizar", self.update_contact),
            ("Borrar", self.delete_contact),
            ("Limpiar", self.clear_fields)
        ]

        for text, command in buttons:
            tk.Button(button_frame, text=text, command=command, width=12).pack(side=tk.LEFT, padx=3)

    def create_contact(self):
        name = self.name_entry.get().strip()
        number = self.number_entry.get().strip()

        if not name or not number:
            messagebox.showwarning("Error", "Debe ingresar nombre y número.")
            return

        with open("friendsContact.txt", "a") as file:
            file.write(f"{name}!{number}\n")

        messagebox.showinfo("Éxito", "Contacto añadido correctamente.")
        self.clear_fields()

    def read_contact(self):
        name = self.name_entry.get().strip()

        if not os.path.exists("friendsContact.txt"):
            messagebox.showwarning("Error", "No hay contactos guardados.")
            return

        with open("friendsContact.txt", "r") as file:
            contacts = file.readlines()

        if not contacts:
            messagebox.showinfo("Información", "No hay contactos en la agenda.")
            return

        if not name:
            contact_list = "\n".join(contacts)
            messagebox.showinfo("Lista de Contactos", contact_list)
            return

        for line in contacts:
            contact_name, contact_number = line.strip().split("!")
            if contact_name == name:
                messagebox.showinfo("Contacto Encontrado", f"Nombre: {contact_name}\nNúmero: {contact_number}")
                return

        messagebox.showwarning("Error", "Este contacto no existe.")

    def update_contact(self):
        name = self.name_entry.get().strip()
        number = self.number_entry.get().strip()

        if not name or not number:
            messagebox.showwarning("Error", "Debe ingresar nombre y nuevo número.")
            return

        if not os.path.exists("friendsContact.txt"):
            messagebox.showwarning("Error", "No hay contactos guardados.")
            return

        updated = False
        lines = []
        with open("friendsContact.txt", "r") as file:
            for line in file:
                contact_name, contact_number = line.strip().split("!")
                if contact_name == name:
                    lines.append(f"{name}!{number}\n")
                    updated = True
                else:
                    lines.append(line)

        with open("friendsContact.txt", "w") as file:
            file.writelines(lines)

        if updated:
            messagebox.showinfo("Éxito", "Contacto actualizado correctamente.")
        else:
            messagebox.showwarning("Error", "Contacto no encontrado.")

        self.clear_fields()

    def delete_contact(self):
        name = self.name_entry.get().strip()

        if not name:
            messagebox.showwarning("Error", "Debe ingresar un nombre para eliminar.")
            return

        if not os.path.exists("friendsContact.txt"):
            messagebox.showwarning("Error", "No hay contactos guardados.")
            return

        deleted = False
        lines = []
        with open("friendsContact.txt", "r") as file:
            for line in file:
                contact_name, contact_number = line.strip().split("!")
                if contact_name == name:
                    deleted = True
                else:
                    lines.append(line)

        with open("friendsContact.txt", "w") as file:
            file.writelines(lines)

        if deleted:
            messagebox.showinfo("Éxito", "Contacto eliminado correctamente.")
        else:
            messagebox.showwarning("Error", "Contacto no encontrado.")

        self.clear_fields()

    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.number_entry.delete(0, tk.END)

class MainApp:
    @staticmethod
    def main():
        root = tk.Tk()
        app = FriendsContact(root)
        root.mainloop()

if __name__ == "__main__":
    MainApp.main()
