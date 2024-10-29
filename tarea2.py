productos = []

def añadir_producto():
    nombre = input("Introduce el nombre del producto: ")
    if any(p["nombre"].lower()==nombre.lower() for p in productos):
        print(f"este producto ya existe '{nombre}'")
        return
    while True:
        try:
            precio = float(input("Introduce el precio del producto: "))
            if precio < 0:
                print ("el precio no puede ser negativo")
                continue 
            
            cantidad = int(input("Introduce la cantidad del producto: "))
            if cantidad < 0:
                print ("la cantidad no puede ser negativa")
                continue 
            break
        except ValueError:
            print ("por favor introduzca un numero valido")
    productos.append({'nombre': nombre, 'precio': precio, 'cantidad': cantidad})
    print("Producto añadido exitosamente.")
    guardar_datos()


def ver_productos():
    if not productos:
        print("No hay productos para mostrar.")
    else:
        print("Lista de productos:")
        for i, producto in enumerate(productos, start=1):
            print(f"{i}. Nombre: {producto['nombre']}, Precio: ${producto['precio']:.2f}, Cantidad: {producto['cantidad']}")

def actualizar_producto():
    nombre = input("Introduce el nombre del producto a actualizar: ")
    for producto in productos:
        if producto['nombre'].lower() == nombre.lower():
            nuevo_nombre = input("Introduce el nuevo nombre del producto (deja en blanco para no cambiar): ")
            nuevo_precio = input("Introduce el nuevo precio del producto (deja en blanco para no cambiar): ")
            nueva_cantidad = input("Introduce la nueva cantidad del producto (deja en blanco para no cambiar): ")
            
            if nuevo_nombre:
                producto['nombre'] = nuevo_nombre
            if nuevo_precio:
                producto['precio'] = float(nuevo_precio)
            if nueva_cantidad:
                producto['cantidad'] = int(nueva_cantidad)

            print("Producto actualizado exitosamente.")
            return
    
    print("Producto no encontrado.")

def eliminar_producto():
    nombre = input("Introduce el nombre del producto a eliminar: ")
    global productos
    productos = [producto for producto in productos if producto['nombre'].lower() != nombre.lower()]
    print("Producto eliminado exitosamente." if len(productos) < len(productos) else "Producto no encontrado.")

def guardar_datos():
    with open('productos.txt', 'w') as f:
        for producto in productos:
            f.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    print("Datos guardados exitosamente.")

def cargar_datos():
    try:
        with open('productos.txt', 'r') as f:
            for linea in f:
                nombre, precio, cantidad = linea.strip().split(',')
                productos.append({'nombre': nombre, 'precio': float(precio), 'cantidad': int(cantidad)})
        print("Datos cargados exitosamente.")
    except FileNotFoundError:
        print("No se encontró el archivo de datos. Se iniciará con una lista vacía.")

def menu():
    cargar_datos()  # Cargar productos al inicio
    while True:
        print("\nMenú de gestión de productos:")
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.")

# Iniciar el menú
menu()
