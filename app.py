import tkinter

class App:
    __POS_JUGADOR_X = 10
    __pos_jugador = 0

    def __init__(self):    
        self.root = tkinter.Tk()
        self.root.title("Ping Pong")
        self.root.geometry("750x500")
        #self.root.update()
        #self.__ANCHO_VENTANA = self.root.winfo_width()
        #self.__ALTO_VENTANA = self.root.winfo_height()
        self.root.resizable(0, 0)
        self.configurar_escena()
        self.crear_jugador()
        #self.root.bind("<KeyPress-Down>", self.mover_jugador)
        self.root.mainloop()
        


    def configurar_escena(self):
        self.escena = tkinter.Canvas(self.root, width=750, height=500, bg="black")
        self.escena.pack()
    
    def crear_jugador(self):
        print("HOLA")
        self.jugador = self.escena.create_rectangle(self.__POS_JUGADOR_X, 0, 40, 100, fill="#33FF00")

    """def mover_jugador(self, event):
        self.__pos_jugador += 1 if event.keysysm == "Down" else -1
        self.__pos_jugador = max(0, min(self.__ALTO_VENTANA, self.__pos_jugador))
        self.escena.move(self.jugador, 0, self.__pos_jugador)
        self.escena.update()"""

if __name__ == "__main__":
    app = App()