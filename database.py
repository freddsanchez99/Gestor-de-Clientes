class Cliente:
    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
    
    def __str__(self):
        return f"{self.dni} -> {self.nombre} {self.apellido}"


class CLientes:
    lista = []

    def __init__(self, lista):
        self.lista = lista
    
    def __str__(self):
        for cliente in self.lista:
            print(cliente)

    @staticmethod
    def buscar(dni):
        for cliente in Cliente.lista:
            if cliente.dni == dni:
                return cliente
        return None
    
    @staticmethod
    def crear(dni, nombre, apellido):
        cliente = Cliente(dni, nombre, apellido)
        Cliente.lista.append(cliente)
        return cliente
    
    @staticmethod
    def modificar(dni, nombre, apellido):
        cliente = Cliente.buscar(dni)
        cliente.nombre = nombre
        cliente.apellido = apellido
        return cliente
    
    @staticmethod
    def eliminar(dni):
        cliente = Cliente.buscar(dni)
        Cliente.lista.remove(cliente)
        return cliente
