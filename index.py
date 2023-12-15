import windjdk as jdk

def pepe(): # funcion que imprime PEPE
    print("PEPE")

root = jdk.Ventana("400x400", "JADELKA", False) # Crear la instancia de la ventana

boton = jdk.Boton(root.root, "BOTON XD", pepe )  # Accede a la ventana con root.root
boton.CreateBoton()  # Llama a CreateBoton para mostrar el botón

label = jdk.Label(root.root, text="jadelka", font="arial", fg="black") # Accede a la Label con root.root
label.createLabel()  # Llama a CreateLbael para mostrar el Label

root.root.mainloop()