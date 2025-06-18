#Declaracion de variables
varEntero = 5
varDouble = 5.5
varStr = "Hola, soy Cristian"

#Operaciones
suma = varEntero + varDouble
resta = varEntero - varDouble
multiplicacion = varEntero * varDouble
division = varDouble / varEntero

print(varStr)
print(suma)
print(resta)
print(multiplicacion)
print(division)

#Concatenacion

saludo = "Hola! "

nombre = input("Escribe tu nombre: ")

print(saludo , nombre , "Este es mi laboratorio de python!")

#Condicionales y bucles

ingresaNumero = input("Escribe un número: ")

if ingresaNumero.isdigit():
    print("Es un número entero válido.")
else:
    print("No es un número entero válido.")


numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    cuadrado = numero ** 2
    print(f"El cuadrado de {numero} es {cuadrado}")
    
  
numeroBucle = 0  

while numeroBucle <= 10:
    numeroBucle = int(input("Ingresa un número mayor que 10: "))

print(f"¡Bien! Has ingresado el número {numeroBucle}, que es mayor que 10.")


#Listas y diccionarios


# Lista inicial de estudiantes
nombresEstudiantes = ["Ana", "Carlos", "Luis", "María", "Sofía", "Juan"]

# Estudiantes
print("Lista de estudiantes:")
for nombre in nombresEstudiantes:
    print(nombre)

# Diccionario de contacto
contacto = {
    "nombre": "Juan Pérez",
    "correo": "juan.perez@ejemplo.com"
}

print("\nInformación de contacto:")
for clave, valor in contacto.items():
    print(f"{clave}: {valor}")

# Menú 
while True:
    print("\n¿Qué deseas hacer?")
    print("1. Agregar estudiante a la lista")
    print("2. Actualizar valor en el diccionario")
    print("3. Ver lista de estudiantes")
    print("4. Ver diccionario")
    print("5. Salir")

    opcion = input("Ingresa una opción (1-5): ")

    if opcion == "1":
        elemento = input("Escribe el nombre del estudiante que deseas agregar: ")
        nombresEstudiantes.append(elemento)
        print("Estudiante agregado.")

    elif opcion == "2":
        clave = input("Escribe la clave que deseas actualizar (ej: nombre, correo): ")
        valor = input(f"Ingrese el nuevo valor para '{clave}': ")
        contacto[clave] = valor
        print("Diccionario actualizado.")

    elif opcion == "3":
        print("Lista de estudiantes actual:", nombresEstudiantes)

    elif opcion == "4":
        print("Diccionario actual:")
        for k, v in contacto.items():
            print(f"{k}: {v}")

    elif opcion == "5":
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")
        

#CALCULADORA

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero."
    return a / b

while True:
    print("\n--- Calculadora Básica ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Selecciona una opción (1-5): ")

    if opcion == "5":
        print("Gracias por usar la calculadora. ¡Hasta luego!")
        break

    if opcion in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Error: Debes ingresar números válidos.")
            continue

        if opcion == "1":
            resultado = sumar(num1, num2)
            operacion = "Suma"
        elif opcion == "2":
            resultado = restar(num1, num2)
            operacion = "Resta"
        elif opcion == "3":
            resultado = multiplicar(num1, num2)
            operacion = "Multiplicación"
        elif opcion == "4":
            resultado = dividir(num1, num2)
            operacion = "División"

        print(f"{operacion} de {num1} y {num2} es: {resultado}")
    else:
        print("Opción inválida. Por favor, elige una opción del 1 al 5.")
    
    
#ADIVINANZA

import random

# Generar número aleatorio entre 1 y 10
numero_secreto = random.randint(1, 10)
intentos = 0

print("Bienvenido al juego de adivinanza")
print("Adivina el número secreto entre 1 y 10")

while True:
    try:
        adivinanza = int(input("Ingresa tu número: "))
        intentos += 1

        if adivinanza < numero_secreto:
            print("El número secreto es mayor.")
        elif adivinanza > numero_secreto:
            print("El número secreto es menor.")
        else:
            print(f"¡Correcto! El número era {numero_secreto}.")
            print(f"Adivinaste en {intentos} intento(s).")
            break
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero.")
    

