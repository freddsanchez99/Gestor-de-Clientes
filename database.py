class Cliente:
    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
    
    def __str__(self):
        return f"{self.dni} -> {self.nombre} {self.apellido}"


class Clientes:
    lista = []

    def __init__(self, lista):
        self.lista = lista
    
    def __str__(self):
        for cliente in self.lista:
            print(cliente)

    @staticmethod
    def buscar(dni):
        for cliente in Clientes.lista:
            if cliente.dni == dni:
                return cliente
        return None
    
    @staticmethod
    def crear(dni, nombre, apellido):
        cliente = Cliente(dni, nombre, apellido)
        Clientes.lista.append(cliente)
        return cliente
    
    @staticmethod
    def modificar(dni, nombre, apellido):
        cliente = Clientes.buscar(dni)
        cliente.nombre = nombre
        cliente.apellido = apellido
        return cliente
    
    @staticmethod
    def eliminar(dni):
        cliente = Clientes.buscar(dni)
        Clientes.lista.remove(cliente)
        return cliente
