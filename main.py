from producto import Electrodomestico, Ropa, Alimento
from carrito import Carrito
from descuento import Descuento

def mostrar_menu():
    print("\n--- TIENDA ONLINE ---")
    print("1. Agregar Electrodoméstico")
    print("2. Agregar Ropa")
    print("3. Agregar Alimento")
    print("4. Ver Carrito")
    print("5. Calcular Total con Descuento")
    print("6. Vaciar Carrito")
    print("7. Salir")

carrito = Carrito()
descuento = Descuento()

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre del electrodoméstico: ")
        precio = float(input("Precio: "))
        garantia = int(input("Meses de garantía: "))
        producto = Electrodomestico(nombre, precio, garantia)
        carrito.agregar_producto(producto)
        print("Producto agregado.")

    elif opcion == "2":
        nombre = input("Nombre de la prenda: ")
        precio = float(input("Precio: "))
        talla = input("Talla: ")
        producto = Ropa(nombre, precio, talla)
        carrito.agregar_producto(producto)
        print("Producto agregado.")

    elif opcion == "3":
        nombre = input("Nombre del alimento: ")
        precio = float(input("Precio: "))
        fecha = input("Fecha de vencimiento (YYYY-MM-DD): ")
        producto = Alimento(nombre, precio, fecha)
        carrito.agregar_producto(producto)
        print("Producto agregado.")

    elif opcion == "4":
        print("\n--- Carrito de Compras ---")
        carrito.listar_productos()

    elif opcion == "5":
        total = carrito.calcular_total()
        total_descuento = descuento.aplicar(total)
        print(f"\nTotal sin descuento: ${total:.2f}")
        print(f"Total con descuento: ${total_descuento:.2f}")

    elif opcion == "6":
        carrito.vaciar()
        print("Carrito vaciado.")

    elif opcion == "7":
        print("Gracias por usar la tienda.")
        break

    else:
        print("Opción no válida.")
