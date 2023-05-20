import os
import time
import helpers
import database as db
menu = '''
-----------------------------------
-------Bienvenido al gestor--------
-----------------------------------
[1] Listar los clientes
[2] Buscar un cliente
[3] Añadir un cliente
[4] Modificar un cliente
[5] Borrar un cliente
[6] Salir
'''
def iniciar():
    while True:
        helpers.limpiar_pantalla()
        print(menu)
        opcion = input('> ')
        #Opciones
        helpers.limpiar_pantalla()
        if opcion == '1':
            print('Listando los clientes...')
            for cliente in db.Clientes.lista:
                print(cliente)
        elif opcion == '2':
            dni = helpers.leer_texto(min_len=3, max_len=3, mensaje= 'DNI (3 dígitos)')
            cliente = db.Clientes.buscar(dni)
            print(cliente) if cliente else print('Cliente no existe') 
        elif opcion == '3':
            dni = helpers.leer_texto(min_len=3, max_len=3, mensaje= 'DNI (3 digitos)')
            nombre = helpers.leer_texto(min_len=2, max_len=30, mensaje= 'Nombre (2 a 30 chars)').capitalize()
            apellido = helpers.leer_texto(min_len=2, max_len=30, mensaje= 'Apellido (2 a 30 chars)').capitalize()
            print(db.Clientes.crear(dni, nombre, apellido).__str__() + ' creado')
        elif opcion == '4':
            dni = helpers.leer_texto(min_len=3, max_len=3, mensaje= 'DNI (3 digitos)')
            c = db.Clientes.buscar(dni)
            if c:
                nombre = helpers.leer_texto(min_len=2, max_len=30, mensaje= f'Nombre (2 a 30 chars) [{c.nombre}]').capitalize()
                apellido = helpers.leer_texto(min_len=2, max_len=30, mensaje= f'Apellido (2 a 30 chars) [{c.apellido}]').capitalize()
                print(db.Clientes.modificar(dni, nombre, apellido).__str__() +' modificado')
            else:
                print('Cliente no existe')
        elif opcion == '5':
            dni = helpers.leer_texto(min_len=3, max_len=3, mensaje= 'DNI (3 digitos)')
            print(db.Clientes.eliminar(dni).__str__() +' borrado') if db.Clientes.buscar(dni) else print('Cliente no existe')
        elif opcion == '6':
            print('Adios...')
            time.sleep(1)
            break
        else:
            print('Opcion no valida')
        input('Presiona enter para continuar...')