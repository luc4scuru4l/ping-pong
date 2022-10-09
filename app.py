import tkinter

class Pelota:
    __POS_X_INICIAL = 100
    __POS_Y_INICIAL = 100
    __RADIO = 50
    __velx = 6
    __vely = -6

    def __init__(self, canvas, color):
        self.__pos_x = self.__POS_X_INICIAL
        self.__pos_y = self.__POS_Y_INICIAL
        self.canvas = canvas
        self.id = canvas.create_oval(
            self.__POS_X_INICIAL, 
            self.__POS_Y_INICIAL, 
            self.__POS_X_INICIAL + self.__RADIO, 
            self.__POS_Y_INICIAL + self.__RADIO, 
            fill=color
            )
    def mover(self):
        self.__pos_x += self.__velx
        self.__pos_y += self.__vely
        self.canvas.coords(self.id, self.__pos_x, self.__pos_y, self.__pos_x + (self.__RADIO * 2), self.__pos_y + (self.__RADIO * 2))
    def reflejar_x(self, n: int):
        self.__pos_x += n
        self.__velx *= -1
    def reflejar_y(self, n: int):
        self.__pos_y += n
        self.__vely *= -1





class App:
    #VARIABLES Y CONSTANTES ASOCIADAS A LA BARRA
    __VEL_BARRA = 10
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
        self.pelota = Pelota(self.escena, "white")
        self.root.bind("<KeyPress-Down>", self.mover_barra)
        self.root.bind("<KeyPress-Up>", self.mover_barra)
        self.root.mainloop()
        


    def configurar_escena(self):
        self.escena = tkinter.Canvas(self.root, width=750, height=500, bg="black")
        self.escena.pack()
    
    def crear_barra(self):
        self.barra = self.escena.create_rectangle(self.__POS_BARRA_X, 0, 40, 100, fill="#33FF00")

    def mover_barra(self, event):
        self.__pos_barra += self.__VEL_BARRA if event.keysym == "Down" else -self.__VEL_BARRA
        self.__pos_barra = max(0, min(self.__ALTO_VENTANA - 100, self.__pos_barra))
        self.escena.coords(self.barra, self.__POS_BARRA_X, self.__pos_barra, 40, self.__pos_barra + 100)
        self.escena.update()
    
    def rebote_en_x(self):
        pass
    
if __name__ == "__main__":
    app = App()