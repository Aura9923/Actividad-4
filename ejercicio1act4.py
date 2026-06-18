import tkinter as tk
from tkinter import scrolledtext


def ejecutar_ejercicio():
    resultado.delete("1.0", tk.END)

    def escribir(texto):
        resultado.insert(tk.END, texto + "\n")

    # Primer bloque try
    try:
        escribir("Ingresando al primer try")
        cociente = 10000 / 0
        escribir("Despues de la division")
    except ZeroDivisionError:
        escribir("Division por cero")
    finally:
        escribir("Ingresando al primer finally")

    # Segundo bloque try
    try:
        escribir("Ingresando al segundo try")
        objeto = None
        objeto.toString()
        escribir("Imprimiendo objeto")
    except ZeroDivisionError:
        escribir("Division por cero")
    except Exception:
        escribir("Ocurrio una excepcion")
    finally:
        escribir("Ingresando al segundo finally")


ventana = tk.Tk()
ventana.title("Ejercicio 1 - Excepciones")
ventana.geometry("520x340")

titulo = tk.Label(
    ventana,
    text="Resultado del programa con try, except y finally",
    font=("Arial", 13, "bold")
)
titulo.pack(pady=10)

resultado = scrolledtext.ScrolledText(ventana, width=58, height=13, font=("Consolas", 11))
resultado.pack(padx=10, pady=5)

boton = tk.Button(ventana, text="Ejecutar ejercicio", command=ejecutar_ejercicio)
boton.pack(pady=10)

ventana.mainloop()
