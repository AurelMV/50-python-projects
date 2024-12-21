import tkinter

# Crear la ventana principal
ventana = tkinter.Tk()
ventana.title("Calculadora Básica")

# Crear la pantalla de la calculadora
pantalla = tkinter.Entry(ventana, font=("Arial", 20))
pantalla.grid(row=0, column=0, columnspan=4)

# Lista de botones
botones = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '.', '0', '=', '+'
]

# Crear los botones
fila = 1
columna = 0
for i in botones:
    boton = tkinter.Button(ventana, text=i, width=5, height=3)
    boton.grid(row=fila, column=columna)
    columna += 1
    if columna > 3:
        columna = 0
        fila += 1

# Ejecutar la ventana
ventana.mainloop()
