import tkinter as tk
from tkinter import ttk, messagebox, filedialog


class LeerArchivo:
    @staticmethod
    def leer_archivo(ruta):
        with open(ruta, "r", encoding="utf-8") as archivo:
            return archivo.read()


class AplicacionLeerArchivo(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Ejercicio 5 - Leer Archivo")
        self.geometry("650x450")

        ttk.Button(self, text="Seleccionar archivo", command=self.seleccionar_archivo).pack(pady=10)

        self.resultado = tk.Text(self, height=22, width=75)
        self.resultado.pack(pady=10)

    def seleccionar_archivo(self):
        ruta = filedialog.askopenfilename(
            title="Seleccionar archivo de texto",
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
        )

        if ruta:
            try:
                contenido = LeerArchivo.leer_archivo(ruta)
                self.resultado.delete("1.0", tk.END)
                self.resultado.insert(tk.END, contenido)

            except OSError:
                messagebox.showerror("Error", "No se pudo leer el archivo.")


if __name__ == "__main__":
    app = AplicacionLeerArchivo()
    app.mainloop()