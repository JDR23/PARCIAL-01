# producto.py

class Producto:
    def __init__(self, nombre: str, precio: float):
        self._nombre = nombre
        self._precio = precio

    def obtener_nombre(self) -> str:
        return self._nombre

    def obtener_precio(self) -> float:
        return self._precio

    def __str__(self):
        return f"{self._nombre} - ${self._precio:.2f}"


class Electrodomestico(Producto):
    def __init__(self, nombre: str, precio: float, garantia: int):
        super().__init__(nombre, precio)
        self.garantia = garantia


class Ropa(Producto):
    def __init__(self, nombre: str, precio: float, talla: str):
        super().__init__(nombre, precio)
        self.talla = talla


class Alimento(Producto):
    def __init__(self, nombre: str, precio: float, fecha_vencimiento: str):
        super().__init__(nombre, precio)
        self.fecha_vencimiento = fecha_vencimiento
