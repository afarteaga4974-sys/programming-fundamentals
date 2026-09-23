class Producto:
    def __init__(self,nombre,caducidad,valor):
        self.nombre=nombre
        self.caducidad=caducidad
        self.valor=valor
producto1=Producto("azucar morena","10/10/2029",2500)
print(producto1.nombre)
print(producto1.caducidad)
print(producto1.valor)