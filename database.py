import config
import csv
class Cliente:
    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
    
    def __str__(self):
        return f"{self.dni} -> {self.nombre} {self.apellido}"


class Clientes:
    lista = []
    with open(config.DATABASE_PATH, newline='\n') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            lista.append(Cliente(row[0], row[1], row[2]))

    @staticmethod
    def guardar():
        with open(config.DATABASE_PATH, 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            for cliente in Clientes.lista:
                writer.writerow((cliente.dni, cliente.nombre, cliente.apellido))
    
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
        Clientes.guardar()
        return cliente
    
    @staticmethod
    def modificar(dni, nombre, apellido):
        cliente = Clientes.buscar(dni)
        cliente.nombre = nombre
        cliente.apellido = apellido
        Clientes.guardar()
        return cliente
    
    @staticmethod
    def eliminar(dni):
        cliente = Clientes.buscar(dni)
        Clientes.lista.remove(cliente)
        Clientes.guardar()
        return cliente

if __name__ == '__main__':
    for cliente in Clientes.lista:
        print(cliente)