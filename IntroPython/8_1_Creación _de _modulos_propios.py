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