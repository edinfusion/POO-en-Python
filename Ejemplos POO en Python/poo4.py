#EN ESTE EJEMPLO SE APLICA ENCAPSULAMIENTO DE METODOS O FUNCIONES
class Carro():
    #propiedades de la clase, en este caso de tipo carro
    #estas propiedades seran general para todos los objetos de tipo carro
    #a este metodo se le llama constructor
    def __init__(self):
        self.color = "Rojo"
        self.LargodeChasis = 250
        self.AnchoChasis = 125
        #se aplica encapsulamiento de datos
        #a las propiedades de la clase se les antepone __
        #de esta manera se evita que se modifiquen las propiedades de la clase
        #en este caso un auto no puede tener dos ruedas
        self.__Ruedas = 4
        self.__Enmarcha = False

    def Arrancar(self, enciende):
        self.__Enmarcha = enciende
        if self.__Enmarcha and self.__ChequeoInterno():
            return print("El carro esta en marcha")
        elif self.__Enmarcha and self.__ChequeoInterno() == False:
            return print("Algo ha ido mal en el chequeo. No podemos arrancar")
        else:
            return print("El carro esta detenido")

    #metodo para detener el carro
    def Detener(self, detener):
        self.__Enmarcha = detener
        if self.__Enmarcha:
            return print("El carro se ha detenido")
        else:
            return print("El carro esta en marcha")

    def Estado(self):
        print("El auto tiene ", self.__Ruedas, " ruedas. Un ancho de ", self.AnchoChasis, " y un largo de ", self.LargodeChasis)

    #metodo para encapsular el metodo de chequeo
    def __ChequeoInterno(self):
        print("Realizando chequeo interno")
        self.gasolina = False
        self.aceite = True
        self.puertas = True

        if self.gasolina and self.aceite and self.puertas:
            return True
        else:
            return False
        #self.__Chequeo()


carron = Carro()
carron.Arrancar(True)

carron.Estado()
