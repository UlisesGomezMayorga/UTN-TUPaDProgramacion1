precios_frutas = {'banana':1200, 'ananá':2500, 'melón':3000, 'uva':1450}


# Punto 1
precios_frutas['naranja'] = 1200
precios_frutas['manzana'] = 1500
precios_frutas['pera'] = 2300
print(precios_frutas)

# Punto 2
precios_frutas['banana'] = 1330
precios_frutas['manzana'] = 1700
precios_frutas['melón'] = 2800
print(precios_frutas)

# Punto 3
lista_frutas = list(precios_frutas.keys())
print(lista_frutas)


# Punto 4
contactos = {}
for i in range(1, 6):
    nombre = input(f"Contacto {i} - Ingresá el nombre:").strip()
    numero = input(f"Ingresá el número de {nombre}:").strip()
    contactos[nombre] = numero
print("\nAgenda cargada:")
for n, num in contactos.items():
    print(f"{n}:{num}")
consulta = input("\nIngresá un nombre para consultar su número:").strip()
if consulta in contactos:
    print(f"El número de {consulta} es:{contactos[consulta]}")
else:
    print(f"No existe el contacto'{consulta}' en la agenda.")



# Punto 5

frase = input("Ingresá una frase:").strip()
palabras = frase.lower().split()
unicas = set(palabras)
recuento = {}
for p in palabras:
    recuento[p] = recuento.get(p, 0) + 1
print(f"Palabras únicas:{unicas}")
print(f"Recuento:{recuento}")


# Punto 6
alumnos = {}
for i in range(3):
    nombre = input("Nombre del alumno:")
    notas = tuple(float(input(f"Nota {j+1}:")) for j in range(3))
    alumnos[nombre] = notas
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")


# Punto 7
parcial1 = {1, 2, 3, 4}
parcial2 = {3, 4, 5, 6}
print("Los dos parciales:", parcial1 & parcial2)
print("Solo uno:", parcial1 ^ parcial2)
print("por lo menos uno:", parcial1 | parcial2)


# Punto 8
inventario = {"harina": 10, "azucar": 5}
producto = input("Producto a consultar:")
print("Stock:", inventario.get(producto, "No existe"))
producto = input("Producto para agregar stock:")
cantidad = int(input("Cantidad:"))
if producto in inventario:
    inventario[producto] += cantidad
else:
    inventario[producto] = cantidad
print("Inventario actualizado:", inventario)


# Punto 9
agenda = {
    ("lunes", "10:00"):"Reunión",
    ("martes", "15:00"):"Clase de inglés",
    ("miércoles", "09:30"):"Gimnasio",
}
dia = input("Ingresá el día:").strip().lower()
hora = input("Ingresá la hora (hh:mm):").strip()
evento = agenda.get((dia, hora), "mo hay actividad en ese día y hora.")
print("Actividad:", evento)


# Punto 10
original = {
    "Argentina":"Buenos Aires",
    "Chile":"Santiago",
    "Perú":"Lima",
}
invertido = {capital: pais for pais, capital in original.items()}
print("original:", original)
print("invertido:", invertido)