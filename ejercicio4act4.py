import tkinter as tk
from tkinter import messagebox, scrolledtext


class Programador:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class EquipoMaraton:
    def __init__(self, nombre_equipo, universidad, lenguaje, tamano):
        if tamano < 2 or tamano > 3:
            raise Exception("El equipo debe tener minimo 2 y maximo 3 programadores.")

        self.nombre_equipo = nombre_equipo
        self.universidad = universidad
        self.lenguaje = lenguaje
        self.tamano = tamano
        self.programadores = []

    def esta_completo(self):
        return len(self.programadores) == self.tamano

    def agregar_programador(self, nombre, apellido):
        if self.esta_completo():
            raise Exception("No se puede agregar mas programadores, el equipo esta lleno.")

        self.validar_texto(nombre, "nombre")
        self.validar_texto(apellido, "apellido")

        nuevo = Programador(nombre, apellido)
        self.programadores.append(nuevo)

    def validar_texto(self, texto, campo):
        if texto.strip() == "":
            raise Exception("El " + campo + " no puede estar vacio.")

        if len(texto) >= 20:
            raise Exception("El " + campo + " debe tener menos de 20 caracteres.")

        for letra in texto:
            if letra.isdigit():
                raise Exception("El " + campo + " no puede tener numeros.")


equipo = None


def crear_equipo():
    global equipo

    try:
        nombre_equipo = entrada_equipo.get().strip()
        universidad = entrada_universidad.get().strip()
        lenguaje = entrada_lenguaje.get().strip()
        tamano = int(entrada_tamano.get().strip())

        if nombre_equipo == "" or universidad == "" or lenguaje == "":
            raise Exception("Debe llenar los datos del equipo.")

        equipo = EquipoMaraton(nombre_equipo, universidad, lenguaje, tamano)
        mostrar_equipo()
        messagebox.showinfo("Correcto", "Equipo creado correctamente.")

    except ValueError:
        messagebox.showerror("Error", "El tamano debe ser un numero.")
    except Exception as error:
        messagebox.showerror("Error", str(error))


def agregar_programador():
    try:
        if equipo is None:
            raise Exception("Primero debe crear el equipo.")

        nombre = entrada_nombre.get().strip()
        apellido = entrada_apellido.get().strip()

        equipo.agregar_programador(nombre, apellido)

        entrada_nombre.delete(0, tk.END)
        entrada_apellido.delete(0, tk.END)

        mostrar_equipo()

    except Exception as error:
        messagebox.showerror("Error", str(error))


def mostrar_equipo():
    area_datos.delete("1.0", tk.END)

    if equipo is None:
        return

    area_datos.insert(tk.END, "Equipo: " + equipo.nombre_equipo + "\n")
    area_datos.insert(tk.END, "Universidad: " + equipo.universidad + "\n")
    area_datos.insert(tk.END, "Lenguaje: " + equipo.lenguaje + "\n")
    area_datos.insert(tk.END, "Tamano: " + str(equipo.tamano) + "\n\n")

    area_datos.insert(tk.END, "Programadores:\n")
    for i, programador in enumerate(equipo.programadores):
        linea = str(i + 1) + ". " + programador.nombre + " " + programador.apellido + "\n"
        area_datos.insert(tk.END, linea)

    area_datos.insert(tk.END, "\nEstado: ")
    if equipo.esta_completo():
        area_datos.insert(tk.END, "El equipo esta completo.")
    else:
        area_datos.insert(tk.END, "Faltan programadores.")


ventana = tk.Tk()
ventana.title("Ejercicio 4 - Equipo Maraton Programacion")
ventana.geometry("620x500")

frame = tk.Frame(ventana)
frame.pack(padx=12, pady=12, fill="x")

tk.Label(frame, text="Nombre del equipo:").grid(row=0, column=0, sticky="w", pady=4)
entrada_equipo = tk.Entry(frame, width=35)
entrada_equipo.grid(row=0, column=1, pady=4)

tk.Label(frame, text="Universidad:").grid(row=1, column=0, sticky="w", pady=4)
entrada_universidad = tk.Entry(frame, width=35)
entrada_universidad.grid(row=1, column=1, pady=4)

tk.Label(frame, text="Lenguaje:").grid(row=2, column=0, sticky="w", pady=4)
entrada_lenguaje = tk.Entry(frame, width=35)
entrada_lenguaje.grid(row=2, column=1, pady=4)

tk.Label(frame, text="Tamano del equipo (2 o 3):").grid(row=3, column=0, sticky="w", pady=4)
entrada_tamano = tk.Entry(frame, width=35)
entrada_tamano.grid(row=3, column=1, pady=4)

tk.Label(frame, text="Nombre programador:").grid(row=4, column=0, sticky="w", pady=4)
entrada_nombre = tk.Entry(frame, width=35)
entrada_nombre.grid(row=4, column=1, pady=4)

tk.Label(frame, text="Apellido programador:").grid(row=5, column=0, sticky="w", pady=4)
entrada_apellido = tk.Entry(frame, width=35)
entrada_apellido.grid(row=5, column=1, pady=4)

boton_crear = tk.Button(frame, text="Crear equipo", command=crear_equipo)
boton_crear.grid(row=6, column=0, pady=8)

boton_agregar = tk.Button(frame, text="Agregar programador", command=agregar_programador)
boton_agregar.grid(row=6, column=1, pady=8)

area_datos = scrolledtext.ScrolledText(ventana, width=70, height=13, font=("Consolas", 10))
area_datos.pack(padx=12, pady=8)

ventana.mainloop()
