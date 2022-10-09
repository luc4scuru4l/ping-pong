import tkinter

class Figura:
    def __init__(self, canvas, x1, y1, x2, y2):
        self.set_posicion(x1, y1, x2, y2)
        self.canvas = canvas
    def set_posicion(self, x1, y1, x2, y2):
        (self.__lado_izq_x, 
        self.__lado_izq_y, 
        self.__lado_der_x, 
        self.__lado_der_y
        ) = (x1, y1, x2, y2)
    def get_posicion(self):
        return (self.__lado_izq_x, 
                self.__lado_izq_y, 
                self.__lado_der_x, 
                self.__lado_der_y)
    def dibujar(self):
        self.canvas.coords(
            self.id, 
            *self.get_posicion()
            )
        self.canvas.update()
class Barra(Figura):
    __LADO_IZQ_X = 10
    __ANCHO = 30
    __ALTO = 100
    __VEL_BARRA = 10
    
    def __init__(self, canvas, color):
        self.__MAX_POS = canvas.winfo_height() - self.__ALTO
        self.__lado_izq_y = self.__MAX_POS * 0.5
        self.__lado_der_x = self.__LADO_IZQ_X + self.__ANCHO
        self.__lado_der_y = self.__lado_izq_y + self.__ALTO
        Figura.__init__(
            self,
            canvas, 
            self.__LADO_IZQ_X, 
            self.__lado_izq_y, 
            self.__lado_der_x, 
            self.__lado_der_y,
            )
        self.id = self.canvas.create_rectangle(
            *self.get_posicion(), 
            fill=color
            )

    def corregir_posicion(self, y):
        return max(0, min(self.__MAX_POS, y))
    
    def mover(self, event):
        if event.keysym == "Up":
            self.operacion = lambda x, y: x - y
        else:
            self.operacion = lambda x, y: x + y
        self.actual = self.get_posicion()
        self.y = self.corregir_posicion(self.operacion(self.actual[1], self.__VEL_BARRA))
        self.set_posicion(
            self.actual[0],
            self.y,
            self.actual[2],
            self.y + self.__ALTO
        )
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
        #print(self.canvas.winfo_width())
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
        self.rebote()
        self.canvas.coords(
            self.id, 
            self.__lado_izq_x, 
            self.__lado_izq_y, 
            self.__lado_der_x, 
            self.__lado_der_y
            )
        self.canvas.after(10, self.mover)
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
    def choca_con_pared(self):
        return self.__lado_der_x > self.canvas.winfo_width()
    def rebote(self):
        if self.choca_con_pared():
            self.reflejar_x(self.canvas.winfo_width() - self.__lado_der_x)
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
        self.root.resizable(0, 0)
        self.configurar_escena()
        self.escena.update()
        self.barra = Barra(self.escena, "#33FF00")
        self.barra.dibujar()
        self.pelota = Pelota(self.escena, "white")
        self.pelota.mover()
        self.root.bind("<KeyPress-Down>", self.barra.mover)
        self.root.bind("<KeyPress-Up>", self.barra.mover)
        self.root.mainloop()
                    
    def configurar_escena(self):
        self.escena = tkinter.Canvas(self.root, width=750, height=500, bg="black")
        self.escena.pack()

    
if __name__ == "__main__":
    app = App()