#para crear una clase se usa la palabra reservada class
#ejemplo basico de una clase sin constructor
#esta clase tiene 4 propiedades y 3 metodos
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
    def Arrancar(self):
        print("El carro ha sido encendido")
        self.Enmarcha = True

    #metodo para detener el carro
    def Detener(self):
        print("El carro ha sido detenido")
        self.Enmarcha = False
    
    #metodo para saber si el carro esta en marcha o no
    def Estado(self):
        if self.Enmarcha:
            print("El carro esta en marcha")
        else:
            print("El carro esta detenido")



#instanciar la clase, crear un objeto de tipo carro
#se crea un objeto de tipo carro
carronuevoi = Carro() #se crea un objeto de tipo carro
#se accede a las propiedades de la clase, a través del objeto con el punto
carronuevoi.Arrancar() #se llama al metodo Arrancar del objeto carronuevoi
carronuevoi.Estado() #se llama al metodo Estado del objeto carronuevoi
carronuevoi.Detener() #se llama al metodo Detener del objeto carronuevoi
carronuevoi.Estado() #se llama al metodo Estado del objeto carronuevoi
print("Largo del automovil: ",carronuevoi.LargodeChasis) #se accede a la propiedad LargodeChasis del objeto carronuevoi