class Figura:
    def __init__(self, canvas, coordenadas, ancho, alto):
        self.posicion = {
            "x" : 0,
            "y" : 0,
            "x2" : 0,
            "y2" : 0
        }
        self.coordenadas = coordenadas
        self.ancho = ancho
        self.alto = alto
        self.set_posicion(self.coordenadas)
        self.canvas = canvas
    def set_posicion(self, coordenadas):
        for coordenada, valor in coordenadas.items():
            self.posicion[coordenada] = valor
        self.posicion["x2"] = self.posicion["x"] + self.ancho
        self.posicion["y2"] = self.posicion["y"] + self.alto
    def mover_posicion(self, coordenadas):
        for coordenada, valor in coordenadas.items():
            self.posicion[coordenada] += valor
        self.set_posicion(dict())
        
    def get_posicion(self):
        return self.posicion
    def dibujar(self):
        self.canvas.coords(
            self.id, 
            *self.get_posicion().values()
            )
        self.canvas.update()