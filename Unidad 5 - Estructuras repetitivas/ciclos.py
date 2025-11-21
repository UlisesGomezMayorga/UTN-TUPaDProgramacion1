import random

# PUNTO 1

for i in range(101):
    print(i)
    
# PUNTO 2
numero = input("Ingresá un número entero:")
print("Cantidad de dígitos:", len(numero))

# PUNTO 3
a = int(input("Ingresá el primer número:"))
b = int(input("Ingresá el segundo número:"))

suma = 0
for i in range(a + 1, b):
    suma += i

print("La suma es:", suma)

# PUNTO 4
suma = 0
while True:
    num = int(input("Ingresá un número (0 para terminar):"))
    if num == 0:
        break
    suma += num

print("Total acumulado:", suma)

# PUNTO 5
numero_secreto = random.randint(0, 9)
intentos = 0
while True:
    intento = int(input("Adivine el número (0-9):"))
    intentos += 1
    if intento == numero_secreto:
        print(f"¡Correcto! Intentos: {intentos}")
        break
    
# PUNTO 6
for i in range(100, -1, -2):
    print(i)
    
# PUNTO 7
n = int(input("Ingresá un número positivo:"))
suma = 0
for i in range(n + 1):
    suma += i
print("La suma es:", suma)

# PUNTO 8
pares = impares = positivos = negativos = 0

for _ in range(100):
    num = int(input("Ingresá un número:"))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1


# PUNTO 9
suma = 0
for _ in range(100):
    num = int(input("Ingresá un número:"))
    suma += num

media = suma / 100
print("La media es:", media)


# PUNTO 10
numero = input("Ingresá un número:")
invertido = numero[::-1]
print("Número invertido:", invertido)