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
        #self.dibujar()

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
class Pelota(Figura):
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
        Figura.__init__(
            self,
            canvas,
            self.__lado_izq_x,
            self.__lado_izq_y,
            self.__lado_der_x,
            self.__lado_der_y,)
        self.id = canvas.create_oval(
            *self.get_posicion(), 
            fill=color
            )
    def mover(self):
        #print(self.get_posicion())
        self.rebota()
        self.actual = self.get_posicion()
        self.x = self.actual[0] + self.velocidad()["x"]
        self.y = self.actual[1] + self.velocidad()["y"]
        self.set_posicion(
            self.x,
            self.y,
            self.x + self.__DIAMETRO,
            self.y + self.__DIAMETRO
        )
        self.dibujar()
        #self.canvas.after(10, self.mover)
    def reflejar_x(self, n: int):
        self.__velx *= -1
        self.actual = self.get_posicion()
        self.x = self.actual[0] + n
        self.set_posicion(
            self.x,
            self.actual[1],
            self.x + self.__DIAMETRO,
            self.actual[3]
        )
    def reflejar_y(self, n: int):
        self.__vely *= -1
        self.actual = self.get_posicion()
        self.y = self.actual[1] + n
        self.set_posicion(
            self.actual[0],
            self.actual[1] + n,
            self.actual[2],
            self.y + self.__DIAMETRO
        )
    def velocidad(self):
        return {
            "x": self.__velx, 
            "y": self.__vely
            }
    def choca_con_pared(self):
        return self.get_posicion()[2] > self.canvas.winfo_width()
    def choca_con_techo(self):
        return self.get_posicion()[1] < 0
    def choca_con_piso(self):
        return self.get_posicion()[3] > self.canvas.winfo_height()
    def rebota(self):
        self.rebota_en_y()
        self.rebota_en_x()
    def rebota_en_y(self):
        if self.choca_con_techo():
            #print("CHOCÓ CON TECHO")
            self.reflejar_y(-self.get_posicion()[1])
        if self.choca_con_piso():
            #print("CHOCÓ CON PISO")
            self.reflejar_y(self.canvas.winfo_height() - self.get_posicion()[3])
    def rebota_en_x(self):
        if self.choca_con_pared():
            #print("CHOCÓ CON PARED")
            self.reflejar_x(self.canvas.winfo_width() - self.get_posicion()[2])
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

class App:

    def __init__(self):
        self.id = None
        self.root = tkinter.Tk()
        self.root.title("Ping Pong")
        self.root.geometry("750x500")
        self.root.update()
        self.root.resizable(0, 0)
        self.configurar_escena()
        self.escena.update()
        self.barra = Barra(self.escena, "#33FF00")
        self.pelota = Pelota(self.escena, "#33FF00")
        self.root.bind("<KeyPress-Down>", self.barra.mover)
        self.root.bind("<KeyPress-Up>", self.barra.mover)
        self.iniciar()
        self.root.mainloop()
                    
    def configurar_escena(self):
        self.escena = tkinter.Canvas(self.root, width=750, height=500, bg="black")
        self.escena.pack()
        self.puntaje = Puntaje(self.root, "#33FF00")
    def pelota_choca_con_barra(self):
        pelota, barra = self.pelota.get_posicion(), self.barra.get_posicion()
        return all(
            ((barra[1] < pelota[1] and barra[3] > pelota[1]) or (barra[1] < pelota[3] and barra[3] > pelota[3]),
            0 < barra[2] - pelota[0] <= abs(self.pelota.velocidad()["x"]))
        )
    
    def fuera_de_escena(self):
        return (self.pelota.get_posicion()[0] < self.barra.get_posicion()[2]) and not self.pelota_choca_con_barra()

    def juego(self):
        self.pelota.mover()
        if self.pelota_choca_con_barra():
            self.puntaje.sumar_punto()
            self.pelota.reflejar_x(self.barra.get_posicion()[2] - self.pelota.get_posicion()[0])
        self.id = self.escena.after(10, self.juego)
        if self.fuera_de_escena():
            self.perdiste()
    def iniciar(self):
        self.juego()
    def perdiste(self):
        self.escena.after_cancel(self.id)
if __name__ == "__main__":
    app = App()