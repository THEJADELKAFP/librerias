import windjdk as jdk

def pepe():
    print("pepe")

# Crear la instancia de la ventana
root = jdk.Ventana("400x400", "JADELKA", False)

# Crear la instancia del botón en la ventana
boton = jdk.Boton(root.root, "BOTON XD", pepe )  # Accede a la ventana con root.root
boton.CreateBoton()  # Llama a CreateBoton para mostrar el botón

label = jdk.Label(root.root, text="jadelka", font="arial", fg="black") # Accede a la Label con root.root
label.createLabel()  # Llama a CreateLbael para mostrar el Label

label = jdk.Label(root.root, text="jadelka", font="arial", fg="black")
label.createLabel()

# Iniciar el bucle principal de tkinter
root.root.mainloop()