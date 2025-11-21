import os
FILENAME = os.path.join(os.path.dirname(__file__), "productos.txt")

def guardararchivo():
    if not os.path.exists(FILENAME):
        ejemplos = [
            "Manzana,10.5,20",
            "Leche,55.0,10",
            "Pan,30,50"
        ]
        os.makedirs(os.path.dirname(FILENAME), exist_ok=True)
        with open(FILENAME, "w", encoding="utf-8") as f:
            for linea in ejemplos:
                f.write(linea + "\n")
def cargar():
    productos = []
    if not os.path.exists(FILENAME):
        return productos
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
    print("\nListado de productos:")
    for p in productos:
        print(f" - Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
    print()

def agregar(productos):
    print("\nIngresá un nuevo producto (dejar nombre vacío cancela):")
    nombre = input("nombre:").strip()
    if not nombre:
        print("Alta cancelada.")
        return False
    while True:
        precio = input("precio:").strip()
        try:
            float(precio)
            break
        except ValueError:
            print("precio inválido. Ingresá un número.")
    while True:
        cantidad = input("cantidad:").strip()
        if cantidad.isdigit():
            break
        print("cantidad inválida. Ingresá un entero.")
    productos.append({
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    })
    print(f"producto '{nombre}' agregado.")
    return True

def guardar_productos(productos):
    with open(FILENAME, "w", encoding="utf-8") as f:
        for p in productos:
            linea = f"{p['nombre']},{p['precio']},{p['cantidad']}\n"
            f.write(linea)
    print("cambios guardados en el archivo.")

def buscar(productos):
    nombre_buscar = input("\nIngresá el nombre del producto a buscar:").strip()
    if not nombre_buscar:
        print("búsqueda cancelada (nombre vacío).")
        return
    encontrados = [p for p in productos if p["nombre"].lower() == nombre_buscar.lower()]
    if encontrados:
        for p in encontrados:
            print(f"producto: {p['nombre']} | precio: ${p['precio']} | cantidad: {p['cantidad']}")
    else:
        print(f"El producto '{nombre_buscar}' no existe.")

def main():
    guardararchivo()
    productos = cargar()
    cambios = False

    menu = """
            Menú:
            1) Mmostrar productos
            2) agregar producto
            3) buscar producto
            4) guardar en archivo
            5) recargar desde archivo (pierde cambios no guardados)
            6) salir
            Elegí una opción (1-6):"""

    while True:
        try:
            opcion = input(menu).strip()
        except (EOFError, KeyboardInterrupt):
            print("\nSalida forzada.")
            opcion = "6"
        if opcion == "1":
            mostrar(productos)
        elif opcion == "2":
            if agregar(productos):
                cambios = True
        elif opcion == "3":
            buscar(productos)
        elif opcion == "4":
            guardar_productos(productos)
            cambios = False
        elif opcion == "5":
            if cambios:
                confirmar = input("¿Desea recargar y perder los datos no guardados? (s/N):").strip().lower()
                if confirmar != "s":
                    continue
            productos = cargar()
            cambios = False
            print("Archivo cargado.")
        elif opcion == "6":
            if cambios:
                confirmar = input("Guardar antes de salir? (S/n):").strip().lower()
                if confirmar in ("", "s"):
                    guardar_productos(productos)
            print("Saliendo.")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()
