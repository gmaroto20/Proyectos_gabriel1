a=1
class coche():
    def __init__(self):
        self.largo = 3900
        self.ancho = 1500
        self.__ruedas = 4
        self.enmarcha = False

    def arrancar(self, arrancamos):
        self.enmarcha = arrancamos
        if (self.enmarcha):
            chequeado = self.__chequeo()
        if (self.enmarcha and chequeado):
            return "Arrancado"
        elif (self.enmarcha and chequeado == False):
            return ("No arrancar, el coche tiene que revisarse")
        else:
            return "Parado"

    def estado(self):
        print("largo:", self.largo, "\nancho:", self.ancho, "\nruedas:", self.__ruedas)

    def __chequeo(self):
        print("se va a proceder a chequear el coche ")
        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"
        if (self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):
            return True
        else:
            return False




