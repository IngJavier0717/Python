print ("¡Hola, Mundo!")

print ("\nEjemplo ")
edad = 18
#int (input ("¿Cuál es tu edad? "))
if edad >= 18:
   print ("Eres mayor de edad.")
else:
    print ("Eres menor de edad.")


# Inicio del ejemplo 2
print ("\nEjemplo 2")
calificacion = 95
#int (input ("Ingresa tu calificación: "))    

if calificacion >= 90:
   print ("Excelente")

elif calificacion >= 80:
   print ("Muy bueno")

elif calificacion >= 70:
   print ("Bueno")

else:
   print ("Necesita mejorar")

#3.1. Bucles/loops
print ("\n\nBucles/loops")
print ("\nEjemplo 2 FOR")
#For
frutas = ["manzana", "banana", "naranja"]

for fruta in frutas:
    print(fruta)

print ("\nEjemplo 2 WHILE")
#While
contador = 0
while contador < 5:

    print(contador)
    contador += 1

#Control de bucles
#BREAK
print ("\nControl de bucles")
print ("\nEjemplo 3 BREAK")

contador = 0

while True:
    print(contador)
    contador += 1
    if contador == 5:
        break


#CONTINUE
print ("\nEjemplo 4 CONTINUE")
for i in range(10):

    if i % 2 == 0:
        continue
    print(i)

#PASS
print ("\nEjemplo 5 PASS")
for i in range(5):
    pass

#4. Estructuras de datos
print ("\nEstructuras de datos")
#Listas
print ("\nEjemplo 6 LISTAS")
frutas = ["manzana", "banana", "naranja"]
print(frutas)
print(frutas[0])  # Imprime "manzana"
print(frutas[1])  # Imprime "banana"
print(frutas[2])  # Imprime "naranja"
#Índices negativos
print(frutas[-1])  # Imprime "naranja"
print(frutas[-2])  # Imprime "banana"
print(frutas[-3])  # Imprime "manzana"

#Métodos de listas
print ("\nMétodos de listas")
frutas = ["manzana", "banana", "naranja"]

frutas.append("pera")
print(frutas)  # Imprime ["manzana", "banana", "naranja", "pera"]

frutas.insert(1, "uva")
print(frutas)  # Imprime ["manzana", "uva", "banana", "naranja", "pera"]

frutas.remove("banana")
print(frutas)  # Imprime ["manzana", "uva", "naranja", "pera"]

fruta_eliminada = frutas.pop(2)
print(frutas)  # Imprime ["manzana", "uva", "pera"]
print(fruta_eliminada)  # Imprime "naranja"

frutas.sort()
print(frutas)  # Imprime ["manzana", "pera", "uva"]

frutas.reverse()
print(frutas)  # Imprime ["uva", "pera", "manzana"]
# Fin del programa

#Listas de comprensión
#nueva_lista = [expresion for elemento in secuencia if condicion]
print ("\nEjemplo 7 LISTAS DE COMPRENSIÓN")
#Sin condición
numeros = [1, 2, 3, 4, 5]
cuadrados = [x**2 for x in numeros]
print(cuadrados)  # Imprime [1, 4, 9, 16, 25]

#Con condición
numeros = [1, 2, 3, 4, 5]
cuadrados = [x ** 2 for x in numeros if x % 2 == 0]
print(cuadrados)  # Imprime [4, 16]

#4.1. Tuplas
print ("\nEjemplo 8 TUPLAS")
#Creación y acceso
print ("\nCreación y acceso")
punto = (3, 4)
print(punto)        # Imprime (3, 4)
print(punto[0])     # Imprime 3 
print(punto[1])     # Imprime 4

#Métodos de tuplas
print ("\nMétodos de tuplas")
mi_tupla = (1, 2, 3, 2, 4, 2)

print (mi_tupla.index(2))   # Salida: 1
print (mi_tupla.index(2, 2))   #Salida: 3
print (mi_tupla.index(2, 2, 4))   #Salida: 3

#4.2. Diccionarios
print ("\nEjemplo 9 DICCIONARIOS")
#Creación y acceso
print ("\nCreación y acceso")
persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}
print(persona)               # Imprime el diccionario completo
print(persona["nombre"])     # Imprime "Juan"
print(persona["edad"])       # Imprime 25
print(persona["ciudad"])     # Imprime "Madrid"

