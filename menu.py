# menu.py
from operaciones import sumar, restar, multiplicar, dividir  # Importar la función dividir

def mostrar_menu():
    print("Seleccione una opción:")
    print("1 - Sumar")
    print("2 - Restar")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Salir")

    opcion = input("Ingrese el número de la opción elegida: ")

    try:
        opcion = int(opcion)  # Convertir la opción a un número entero
    except ValueError:
        print("Por favor, ingrese una opción válida (1-5).")
        return

    if opcion == 1:
        # Sumar
        try:
            num1 = float(input("Ingrese el primer valor: "))
            num2 = float(input("Ingrese el segundo valor: "))
            if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
                print("Resultado:", sumar(num1, num2))
            else:
                print("Error: Ambos valores deben ser números (int o float).")
        except ValueError:
            print("Error: Los valores deben ser números.")

    elif opcion == 2:
        # Restar
        try:
            num1 = float(input("Ingrese el primer valor: "))
            num2 = float(input("Ingrese el segundo valor: "))
            if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
                print("Resultado:", restar(num1, num2))
            else:
                print("Error: Ambos valores deben ser números (int o float).")
        except ValueError:
            print("Error: Los valores deben ser números.")

    elif opcion == 3:
        # Multiplicar
        try:
            num1 = float(input("Ingrese el primer valor: "))
            num2 = float(input("Ingrese el segundo valor: "))
            if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
                print("Resultado:", multiplicar(num1, num2))
            else:
                print("Error: Ambos valores deben ser números (int o float).")
        except ValueError:
            print("Error: Los valores deben ser números.")

    elif opcion == 4:
        # Dividir
        try:
            num1 = float(input("Ingrese el primer valor: "))
            num2 = float(input("Ingrese el segundo valor: "))
            if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
                if num2 == 0:
                    print("Error: No se puede dividir entre cero.")
                else:
                    print("Resultado:", dividir(num1, num2))
            else:
                print("Error: Ambos valores deben ser números (int o float).")
        except ValueError:
            print("Error: Los valores deben ser números.")

    elif opcion == 5:
        print("Saliendo del programa...")
    else:
        print("Opción no válida. Intente nuevamente.")
