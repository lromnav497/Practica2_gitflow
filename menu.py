from operaciones import sumar, restar, multiplicar, dividir, factorial_recursivo, fibonacci

def mostrar_menu():
    print("Seleccione una opción:")
    print("1 - Sumar")
    print("2 - Restar")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Salir")
    print("6 - Calcular el factorial de un número (recursivo)")
    print("7 - Calcular el fibonacci de un número (iterativo)")

    # Pedir al usuario que elija una opción
    opcion = input("Ingrese una opción (1-7): ")
    
    # Validar que la opción esté en el rango esperado
    if opcion not in ['1', '2', '3', '4', '5', '6', '7']:
        print("Opción inválida. Por favor, ingrese un número entre 1 y 7.")
        return None, None, None
    
    # Pedir al usuario dos números
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: ")) if opcion not in ['6', '7'] else None
    
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
    elif opcion == '7':
        try:
            resultado = fibonacci(int(numero1))
            print(f"Resultado de calcular el fibonacci iterativo: {resultado}")
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
