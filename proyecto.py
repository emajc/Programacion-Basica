#Esta es la primera prueba del proyecto de gestion de inventarios

# Programa de Gestión de Inventarios

# Matriz de productos (vacía al inicio)
productos = []

# Función para mostrar el menú
def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Registrar producto")
    print("2. Actualizar cantidad (Compra/Venta)")
    print("3. Generar reporte de productos con bajo stock")
    print("4. Salir")

# Función para registrar un producto
def registrar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    codigo = input("Ingrese el código del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad disponible: "))
    umbral_minimo = int(input("Ingrese el umbral mínimo: "))

    # Verificar si el producto ya existe
    for producto in productos:
        if producto[1] == codigo:
            print("Error: El producto ya está registrado.")
            return

    # Registrar el nuevo producto
    productos.append([nombre, codigo, precio, cantidad, umbral_minimo])
    print("Producto registrado exitosamente.")

# Función para actualizar la cantidad de un producto
def actualizar_cantidad():
    codigo = input("Ingrese el código del producto: ")
    cantidad_modificacion = int(input("Ingrese la cantidad (positiva para compra, negativa para venta): "))

    # Buscar el producto por el código
    for producto in productos:
        if producto[1] == codigo:
            nueva_cantidad = producto[3] + cantidad_modificacion
            if nueva_cantidad < 0:
                print("Error: La cantidad no puede ser negativa.")
                return
            producto[3] = nueva_cantidad
            print(f"Cantidad actualizada. Nueva cantidad: {producto[3]}")
            return

    print("Error: Producto no encontrado.")

# Función para generar reporte de productos con bajo stock
def generar_reporte_bajo_stock():
    print("\nReporte de productos con bajo stock:")
    bajo_stock_encontrado = False
    for producto in productos:
        if producto[3] < producto[4]:  # Comparar cantidad con umbral mínimo
            print(f"Producto: {producto[0]}, Código: {producto[1]}, Cantidad: {producto[3]}")
            bajo_stock_encontrado = True

    if not bajo_stock_encontrado:
        print("No hay productos con bajo stock.")

# Función principal del programa
def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            actualizar_cantidad()
        elif opcion == "3":
            generar_reporte_bajo_stock()
        elif opcion == "4":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

# Ejecutar el programa
main()
