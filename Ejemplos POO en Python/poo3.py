#EN ESTE EJEMPLO SE APLICA ENCAPSULAMIENTO DE DATOS, EN LOS ATRIBUTOS DEL METODO CONSTRUCTOR
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
        if self.__Enmarcha:
            return print("El carro esta en marcha")
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


#instancias de la clase
carro1 = Carro()
carro2 = Carro()

carro1.Ruedas = 2
carro1.AnchoChasis = 100
carro1.LargodeChasis = 200

carro2.Ruedas = 4
carro2.AnchoChasis = 125
carro2.LargodeChasis = 250

print("-------AUTOMOVIL 1-------")
carro1.Arrancar(False)
carro1.Detener(False)
carro1.Estado()
print("-------AUTOMOVIL 2-------")
carro2.Arrancar(True)
carro2.Detener(False)
carro2.Estado()
        