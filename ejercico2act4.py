import tkinter as tk
from tkinter import ttk, messagebox


class Vendedor:
    def __init__(self, nombre, apellidos, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = self.verificar_edad(edad)

    def verificar_edad(self, edad):
        edad = int(edad)

        if edad < 0 or edad > 120:
            raise ValueError("La edad no puede ser negativa ni mayor a 120.")

        if edad < 18:
            raise ValueError("El vendedor debe ser mayor de 18 anos.")

        return edad

    def imprimir(self):
        return (
            f"Nombre del vendedor = {self.nombre}\n"
            f"Apellidos del vendedor = {self.apellidos}\n"
            f"Edad del vendedor = {self.edad}"
        )


class AplicacionVendedor(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Ejercicio 2 - Vendedor")
        self.geometry("500x360")

        ttk.Label(self, text="Nombre:").pack(pady=5)
        self.nombre_entry = ttk.Entry(self, width=40)
        self.nombre_entry.pack()

        ttk.Label(self, text="Apellidos:").pack(pady=5)
        self.apellidos_entry = ttk.Entry(self, width=40)
        self.apellidos_entry.pack()

        ttk.Label(self, text="Edad:").pack(pady=5)
        self.edad_entry = ttk.Entry(self, width=40)
        self.edad_entry.pack()

        ttk.Button(self, text="Crear vendedor", command=self.crear_vendedor).pack(pady=12)

        self.resultado = tk.Text(self, height=8, width=55)
        self.resultado.pack(pady=10)

    def crear_vendedor(self):
        try:
            vendedor = Vendedor(
                self.nombre_entry.get(),
                self.apellidos_entry.get(),
                self.edad_entry.get()
            )

            self.resultado.delete("1.0", tk.END)
            self.resultado.insert(tk.END, vendedor.imprimir())

        except ValueError as error:
            messagebox.showerror("Error", str(error))


if __name__ == "__main__":
    app = AplicacionVendedor()
    app.mainloop()