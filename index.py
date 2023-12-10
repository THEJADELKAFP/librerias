import windjdk as jdk

def pepe():
    print("pee")

# Crear la instancia de la ventana
root = jdk.Ventana("400x300", "jadelka", True)

# Crear la instancia del botón en la ventana
boton = jdk.Boton(root.root, "BOTON XD", pepe)  # Accede a la ventana con root.root
boton.CreateBoton()  # Llama a CreateBoton para mostrar el botón

# Iniciar el bucle principal de tkinter
root.root.mainloop()