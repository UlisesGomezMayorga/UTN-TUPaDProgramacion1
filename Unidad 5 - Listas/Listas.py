import random
# PUNTO 1
notas = [7, 5, 9, 6, 8, 10, 4, 6, 7, 9]
print("notas de los estudiantes:")
for n in notas:
    print(n)
promedio = sum(notas) / len(notas)
print("promedio:", promedio)
print("nota más alta:", max(notas))
print("nota más baja:", min(notas))


# PUNTO 2
productos = []
for i in range(5):
    prod = input(f"Ingresa el producto {i+1}: ")
    productos.append(prod)
print("\nProductos ordenados alfabéticamente:")
for p in sorted(productos):
    print(p)
elim = input("\n¿Qué producto desea eliminar?: ")
if elim in productos:
    productos.remove(elim)
print("\nLista actualizada:")
for p in productos:
    print(p)


# PUNTO 3
numeros = [random.randint(1, 100) for _ in range(15)]
pares = []
impares = []
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print("Lista completa:", numeros)
print("Cantidad de pares:", len(pares))
print("Cantidad de impares:", len(impares))


# PUNTO 4
lista_repetida = [2, 3, 4, 3, 5, 2, 6, 3, 7, 6]
sin_repetidos = []
for elem in lista_repetida:
    if elem not in sin_repetidos:
        sin_repetidos.append(elem)
print("Lista original:", lista_repetida)
print("Sin repetidos:", sin_repetidos)

# PUNTO 5
estudiantes = ["Ana", "Luis", "maria", "Jorge", "clara", "pédrotp", "Lucía", "Sofía"]
op = input("¿Desea agregar (A) o eliminar (E) un estudiante?: ").upper()
if op == "A":
    nuevo = input("Nombre del nuevo estudiante: ")
    estudiantes.append(nuevo)
elif op == "E":
    borrar = input("Nombre del estudiante a eliminar: ")
    if borrar in estudiantes:
        estudiantes.remove(borrar)
print("\nLista final:")
for e in estudiantes:
    print(e)


# PUNTO 6
lista_rotar = [1, 2, 3, 4, 5, 6, 7]
ultimo = lista_rotar[-1]
for i in range(len(lista_rotar)-1, 0, -1):
    lista_rotar[i] = lista_rotar[i-1]
lista_rotar[0] = ultimo
print("Lista rotada:", lista_rotar)


# PUNTO 7
temperaturas = [
    [10, 20],
    [12, 22],
    [9, 18],
    [8, 19],
    [15, 25],
    [11, 23],
    [7, 17]
]
minimas = []
maximas = []
amplitudes = []
for dia in temperaturas:
    minimas.append(dia[0])
    maximas.append(dia[1])
    amplitudes.append(dia[1] - dia[0])
print("promedio mínimas:", sum(minimas)/len(minimas))
print("promedio máximas:", sum(maximas)/len(maximas))
print("Mayor amplitud térmica en el día:", amplitudes.index(max(amplitudes)) + 1)


# PUNTO 8
notas = [
    [7, 8, 9],
    [6, 5, 7],
    [9, 9, 8],
    [4, 6, 5],
    [8, 7, 9]
]
print("promedio por estudiante:")
for i in range(5):
    prom = sum(notas[i]) / 3
    print(f"Estudiante {i+1}: {prom}")
print("\npromedio por materia:")
for m in range(3):
    suma = 0
    for e in range(5):
        suma += notas[e][m]
    print(f"Materia {m+1}: {suma / 5}")

# PUNTO 9
tablero = [["-" for _ in range(3)] for _ in range(3)]
for turno in range(1, 7):
    print(f"\nJugada {turno}")
    fila = int(input("Fila (0-2): "))
    col = int(input("Columna (0-2): "))
    ficha = input("Ficha (X/O): ").upper()
    tablero[fila][col] = ficha
    print("\nTablero:")
    for fila_t in tablero:
        print(fila_t)



# PUNTO 10
ventas = [
    [20, 30, 25, 28, 22, 27, 31],
    [15, 18, 20, 19, 17, 16, 22],
    [40, 42, 45, 41, 39, 38, 46],
    [10, 12, 11, 9, 14, 13, 15]
]
# Total por producto
print("Total vendido por cada producto:")
totales = []
for i in range(4):
    total = sum(ventas[i])
    totales.append(total)
    print(f"Producto {i+1}: {total}")
totales_dias = []
for d in range(7):
    suma = 0
    for p in range(4):
        suma += ventas[p][d]
    totales_dias.append(suma)
print("Día con mayores ventas:", totales_dias.index(max(totales_dias)) + 1)
print("Producto más vendido:", totales.index(max(totales)) + 1)
