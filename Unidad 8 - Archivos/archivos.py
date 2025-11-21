import os
FILENAME = "productos.txt"
def guardararchivo():
    if not os.path.exists(FILENAME):
        ejemplos = [
            "Manzana,10.5,20",
            "Leche,55.0,10",
            "Pan,30,50"
        ]
        with open(FILENAME, "w", encoding="utf-8") as f:
            for linea in ejemplos:
                f.write(linea + "\n")

def cargar():
    productos = []
    with open(FILENAME, "r", encoding="utf-8") as f:
        for raw in f:
            linea = raw.strip()
            if not linea:
                continue
            partes = linea.split(",")
            if len(partes) != 3:
                continue
            nombre = partes[0].strip()
            precio = partes[1].strip()
            cantidad = partes[2].strip()
            productos.append({
                "nombre": nombre,
                "precio": precio,
                "cantidad": cantidad
            })
    return productos

def mostrar(productos):
    if not productos:
        print("No hay productos para mostrar.")
        return
    for p in productos:
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

def agregar(productos):
    print("\nIngresá un nuevo producto:")
    nombre = input("Nombre:")
    precio = input("Precio:")
    cantidad = input("Cantidad:")
    productos.append({
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    })
    print(f"Producto '{nombre}' agregado.")
    return True

def guardar_productos(productos):
    with open(FILENAME, "w", encoding="utf-8") as f:
        for p in productos:
            linea = f"{p['nombre']},{p['precio']},{p['cantidad']}\n"
            f.write(linea)

def buscar(productos):
    nombre_buscar = input("\nIngresá el nombre del producto a buscar:").strip()
    if not nombre_buscar:
        print("Búsqueda cancelada (nombre vacío).")
        return
    encontrados = [p for p in productos if p["nombre"].lower() == nombre_buscar.lower()]
    if encontrados:
        for p in encontrados:
            print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
    else:
        print(f"El producto '{nombre_buscar}' no existe.")

def main():
    guardararchivo()
    productos = cargar()
    print("Productos actuales:")
    mostrar(productos)
    agregar(productos)
    guardar_productos(productos)
    buscar(productos)

if __name__ == "__main__":
    main()
