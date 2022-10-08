import tkinter

class App:
    #CONSTANTES ASOCIADAS A LA BARRA
    __BARRA_VEL = 10
    __POS_BARRA_X = 10


    __pos_barra = 0

    def __init__(self):    
        self.root = tkinter.Tk()
        self.root.title("Ping Pong")
        self.root.geometry("750x500")
        self.root.update()
        self.__ANCHO_VENTANA = self.root.winfo_width()
        self.__ALTO_VENTANA = self.root.winfo_height()
        self.root.resizable(0, 0)
        self.configurar_escena()
        self.crear_barra()
        self.root.bind("<KeyPress-Down>", self.mover_barra)
        self.root.bind("<KeyPress-Up>", self.mover_barra)
        self.root.mainloop()
        


    def configurar_escena(self):
        self.escena = tkinter.Canvas(self.root, width=750, height=500, bg="black")
        self.escena.pack()
    
    def crear_barra(self):
        self.barra = self.escena.create_rectangle(self.__POS_BARRA_X, 0, 40, 100, fill="#33FF00")

    def mover_barra(self, event):
        self.__pos_barra += self.__BARRA_VEL if event.keysym == "Down" else -self.__BARRA_VEL
        self.__pos_barra = max(0, min(self.__ALTO_VENTANA - 100, self.__pos_barra))
        self.escena.coords(self.barra, self.__POS_BARRA_X, self.__pos_barra, 40, self.__pos_barra + 100)
        self.escena.update()

if __name__ == "__main__":
    app = App()