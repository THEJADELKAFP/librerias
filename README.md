# WINDJDK
¿Que para que sirve?
+ para poder ser mas eficiente en la programacion haciendo lo mismo pero con menos lineas de codigo



## Codigo de muestra
+ Asi es como se crea una ventana con la libreria windjdk

```python
import windjdk as jdk

# Crear la instancia de la ventana
root = jdk.Ventana("400x300", "jadelka", True)

# Iniciar el bucle principal de tkinter
root.root.mainloop()
```

+ para poner un boton es:
  
```python
#Crear la instancia del botón en la ventana
boton = jdk.Boton(root.root, "BOTON XD", pepe)  # Accede a la ventana con root.root
boton.CreateBoton()  # Llama a CreateBoton para mostrar el botón
```

## Libreria necesarias

```
pip install tkinter
```
## Metas y cosas hechas

- [X] crear ventana facil
- [X] crear botones facil
- [x] crear label facil
- [ ] unir base de datos facil
- [ ] crear graficas facil

## Leer importante

> [!NOTE]
> esto es para facilitar mi creacion de aplicaciones de Desktop.

> [!TIP]
> opcional visita mi pagina web para mayor informacion sobre como funciona este libreria.
> Esta es mi pagina web [JADELKA](jadelka).

> [!WARNING]
> Necesitas tenes tkinter instalado globalmente en tu pc.

### ANTES Y DESPUES DE WINDJDK

* Antes 

```python
import tkinter as tk

def on_button_click():
    label.config(text="¡Hola, Tkinter!")

# Crear la instancia de la ventana
ventana = tk.Tk()
ventana.title("Jadelka")
ventana.geometry("400x400")
ventana.resizable(False, False)  # Hace que la ventana no sea redimensionable

# Crear la etiqueta
label = tk.Label(ventana, text="Hola Mundo!")
label.pack(pady=10)  # Añade un espacio alrededor de la etiqueta

# Crear el botón
boton = tk.Button(ventana, text="Haz clic", command=on_button_click)
boton.pack(pady=10)  # Añade un espacio alrededor del botón

# Iniciar el bucle principal de Tkinter
ventana.mainloop()

```

### DESPUES

```python
import windjdk as jdk

def pepe():
    print("pepe")

# Crear la instancia de la ventana
root = jdk.Ventana("400x400", "JADELKA", False)

# Crear la instancia del botón en la ventana
boton = jdk.Boton(root.root, "BOTON XD", pepe )  # Accede a la ventana con root.root
boton.CreateBoton()  # Llama a CreateBoton para mostrar el botón

label = jdk.Label(root.root, text="jadelka", font="arial", fg="black")
label.createLabel()

# Iniciar el bucle principal de tkinter
root.root.mainloop()
```

> proximamente

