import re
import os
import platform

def limpiar_pantalla():
    os.system('cls') if platform.system() == 'Windows' else os.system('clear')

def leer_texto(min_len = 0, max_len = 100, mensaje = None):
    print(mensaje) if mensaje else None
    while True:
        texto = input('> ')
        if min_len <= len(texto) <= max_len:
            return texto

def validar_dni(dni, lista):
    if not re.match('[0-9]{3}$', dni): return False
    for cliente in lista:
        if cliente.dni == dni: return False
    return True