from Figura import Figura
class Barra(Figura):
    __LADO_IZQ_X = 10
    __ANCHO = 30
    __ALTO = 100
    __VEL_BARRA = 10
    
    def __init__(self, canvas, color):
        self.__MAX_POS = canvas.winfo_height() - self.__ALTO
        super().__init__(
            canvas, 
            {
              "x" : self.__LADO_IZQ_X, 
              "y" : self.__MAX_POS * 0.5
              }, 
            self.__ANCHO, 
            self.__ALTO)
        self.id = self.canvas.create_rectangle(
            *self.get_posicion().values(), 
            fill=color
            )
    def corregir_posicion(self):
        self.set_posicion({"y" : max(0, min(self.__MAX_POS, self.get_posicion()["y"]))})
    def mover(self, event):
        self.mover_posicion({"y" : self.__VEL_BARRA * (-1 if event.keysym == "Up" else 1)})
        self.corregir_posicion()
        self.dibujar()
    def mitad(self):
      return self.posicion["x2"] - (self.__ANCHO * 0.5)