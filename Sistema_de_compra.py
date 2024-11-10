class prenda:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_detalle(self):
        print(f"Nombre: {self.nombre}")
        print(f"Precio: {self.precio}")
        print(f"Cantidad: {self.cantidad}")

class RopaHombre(prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla

    def mostrar_detalle(self):
        super().mostrar_detalle()
        print(f"Talla: {self.talla}")


class RopaMujer(prenda):
    def __init__(self, nombre,precio, cantidad, talla):
        super().__init__(nombre,precio, cantidad)
        self.talla = talla

    def mostrar_detalle(self):
        super().mostrar_detalle()
        print(f"Talla: {self.talla}")


class inventario:
    def __init__(self):
        self.prendas = []

    def agregar_prenda(self, prenda):
        self.prendas.append(prenda)

    def mostrar_inventario(self):
        print("Inventario:")
        for prenda in self.prendas:
            prenda.mostrar_detalle()
            print("--------------------")

# Crear  instancias de RopaHombre y RopaMujer
camisa_hombre = RopaHombre("Camisa", 25.00, 50, "p,m,g")
pantalon_hombre = RopaHombre("pantalon", 30.00, 30, "p,m,g")
chaqueta_hombre = RopaHombre("chaqueta", 55.00, 20, "p,m,g")
zapatos_hombre = RopaHombre("zapatos", 60.00, 25, "40,41,42,43,44,45")
falda_mujer = RopaMujer("falda", 28.00, 15, "p,m,g")
blusa_mujer = RopaMujer("blusa", 22.00, 40, "p,m,g")
vestido_mujer = RopaMujer("vestido", 60.00, 20, "p,m,g")
zapatos_mujer = RopaMujer("zapatos", 50.00, 20, "36,37,38,39,40,41")

# Crear instancia de inventario
inventario = inventario()

# Agregar prendas al inventario
inventario.agregar_prenda(camisa_hombre)
inventario.agregar_prenda(pantalon_hombre)
inventario.agregar_prenda(chaqueta_hombre)
inventario.agregar_prenda(zapatos_hombre)

inventario.agregar_prenda(falda_mujer)
inventario.agregar_prenda(blusa_mujer)
inventario.agregar_prenda(vestido_mujer)
inventario.agregar_prenda(zapatos_mujer)

# Mostrar el inventario
inventario.mostrar_inventario()

