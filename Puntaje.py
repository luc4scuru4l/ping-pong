import tkinter
class Puntaje:
    def __init__(self, ventana, color):
        self.puntos = tkinter.StringVar()
        self.puntos.set("0")
        self.label = tkinter.Label(ventana, fg=color, bg="black", font=("Retro Computer", 20), width=2, height=1)
        self.label.config(textvariable=self.puntos)
        ancho_ventana = ventana.winfo_width()
        self.label.place(x=ancho_ventana-60, y=10)
    def sumar_punto(self):
        self.puntos.set(str(int(self.puntos.get()) + 1))
