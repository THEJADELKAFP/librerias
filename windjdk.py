import tkinter as tk

class Ventana:
    def __init__(self, geometry: str, title: str, resizable: bool) -> None:
        self.root = tk.Tk()
        self.root.geometry(geometry)
        self.root.title(title)
        self.root.resizable(resizable, resizable)

class Boton:
    def __init__(self, root, text, command):
        self.root = root
        self.text = text
        self.command = command

    def CreateBoton(self):
        self.variable = tk.Button(self.root, text=self.text, command=self.command)
        self.variable.pack(pady=10)
