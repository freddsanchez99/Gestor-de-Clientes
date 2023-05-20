import helpers
import copy
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
    
    def test_crear_clientes(self):
        l_initial = len(db.Clientes.lista)
        n_client = db.Clientes.crear('246', 'Raul', 'Lara')
        self.assertEqual(len(db.Clientes.lista), l_initial + 1)
        self.assertEqual(n_client.dni, '246')
        self.assertEqual(n_client.nombre, 'Raul')
        self.assertEqual(n_client.apellido, 'Lara')
    
    def test_modificar_clientes(self):
        tm_client = copy.copy(db.Clientes.buscar('456'))
        m_client = db.Clientes.modificar('456', 'Lourdes', 'Alarcon')
        self.assertEqual(tm_client.nombre, 'Lu')
        self.assertEqual(m_client.nombre, 'Lourdes')

    def test_eliminar_clientes(self):
        l_initial = len(db.Clientes.lista)
        db.Clientes.eliminar('789')
        self.assertEqual(len(db.Clientes.lista), l_initial - 1)

    def test_validar_dni(self):
        self.assertFalse(helpers.validar_dni('123', db.Clientes.lista))
        self.assertTrue(helpers.validar_dni('124', db.Clientes.lista))
        self.assertFalse(helpers.validar_dni('AAA', db.Clientes.lista))
        self.assertFalse(helpers.validar_dni('098765432123', db.Clientes.lista))