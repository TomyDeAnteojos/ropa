class Ropa:
    def __init__(self):
        self.ropa = ''
        self.descripcion = ''
        self.precio = 0.0
        self.estado = True

    def __init__(self, ropa, descripcion, precio):
        self.ropa = ropa
        self.descripcion = descripcion
        self.precio = precio
        self.estado = True

    def agregar(self, ropa, descripcion, precio):
        self.ropa = ropa
        self.descripcion = descripcion
        self.precio = precio

    def mostrar(self):
        if self.estado:
            print(f"Ropa: {self.ropa}")
            print(f"Descripcion: {self.descripcion}")
            print(f"Precio: ${self.precio}")

    def modificar(self):
        self.ropa = input("Ingrese ropa: ")
        self.descripcion = input("Ingrese descripcion: ")
        self.precio = 0
        while self.precio <= 0:
            self.precio = float(input("Ingrese precio: "))

    
def agregarRopa():
    ropa = input("Ingrese ropa: ")
    descripcion = input("Ingrese descripcion: ")
    precio = 0
    while precio <= 0:
        precio = float(input("Ingrese precio: "))
    return Ropa(ropa, descripcion, precio)

list = []

while True:
    print("          MENU"          )
    print("------------------------")
    print("1) Agregar ropa"         )
    print("2) Listar prendas"       )
    print("3) Modificar ropa"       )
    print("4) Eliminar ropa"        )
    print("------------------------")
    op = int(input("Ingrese una opcion: "))

    if op == 1: 
        list.append(agregarRopa())
    
    if op == 2:
        for i in list:
            i.mostrar()
            print("------------------------")
            print()

    if op == 3:
        md = int(input("cual quiere modificar: "))
        if len(list) > md-1:
            list[md-1].modificar()