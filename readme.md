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