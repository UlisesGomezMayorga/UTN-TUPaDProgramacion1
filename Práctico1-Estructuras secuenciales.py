## 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
# print("Hola Mundo!")

# ------------------------------------------------------------------------------

## 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.
# nombre = input("Ingrese su nombre: ")
# print(f"Hola {nombre}!")

# ------------------------------------------------------------------------------


## 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.
# nombre = input("Ingrese su nombre: ")
# apellido = input("Ingrese su apellido: ")
# edad = input("Ingrese su edad: ")
# lugar = input("Ingrese su lugar de residencia: ")
# print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}")

# ------------------------------------------------------------------------------


## 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
# pi = 3.14
# radio = float(input("Ingrese el radio del círculo"))
# area = pi * radio ** 2
# perimetro = 2 * pi * radio
# print(f"El área del círculo es: {area:.2f}")
# print(f"El perímetro del círculo es: {perimetro:.2f}")

# ------------------------------------------------------------------------------

##5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
# segundos = int(input("Introduce la cantidad de segundos: "))
# horas = segundos // 3600
# minutos = (segundos % 3600) // 60
# segundos = segundos % 60
# print(f"{segundos} segundos equivalen a {horas} horas, {minutos} minutos y {segundos} segundos.")

# ------------------------------------------------------------------------------


## 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

# numero = int(input("Ingrese un número: "))
# print(f"Tabla de multiplicar del {numero}:")
# for i in range(1, 11):
#     print(f"{numero} x {i} = {numero * i}")

# ------------------------------------------------------------------------------

## 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos 

# num1 = int(input("Ingrese el primer número: "))
# num2 = int(input("Ingrese el segundo número: "   ))
# if num1 == 0 or num2 == 0:
#     print("Los números tiene que ser distintos a 0.")
# else:
#     suma = num1 +  num2
#     resta = num1 - num2
#     multiplicacion = num1 * num2
#     if num2 != 0:
#         division = num1 / num2
#     else:
#         division = None
#     print(f"La suma es: {suma}")
#     print(f"La resta es: {resta}")
#     print(f"La multiplicación es: {multiplicacion}")
#     if division is not None:
#         print(f"La división es: {division}")

# ------------------------------------------------------------------------------


## 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. Tener en cuenta que el índice de masa corporal
# altura = float(input("Ingrese su altura en metros: "))
# peso = float(input("Ingrese su peso en kilos: "))
# imc = peso / (altura ** 2)
# print(f"Su índice de masa corporal es: {imc:.2f}")


# ------------------------------------------------------------------------------


## 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.

# celsius = float(input("Ingrese la temperatura en grados celsiud: "))
# fahrenheit = (celsius * 9/5) + 32
# print(f"Temperatura en grados Fahrenheit: {fahrenheit:.2f}")

# ------------------------------------------------------------------------------



## 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
# num1 = float(input("Ingrese el primer número: "))
# num2 = float(input("Ingrese el segundo número: "))
# num3 = float(input("Ingrese el tercer número: "))
# promedio = (num1 + num2 + num3) / 3
# print(f"El promedio es: {promedio:.2f}")
