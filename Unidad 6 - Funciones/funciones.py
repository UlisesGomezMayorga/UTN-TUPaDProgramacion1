import math

# PUNTO 1
def imprimir_hola_mundo():
    print("Hola Mundo!")
imprimir_hola_mundo()


# PUNTO 2
def saludar_usuario(nombre):
    return f"Hola {nombre}!"
nombre = input("ingresá su nombre: ")
print(saludar_usuario(nombre))


# PUNTO 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
nom = input("Nombre: ")
ape = input("Apellido: ")
edad = input("Edad: ")
res = input("Residencia: ")
informacion_personal(nom, ape, edad, res)

# PUNTO 4
def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)
def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio
radio = float(input("ingresá el radio del círculo: "))
print("Área del círculo:", calcular_area_circulo(radio))
print("Perímetro del círculo:", calcular_perimetro_circulo(radio))

# PUNTO 5
def segundos_a_horas(segundos):
    return segundos / 3600
seg = int(input("ingresá una cantidad de segundos: "))
print("Equivalen a", segundos_a_horas(seg), "horas")

# PUNTO 6
def tabla_multiplicar(numero):
    print(f"Tabla del {numero}:")
    for i in range(1, 10 + 1):
        print(f"{numero} x {i} = {numero * i}")
num_tabla = int(input("ingresá un número para la tabla: "))
tabla_multiplicar(num_tabla)


# PUNTO 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multi = a * b
    div = a / b if b != 0 else "Error: división por cero"
    return suma, resta, multi, div
a = float(input("ingresá el primer número: "))
b = float(input("ingresá el segundo número: "))
resultado = operaciones_basicas(a, b)
print("\nResultados:")
print("Suma:", resultado[0])
print("Resta:", resultado[1])
print("Multiplicación:", resultado[2])
print("División:", resultado[3])


# PUNTO 8
def calcular_imc(peso, altura):
    return peso / (altura ** 2)
peso = float(input("ingresá su peso en kg: "))
altura = float(input("ingresá su altura en metros: "))
print(f"Su IMC es: {calcular_imc(peso, altura):.2f}")


# PUNTO 9
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32
celsius = float(input("ingresá la temperatura en Celsius: "))
print("En Fahrenheit es:", celsius_a_fahrenheit(celsius))

# PUNTO 10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3
n1 = float(input("ingresá el primer número: "))
n2 = float(input("ingresá el segundo número: "))
n3 = float(input("ingresá el tercer número: "))
print("El promedio es:", calcular_promedio(n1, n2, n3))
