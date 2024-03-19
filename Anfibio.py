from zooAnimales.animal import Animal

class Anfibio(Animal):
    _listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio._listado.append(self)

    @staticmethod
    def cantidadAnfibios():
        return len(Anfibio._listado)

    @staticmethod
    def movimiento():
        return "saltar"

    @classmethod
    def crearRana(cls, nombre, edad, genero):
        cls.ranas += 1
        return cls(nombre, edad, "selva", genero, "rojo", True)

    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        cls.salamandras += 1
        return cls(nombre, edad, "selva", genero, "negro y amarillo", False)

    # Getters
    def getColorPiel(self):
        return self._colorPiel

    def isVenenoso(self):
        return self._venenoso

    # Setters
    def setColorPiel(self, colorPiel):
        self._colorPiel = colorPiel

    def setVenenoso(self, venenoso):
        self._venenoso = venenoso