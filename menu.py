# menu.py
from operaciones import sumar, restar, multiplicar, dividir, factorial_recursivo

def mostrar_menu():
    print("Seleccione una opción:")
    print("1- Sumar")
    print("2- Restar")
    print("3- Multiplicar")
    print("4- Dividir")
    print("5- Salir")
    print("6- Calcular el factorial de un número (recursivo)")
    
    # Pedir al usuario que elija una opción
    opcion = input("Ingrese una opción (1-6): ")
    
    # Validar que la opción esté en el rango esperado
    if opcion not in ['1', '2', '3', '4', '5', '6']:
        print("Opción inválida. Por favor, ingrese un número entre 1 y 6.")
        return None, None, None
    
    # Pedir al usuario dos números
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: ")) if opcion != '6' else None
    
    return opcion, numero1, numero2

def ejecutar_opcion(opcion, numero1, numero2):
    if opcion == '1':
        try:
            resultado = sumar(numero1, numero2)
            print(f"Resultado de sumar: {resultado}")
        except ValueError as e:
            print(e)
    elif opcion == '2':
        try:
            resultado = restar(numero1, numero2)
            print(f"Resultado de restar: {resultado}")
        except ValueError as e:
            print(e)
    elif opcion == '3':
        try:
            resultado = multiplicar(numero1, numero2)
            print(f"Resultado de multiplicar: {resultado}")
        except ValueError as e:
            print(e)
    elif opcion == '4':
        try:
            resultado = dividir(numero1, numero2)
            print(f"Resultado de dividir: {resultado}")
        except ValueError as e:
            print(e)
    elif opcion == '6':
        try:
            resultado = factorial_recursivo(numero1)
            print(f"Resultado de calcular el factorial recursivo: {resultado}")
        except ValueError as e:
            print(e)
    elif opcion == '5':
        print("Saliendo...")

if __name__ == "__main__":
    while True:
        opcion, numero1, numero2 = mostrar_menu()
        if opcion is None:
            continue
        ejecutar_opcion(opcion, numero1, numero2)
        if opcion == '5':
            break