#Métodos de diccionarios
print ("\nMétodos de diccionarios")
persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}
persona.keys()
print(persona.keys())        # Imprime las claves del diccionario
persona.values()
print(persona.values())      # Imprime los valores del diccionario
persona.items()
print(persona.items())       # Imprime los pares clave-valor del diccionario
persona.update({"edad": 26})
print(persona)               # Imprime el diccionario actualizado
persona.pop("ciudad")
print(persona)               # Imprime el diccionario sin la clave "ciudad"
persona.clear()
print(persona)               # Imprime un diccionario vacío {}

persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}

print(persona.keys())    # Imprime dict_keys(["nombre", "edad", "ciudad"])
print(persona.values())  # Imprime dict_values(["Juan", 25, "Madrid"])
print(persona.items())   # Imprime dict_items([("nombre", "Juan"), ("edad", 25), ("ciudad", "Madrid")])

persona.update({"profesion": "Ingeniero"})
print(persona)  # Imprime {"nombre": "Juan", "edad": 25, "ciudad": "Madrid", "profesion": "Ingeniero"}

#4.3. Conjuntos (set)
print ("\nEjemplo 10 CONJUNTOS (set)")
#Creación y operaciones básicas
print ("\nCreación y operaciones básicas")

frutas = {"manzana", "banana", "naranja"}
numeros = set([1, 2, 3, 4, 5])

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
union = conjunto1 | conjunto2
print(union)  # Imprime {1, 2, 3, 4, 5}

interseccion = conjunto1 & conjunto2
print(interseccion)  # Imprime {3}

diferencia = conjunto1 - conjunto2
print(diferencia)  # Imprime {1, 2}

diferencia_simetrica = conjunto1 ^ conjunto2
print(diferencia_simetrica)  # Imprime {1, 2, 4, 5}

#Métodos de conjuntos
print ("\nMétodos de conjuntos")
frutas = {"manzana", "banana", "naranja"}

frutas.add("pera")
print(frutas)  # Imprime {"manzana", "banana", "naranja", "pera"}

frutas.remove("banana")
print(frutas)  # Imprime {"manzana", "naranja", "pera"}

frutas.discard("uva")
print(frutas)  # Imprime {"manzana", "naranja", "pera"}

frutas.clear()
print(frutas)  # Imprime set()

#5. Funciones
print ("\nFunciones")
#Definición y llamada de funciones
"""
Para definir una función en Python, utilizamos la palabra clave def seguida del nombre de la función y paréntesis. 
Opcionalmente, podemos especificar parámetros dentro de los paréntesis. 
El bloque de código de la función se indenta después de los dos puntos.
Para llamar a una función, simplemente escribimos el nombre de la función seguido de paréntesis:
"""
def saludo():
    print("¡Hola, mundo!")
saludo()  # Imprime "¡Hola, mundo!"

#Parámetros y argumentos
print ("\nParámetros y argumentos")

def saludo(nombre):
    print(f"¡Hola, {nombre}!")

saludo("Juan")  # Imprime "¡Hola, Juan!"
saludo("María")  # Imprime "¡Hola, María!"

#Valores de retorno
def suma(a, b):
    return a + b
resultado = suma(3, 4)
print(resultado)  # Imprime 7

#Funciones lambda
print ("\nFunciones lambda")
cuadrado = lambda x: x ** 2
print(cuadrado(5))  # Imprime 25

suma = lambda a, b: a + b
print(suma(3, 4))  # Imprime 7
mayor = lambda a, b: a if a > b else b
print(mayor(5, 10))  # Imprime 10
minimo = lambda a, b: a if a < b else b
print(minimo(5, 10))  # Imprime 5
multiplicar = lambda a, b: a * b
print(multiplicar(3, 4))  # Imprime 12
dividir = lambda a, b: a / b if b != 0 else "Error: División por cero"
print(dividir(10, 2))  # Imprime 5.0
print(dividir(10, 0))  # Imprime "Error: División por cero"


#Alcance de las variables (local vs. global)
print ("\nAlcance de las variables (local vs. global)")
def funcion():
    variable_local = 10
    print(variable_local)  # Accesible dentro de la función

variable_global = 20
def funcion2():
    print(variable_global)  # Accesible desde cualquier lugar

funcion()  # Imprime 10
funcion2()  # Imprime 20
print(variable_global)  # Imprime 20
#print(variable_local)  # Genera un error, la variable no está definida en este alcance.

