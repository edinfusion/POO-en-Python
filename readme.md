# POO (PROGRAMACION ORIENTADA A OBJETOS)
Existen muchos paradigmas para programar, pero los mas comunes y mas usados han sido los orientados a procedimientos y orientados a objetos, respectivamente.
## Programacion Orientada a Procedimientos
Anteriormente existían los lenguajes orientados a procedimientos en la decada de los 60´s, como Fortran, Cobol, Basic, etc.
### Desventajas:
- Unidades de código muy grandes en aplicaciones complejas.
- Codigo dificil de mantener
- Poco Reutilizable
- Si existe fallo en alguna línea del codigo, es muy probable que todo el programa caiga.
- Aparición frecuente de código espagueti (con goto u otros saltos hace que el codigo se vuelva un relajo, por su flujo de ejecución) 
- Dificil de depurar
## Programacion Orientada a Objetos
- ### ¿En que consiste?
Hace la analogía directamente a trasladar los objetos de la vida real, a un lenguaje de programacion, un objeto se compone de partes, como su estado fisico, propiedades de construccion, para que sirve, etc.
- ### Ejemplo clasico en POO
El objeto Carro
- ¿Cúal es el estado del carro? Por ejemplo puede estar estacionado, circulando, fallando, etc.
- ¿Qué propiedades tiene un carro? Un carro tiene un color, modelo, peso, tamaño, no de ruedas, serie, cilindraje, etc.
- ¿Cuál es el comportamiento de un carro? Un carro puede arrancar, acelerar, frenar, girar, etc.
Entonces, en resumen este objeto tienen Propiedades y Comportamientos
### Objeto:
### - Tiene Propiedades (atributos)
- Color 
- Peso
- Alto
- Largo
### Tiene un comportamiento (metodos)
- Arrancar
- Frenar
- Girar
- Acelerar 

### Ventajas:
- Programas divididos en "partes o trozos", "módulos" o "clases" (modularización).
- Reutilizable (Herencia).
- Si existe fallo en alguna línea del codigo, el programa continuará con su funcionamiento. (tratamiento de excepciones)
- Encapsulamiento.

### Vocabulario que se utiliza en POO
- Clase
- Objeto
- Instancia de clase
- Modularización
- Encapsulamiento / encapsulación
- Herencia
- Polimorfismo

### Clase
Una clase, es un modelo en donde se escriben o redactan las caracteristicas comunes de un grupo de objetos. Siguiendo con el ejemplo del carro, las cosas comunes de un auto serían, que tienen ruedas, tienen un chasis, un motor. En python se tiene que generar una clase con estos atributos (caracteristicas comunes) para poder generar una aplicacion para construir autos.

### Objeto, Instancia de clase (sinonimos)
Esto es generar un ejemplar perteneciente a una clase. Siguiendo con ejemplo del auto, en la clase se quedo que se definen las caracteristicas comunes del auto, cuando se crea una instancia u objeto de esa clase, lo que hacemos es decirle a esa clase cuantas llantas tiene ese auto, que motor tiene, que tipo de chasis, todas esas cosas definiran una instancia u objeto de otra. **Es decir comparten caracteristicas comunes (clase) pero cada uno se diferencia al agregar sus propiedades (instancia)**

### Modularización 
Si se tiene una aplicacion compleja, generalmente estara compuesta por varias clases. Asi como el motor de un auto tiene diferentes componentes (modulos) que al relacionarse entre si hace que este se mueva, encienda, etc. Y por ejemplo si falla algun componente se puede cambiar y no necesariamente va a dejar de funcionar el auto si este no funciona, incluso se puede reutilizar esa parte de un otro auto. De igual manera si se tiene un programa bien construido con POO al fallar alguna clase, el programa no dejara de funcionar, unicamente ese comportamiento que le daba esa clase a todo el programa no lo tendra.

### Encapsulacion
El encapsulamiento es dividir cada parte sin afectar lo demas. Por ejemplo el radio del carro nada sabe sobre el aire acondicionado, a el no le interesa si este funciona o no, y no afectara en su funcionamiento. En POO el funcionamiento de la clase 1 nada sabe sobre el funcionamiento sobre la clase 2.

### Metodos de acceso
A traves de estos metodos es como obtenemos el funcioanamiento de determinada clase. Por ejemplo al pizar el acelerador del auto, este le inyeca mas combustible al motor y por lo tanto el motor reacciona y permite desplazarse mas rápido, sin embargo nosotros como usuarios no sabemos como funciona el motor para que sea mas rapido, nosostros solo pizamos y este acelera. Lo mismo sucede en POO, se puede acceder solo a traves de este "pedal" a las otras clases. Por lo general para acceder a estos metodos en POO se utiliza el nombre de la instancia mas un punto y el nombre del metodo, ejemplo: carro1.acelerar()

