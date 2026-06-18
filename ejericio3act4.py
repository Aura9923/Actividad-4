import math
import tkinter as tk
from tkinter import ttk, messagebox


class CalculosNumericos:
    @staticmethod
    def calcular_logaritmo_neperiano(valor):
        valor = float(valor)

        if valor <= 0:
            raise ArithmeticError("El valor debe ser un numero positivo para calcular el logaritmo.")

        return math.log(valor)

    @staticmethod
    def calcular_raiz_cuadrada(valor):
        valor = float(valor)

        if valor < 0:
            raise ArithmeticError("El valor debe ser un numero positivo para calcular la raiz cuadrada.")

        return math.sqrt(valor)


class AplicacionCalculos(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Ejercicio 3 - Calculos Numericos")
        self.geometry("500x320")

        ttk.Label(self, text="Valor numerico:").pack(pady=8)
        self.valor_entry = ttk.Entry(self, width=40)
        self.valor_entry.pack()

        ttk.Button(self, text="Calcular", command=self.realizar_calculos).pack(pady=12)

        self.resultado = tk.Text(self, height=7, width=55)
        self.resultado.pack(pady=10)

    def realizar_calculos(self):
        try:
            valor = self.valor_entry.get()
            logaritmo = CalculosNumericos.calcular_logaritmo_neperiano(valor)
            raiz = CalculosNumericos.calcular_raiz_cuadrada(valor)

            self.resultado.delete("1.0", tk.END)
            self.resultado.insert(
                tk.END,
                f"Logaritmo neperiano = {logaritmo}\n"
                f"Raiz cuadrada = {raiz}"
            )

        except ValueError:
            messagebox.showerror("Error", "El valor debe ser numerico.")

        except ArithmeticError as error:
            messagebox.showerror("Error", str(error))


if __name__ == "__main__":
    app = AplicacionCalculos()
    app.mainloop()
