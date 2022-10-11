import random
from Figura import Figura
class Pelota(Figura):
    __RADIO = 25
    __DIAMETRO = __RADIO * 2
    __POS_X_INICIAL = 100

    def __init__(self, canvas, color):
        self.__velocidad = {
          "x" : 6,
          "y" : 6 * random.choice([1, -1])
        }
        super().__init__(
            canvas,
            {
              "x" : self.__POS_X_INICIAL,
              "y" : random.randint(self.__DIAMETRO, canvas.winfo_height() - self.__DIAMETRO)
            },
            self.__DIAMETRO,
            self.__DIAMETRO
            )
        self.id = canvas.create_oval(
            *self.get_posicion().values(), 
            fill=color
            )
        print(self.get_posicion()["y"])
    def mover(self):
        self.rebota()
        self.mover_posicion({ "x" : self.__velocidad["x"], "y" : self.__velocidad["y"]})
        self.dibujar()
    def velocidad(self):
      return self.__velocidad
    def reflejar(self, eje, n):
      self.__velocidad[eje] *= -1
      self.mover_posicion({eje : n})
    def choca_con_pared(self):
        return self.get_posicion()["x2"] > self.canvas.winfo_width()
    def choca_con_techo(self):
        return self.get_posicion()["y"] < 0
    def choca_con_piso(self):
        return self.get_posicion()["y2"] > self.canvas.winfo_height()
    def rebota(self):
        self.rebota_en_y()
        self.rebota_en_x()
    def rebota_en_y(self):
        if self.choca_con_techo():
            self.reflejar("y", -self.get_posicion()["y"])
        if self.choca_con_piso():
            self.reflejar("y", self.canvas.winfo_height() - self.get_posicion()["y2"])
    def rebota_en_x(self):
        if self.choca_con_pared():
            self.reflejar("x", self.canvas.winfo_width() - self.get_posicion()["x2"])