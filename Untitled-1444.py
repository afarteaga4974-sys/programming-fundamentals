class Producto:
    def __init__(self,nombre,marca,precio):
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
producto1 = Producto("cogin","nine",2000)
print(producto1.nombre)
print(producto1.marca)
print(producto1.precio)