class Producto:
    def ___init___(self,nombre,caducidad,valor):
        self.nombre = nombre
        self.caducidad = caducidad
        self.valor = valor
producto1= Producto("arroz roa",10/10/2028,2700)
print(producto1.nombre)
print(producto1.caducidad)
print(producto1.valor)