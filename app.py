import tkinter
from tkinter import messagebox
from Barra import Barra
from Pelota import Pelota
from Puntaje import Puntaje
class App:

    def __init__(self):
        self.id = None
        self.configurar_ventana()
        self.configurar_escena()
        self.configurar_controles()
        self.iniciar()
        self.root.mainloop()

    def configurar_controles(self):
        self.root.bind("<KeyPress-Down>", self.barra.mover)
        self.root.bind("<KeyPress-Up>", self.barra.mover)
        
    def configurar_ventana(self):
        self.root = tkinter.Tk()
        self.root.title("Ping Pong")
        self.root.geometry("750x500")
        self.root.update()
        self.root.resizable(0, 0)
    def configurar_escena(self):
        self.escena = tkinter.Canvas(self.root, width=750, height=500, bg="black")
        self.escena.pack()
        self.escena.update()
        self.puntaje = Puntaje(self.root, "#33FF00")
        self.barra = Barra(self.escena, "#33FF00")
        self.pelota = Pelota(self.escena, "#33FF00")
    def pelota_choca_con_barra(self):
        pelota, barra = self.pelota.get_posicion(), self.barra.get_posicion()
        return all(
            (
                (barra["y2"] > pelota["y"] > barra["y"]) or 
                (barra["y"] < pelota["y2"] < barra["y2"]),
                -3 <= barra["x2"] - pelota["x"] <= abs(self.pelota.velocidad()["x"])
                )
        )
    def choca_con_barra_inferior(self):
        cercania = (self.pelota.get_posicion()["y"] - self.barra.get_posicion()["y2"])
        if self.barra.mitad() >= self.pelota.get_posicion()["x"] and 10 > cercania >= 0:
            self.pelota.reflejar("y", 6)
    def choca_con_barra_superior(self):
        cercania = (self.barra.get_posicion()["y"] - self.pelota.get_posicion()["y2"])
        if self.barra.mitad() >= self.pelota.get_posicion()["x"] and 10 > cercania >= 0:
            self.pelota.reflejar("y", -6)
            
    
    def fuera_de_escena(self):
        return self.pelota.get_posicion()["x2"] < 0

    def juego(self):
        self.pelota.mover()
        self.choca_con_barra_inferior()
        self.choca_con_barra_superior()
        if self.pelota_choca_con_barra():
            self.puntaje.sumar_punto()
            self.pelota.reflejar("x", self.barra.get_posicion()["x2"] - self.pelota.get_posicion()["x"])
        self.id = self.escena.after(10, self.juego)
        if self.fuera_de_escena():
            self.perdiste()
    def iniciar(self):
        self.juego()
    def perdiste(self):
        self.escena.after_cancel(self.id)
        messagebox.showinfo(message="Perdiste!", title="Game Over")
        self.escena.delete("all")
if __name__ == "__main__":
    app = App()