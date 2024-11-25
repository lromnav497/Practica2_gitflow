# main.py
from menu import mostrar_menu

def main():
    opcion, numero = mostrar_menu()
    if opcion:
        print(f"Has seleccionado la opción {opcion} y el número {numero}")

if __name__ == "__main__":
    main()
