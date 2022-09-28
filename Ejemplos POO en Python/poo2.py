class Carro():
    #propiedades de la clase, en este caso de tipo carro
    #estas propiedades seran general para todos los objetos de tipo carro
    color = "Rojo"
    LargodeChasis = 250
    AnchoChasis = 125
    Ruedas = 4
    Enmarcha = False

    #metodos de la clase, en este caso los metodos para arrancar y detener el carro
    #self es una referencia a la clase
    #self es como decirle a python que estamos hablando de la clase
    #self se utiliza para referirse a las propiedades de la clase
    #self se utiliza para referirse a los metodos de la clase
    #sin self no se puede acceder a las propiedades de la clase
    #sin sel seria solo una funcion ajenas a la clase
    def Arrancar(self, enciende):
        self.Enmarcha = enciende
        if self.Enmarcha:
            return print("El carro esta en marcha")
        else:
            return print("El carro esta detenido")


    #metodo para detener el carro
    def Detener(self, detener):
        self.Enmarcha = detener
        if self.Enmarcha:
            return print("El carro se ha detenido")
        else:
            return print("El carro esta en marcha")


    def Estado(self):
        print("El auto tiene ", self.Ruedas, " ruedas. Un ancho de ", self.AnchoChasis, " y un largo de ", self.LargodeChasis)


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


