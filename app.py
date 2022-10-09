import tkinter

class Barra:
    __MARGEN_IZQ = 10
    __ANCHO = 30
    __ALTO = 100
    __VEL_BARRA = 10
    __pos_actual = 0
    
    def __init__(self, canvas, alto_ventana, color):
        self.__MAX_POS = alto_ventana - self.__ALTO
        self.canvas = canvas
        self.__pos_actual = (alto_ventana - self.__ALTO) * 0.5
        print(self.__pos_actual)
        self.id = canvas.create_rectangle(
            self.__MARGEN_IZQ, 
            self.__pos_actual, 
            self.__MARGEN_IZQ + self.__ANCHO, 
            self.__ALTO, 
            fill=color
            )
    def subir_barra(self):
        self.__pos_actual -= self.__VEL_BARRA

    def baja_barra(self):
        self.__pos_actual += self.__VEL_BARRA

    def corregir_posicion(self):
        self.__pos_actual = max(0, min(self.__MAX_POS, self.__pos_actual))
    
    def dibujar(self):
        self.canvas.coords(
            self.id, 
            self.__MARGEN_IZQ, 
            self.__pos_actual, 
            self.__MARGEN_IZQ + self.__ANCHO, 
            self.__pos_actual + self.__ALTO
            )
        self.canvas.update()

    def mover(self, event):
        if event.keysym == "Up":
            self.subir_barra()
        else:
            self.baja_barra()
        self.corregir_posicion()
        self.dibujar()

class Pelota:
    __POS_X_INICIAL = 100
    __POS_Y_INICIAL = 100
    __RADIO = 25
    __DIAMETRO = __RADIO * 2
    __velx = 6
    __vely = -6

    def __init__(self, canvas, color):
        self.__lado_izq_x = self.__POS_X_INICIAL
        self.__lado_izq_y = self.__POS_Y_INICIAL
        self.__lado_der_x = self.__lado_izq_x + self.__DIAMETRO
        self.__lado_der_y = self.__lado_izq_y + self.__DIAMETRO
        self.canvas = canvas
        self.id = canvas.create_oval(
            self.__lado_izq_x, 
            self.__lado_izq_y, 
            self.__lado_der_x, 
            self.__lado_der_y, 
            fill=color
            )
    def mover(self):
        self.__lado_izq_x += self.__velx
        self.__lado_izq_y += self.__vely
        self.__lado_der_x += self.__velx
        self.__lado_der_y += self.__vely
        self.canvas.coords(
            self.id, 
            self.__lado_izq_x, 
            self.__lado_izq_y, 
            self.__lado_der_x, 
            self.__lado_der_y
            )
    def reflejar_x(self, n: int):
        self.__velx *= -1
        self.__lado_izq_x += n
        self.__lado_der_x += n
    def reflejar_y(self, n: int):
        self.__vely *= -1
        self.__lado_izq_y += n
        self.__lado_der_y += n
    def radio(self):
        return self.__RADIO
    def diametro(self):
        return self.__DIAMETRO
    def lado_der_x(self):
        return self.__lado_der_x

class App:

    def __init__(self):    
        self.root = tkinter.Tk()
        self.root.title("Ping Pong")
        self.root.geometry("750x500")
        self.root.update()
        self.__ANCHO_VENTANA = self.root.winfo_width()
        self.__ALTO_VENTANA = self.root.winfo_height()
        self.root.resizable(0, 0)
        self.configurar_escena()
        self.barra = Barra(self.escena, self.__ALTO_VENTANA, "#33FF00")
        self.barra.dibujar()
        self.pelota = Pelota(self.escena, "white")
        self.root.bind("<KeyPress-Down>", self.barra.mover)
        self.root.bind("<KeyPress-Up>", self.barra.mover)
        self.root.mainloop()
                    
    def configurar_escena(self):
        self.escena = tkinter.Canvas(self.root, width=750, height=500, bg="black")
        self.escena.pack()

    def choca_con_pared(self):
        return self.pelota.lado_der_x() > self.__ANCHO_VENTANA
    
if __name__ == "__main__":
    app = App()