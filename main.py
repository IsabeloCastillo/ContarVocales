import tkinter as tk
from tkinter import ttk, PhotoImage
from PIL import Image, ImageTk

def escribir_texto(mensaje, index=0):
    if index < len(mensaje):
        etiqueta_resultado.config(text=etiqueta_resultado.cget("text") + mensaje[index])
        ventana.after(40, escribir_texto, mensaje, index+1)

def contar_vocales():
    try:
        cadena = entrada_texto.get()

        if not cadena:
            etiqueta_resultado.config(text="")
            escribir_texto("La cadena no puede estar vacía.")
            return

        cadena = cadena.lower()
        vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

        for char in cadena:
            if char in vocales:
                vocales[char] += 1

        mensaje = "Conteo de vocales:\n\n"
        for vocal, veces in vocales.items():
            if veces > 0:
                plural = "veces" if veces != 1 else "vez"
                mensaje += f"La vocal '{vocal}' aparece {veces} {plural}.\n"
            else:
                mensaje += f"La vocal '{vocal}' no aparece.\n"

        etiqueta_resultado.config(text="")
        escribir_texto(mensaje)

    except Exception as e:
        etiqueta_resultado.config(text="")
        escribir_texto(f"Ha ocurrido un error: {e}")


# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Contador de Vocales Futurista")
ventana.geometry("1920x1080")

# Añadir imagen de fondo
imagen_original = Image.open("fondo_futurista.jpg")
imagen_resized = imagen_original.resize((1920, 1080))
fondo = ImageTk.PhotoImage(imagen_resized)
etiqueta_fondo = tk.Label(ventana, image=fondo)
etiqueta_fondo.place(relwidth=1, relheight=1)

# Estilo de los widgets
estilo = ttk.Style()
estilo.configure("TButton", font=("Courier", 14))
estilo.configure("TLabel", font=("Courier", 12, 'bold'))

# Widgets
etiqueta = ttk.Label(ventana, text="Ingresa una cadena de texto:")
entrada_texto = ttk.Entry(ventana, font=("Courier", 12))
boton = ttk.Button(ventana, text="Contar", command=contar_vocales)
etiqueta_resultado = tk.Label(ventana, text="", font=("Courier", 14, 'bold'), fg="red", bg="black")


# Ubicación de los widgets
etiqueta.pack(pady=40)
entrada_texto.pack(pady=5)
boton.pack(pady=10)
etiqueta_resultado.pack(pady=5)

# Enfocar el Entry
entrada_texto.focus_set()

ventana.mainloop()
