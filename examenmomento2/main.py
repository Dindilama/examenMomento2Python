class Producto:
    def __init__(self, producto_id, nombre, descripcion, costo, cantidad, margen_de_venta):
        self.producto_id = producto_id
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo
        self.cantidad = cantidad
        self.precio_de_venta = None
        self.registrar_precio_venta(margen_de_venta)

    def registrar_precio_venta(self, margen_de_venta):
        if margen_de_venta > 0:
            self.precio_de_venta = self.costo / (1 - margen_de_venta)
        else:
            print("El margen de venta debe ser mayor que 0.")

class RegistroProductos:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.producto_id not in self.productos:
            self.productos[producto.producto_id] = producto
        else:
            print(f"El producto con ID {producto.producto_id} ya existe en el registro.")

    def imprimir_productos(self):
        for producto_id, producto in self.productos.items():
            print(f'ID: {producto_id}, Nombre: {producto.nombre}, Precio de Venta: {producto.precio_de_venta}')

# Ejemplo de uso
registro = RegistroProductos()

producto1 = Producto(1, "Producto 1", "Descripción del Producto 1", 50, 10, 0.2)
producto2 = Producto(2, "Producto 2", "Descripción del Producto 2", 30, 5, 0.3)

registro.agregar_producto(producto1)
registro.agregar_producto(producto2)

registro.imprimir_productos()
