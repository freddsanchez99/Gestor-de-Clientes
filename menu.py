import os
import time
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
        os.system('cls')
        print(menu)
        opcion = input('> ')
        #Opciones
        os.system('cls')
        if opcion == '1':
            print('Listando los clientes...')
            #TODO: Listar los clientes
        elif opcion == '2':
            print('Buscando al cliente')
            #TODO: Buscar al cliente
        elif opcion == '3':
            print('Añadiendo al cliente...')
            #TODO: Añadir al cliente
        elif opcion == '4':
            print('Modificando al cliente...')
            #TODO: Modificar al cliente
        elif opcion == '5':
            print('Borrando al cliente...')
            #TODO: Borrar al cliente
        elif opcion == '6':
            print('Adios...')
            time.sleep(3)
            break
        else:
            print('Opcion no valida')
        input('Presiona enter para continuar')