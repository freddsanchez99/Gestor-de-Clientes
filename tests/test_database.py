import unittest
import database as db

class TestDatabase(unittest.TestCase):

    def setUp(self):
        db.Clientes.lista = [
            db.Cliente(dni= '123', nombre= 'Luis', apellidos= 'Sanchez'),
            db.Cliente(dni= '456',nombre= 'Lu', apellidos= 'Alarcon'),
            db.Cliente( dni= '789', nombre= 'Pau',apellidos= 'Crespo')
        ]