# main.py

from operaciones import sumar, restar, multiplicar, dividir

def main():
    # Ejemplo de uso de las funciones
    try:
        num1 = 10
        num2 = 5

        print("Suma:", sumar(num1, num2))
        print("Resta:", restar(num1, num2))
        print("Multiplicación:", multiplicar(num1, num2))
        print("División:", dividir(num1, num2))  # Llamada a la nueva función

    except ValueError as e:
        print(f"Error: {e}")

from menu import mostrar_menu

def main():
    opcion, numero = mostrar_menu()
    if opcion:
        print(f"Has seleccionado la opción {opcion} y el número {numero}")


if __name__ == "__main__":
    main()
