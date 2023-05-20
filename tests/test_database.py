import unittest
import database as db

class TestDatabase(unittest.TestCase):
    def setUp(self):
        db.Clientes.lista = [
            db.Cliente('123', 'Luis', 'Sanchez'),
            db.Cliente('456', 'Lu', 'Alarcon'),
            db.Cliente('789', 'Pau', 'Crespo')
        ]
    
    def test_buscar_clientes(self):
        c_exists = db.Clientes.buscar('123')
        c_no_exists = db.Clientes.buscar('124')
        self.assertIsNotNone(c_exists)
        self.assertIsNone(c_no_exists)
    