#Documentación de funciones (docstrings)
print ("\nDocumentación de funciones (docstrings)")
def area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.


    Args:
        base (float): La base del rectángulo.
        altura (float): La altura del rectángulo.


    Returns:
        float: El área del rectángulo.
    """
    return base * altura

#Funciones con número variable de argumentos
print ("\nFunciones con número variable de argumentos")
def suma_variable(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

print(suma_variable(1, 2, 3))  # Imprime 6
print(suma_variable(4, 5, 6, 7))  # Imprime 22

#6.1. Manejo de excepciones
print ("\nManejo de excepciones")
#Try, except y finally
#TRY
print ("\nTRY")
try:
    # Código que puede generar una excepción
    resultado = 10 / 0  # División por cero
    print(resultado)
except ZeroDivisionError:
    print("Error: División por cero")

#EXCEPT
print ("\nEXCEPT")
try:
    # Código que puede generar una excepción
    resultado = 10 / 0  # División por cero
    print(resultado)
except ZeroDivisionError:
    print("Error: División por cero")
except ValueError:
    print("Error: Valor inválido")

#FINALLY
print ("\nFINALLY")
try:
    #Escritura de archivos
    print ("\nEscritura de archivos")
    archivo = open("datos.txt", "w")
    archivo.write("Hola, mundo!")
    archivo.close()
    # Código que puede generar una excepción
    archivo = open("datos.txt", "r")
    # Realizar operaciones con el archivo
except FileNotFoundError:
    print("Error: Archivo no encontrado")
finally:
    archivo.close()  # Cerrar el archivo siempre, incluso si ocurre una excepción

#6.2. Excepciones personalizadas
print ("\nExcepciones personalizadas")
def funcion():
    # Código que puede generar una excepción personalizada
    if edad < 0:
        raise Exception("Descripción del error")
try:
    funcion()
except Exception as e:
    print(f"Error: {str(e)}")

#7. Entradas/salidas
print ("\nEntradas/salidas")
#Entrada de datos del usuario
print ("\nEntrada de datos del usuario")
nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")

print("Hola, " + nombre + "!")
print("Tienes " + edad + " años.")

#tipo de datos de entrada
print ("\nTipo de datos de entrada")
edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

#Salida de datos
nombre = "Juan"
edad = 25

print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")

#7.1. Lectura y escritura de archivos
print ("\nLectura y escritura de archivos")
#Lectura de archivos
print ("\nLectura de archivos")
archivo = open("datos.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()

#Escritura de archivos
print ("\nEscritura de archivos")
archivo = open("datos.txt", "w")
archivo.write("Hola, mundo!")
archivo.close()

#También puedes utilizar la declaración with para manejar la apertura y cierre de archivos de manera automática.
with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

#8. Importación y creación de módulos
print ("\nImportación y creación de módulos")

#Importación de módulos
print ("\nImportación de módulos")
import math

resultado = math.sqrt(25)
print(resultado)  # Imprime 5.0

#También podemos importar funciones específicas de un módulo utilizando la sintaxis from módulo import función.
from math import sqrt

resultado = sqrt(25)
print(resultado)  # Imprime 5.0

#Funciones y clases de módulos estándar
print ("\nFunciones y clases de módulos estándar")
import random
import datetime

numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)  # Imprime un número entero aleatorio entre 1 y 10

fecha_actual = datetime.datetime.now()
print(fecha_actual)  # Imprime la fecha y hora actual

#8.1. Creación de módulos propios
print ("\nCreación de módulos propios")
#Crear y utilizar módulos personalizados
print ("\nCrear y utilizar módulos personalizados")
#mi_modulo.py

#Luego, podemos importar y utilizar las funciones definidas en mi_modulo.py en otro archivo Python.
import mi_modulo

mi_modulo.saludar("Juan")  # Imprime "Hola, Juan!"
resultado = mi_modulo.calcular_suma(5, 3)
print(resultado)  # Imprime 8

#Organización del código en módulos
print ("\nOrganización del código en módulos")
# operaciones.py
#Luego, podemos importar y utilizar estas funciones en nuestro programa principal.
import operaciones
import utilidades

resultado = operaciones.sumar(5, 3)
utilidades.imprimir_mensaje(f"El resultado de la suma es: {resultado}")

nombre = utilidades.obtener_nombre_usuario()
utilidades.imprimir_mensaje(f"Hola, {nombre}!")

#8.2. Paquetes
print ("\nPaquetes")
#Crear y utilizar paquetes
print ("\nCrear y utilizar paquetes")

#Por ejemplo, creamos un directorio llamado mi_paquete con la siguiente estructura:
#mi_paquete/
#    __init__.py
#    modulo1.py
#    modulo2.py
#Luego, podemos importar y utilizar los módulos dentro del paquete de la siguiente manera:
#from mi_paquete import modulo1, modulo2
#modulo1.funcion1()
#modulo2.funcion2()

(not True) or (False and True) 