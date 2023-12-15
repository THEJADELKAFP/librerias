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

class Label:
    def __init__(self, root,text: str,font: None, bg: str = 'white', fg: str = 'black') -> None:
        self.root = root
        self.text = text
        self.font = font
        self.bg = bg
        self.fg = fg

    def createLabel(self):
        self.variablee = tk.Label(self.root, text=self.text, font=self.font, bg=self.bg, fg=self.fg)
        self.variablee.pack()
