# main.py
from menu import mostrar_menu, ejecutar_opcion

if __name__ == "__main__":
    while True:
        opcion, numero1, numero2 = mostrar_menu()
        if opcion is None:
            continue
        if not ejecutar_opcion(opcion, numero1, numero2):
            break
