from operaciones import sumar, restar, multiplicar, dividir, factorial_recursivo, factorial_iterativo, fibonacci

def mostrar_menu():
    print("Seleccione una opción:")
    print("1 - Sumar")
    print("2 - Restar")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Salir")
    print("6 - Calcular el factorial (iterativo)")
    print("7 - Calcular el factorial (recursivo)")
    print("8 - Calcular el fibonacci de un número (iterativo)")

    # Pedir al usuario que elija una opción
    opcion = input("Ingrese una opción (1-8): ")
    
    # Validar que la opción esté en el rango esperado
    if opcion not in ['1', '2', '3', '4', '5', '6', '7', '8']:
        print("Opción inválida. Por favor, ingrese un número entre 1 y 8.")
        return None, None, None
    
    # Pedir al usuario dos números si la opción no es factorial o fibonacci
    numero1 = float(input("Ingrese el primer número: ")) if opcion not in ['5', '6', '7', '8'] else None
    numero2 = float(input("Ingrese el segundo número: ")) if opcion in ['1', '2', '3', '4'] else None
    
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
        numero = int(input("Ingrese un número para calcular su factorial (iterativo): "))
        try:
            resultado = factorial_iterativo(numero)
            print(f"El factorial iterativo de {numero} es: {resultado}")
        except ValueError as e:
            print(e)
    elif opcion == '7':
        numero = int(input("Ingrese un número para calcular su factorial (recursivo): "))
        try:
            resultado = factorial_recursivo(numero)
            print(f"El factorial recursivo de {numero} es: {resultado}")
        except ValueError as e:
            print(e)
    elif opcion == '8':
        numero = int(input("Ingrese un número para calcular su fibonacci (iterativo): "))
        try:
            resultado = fibonacci(numero)
            print(f"El fibonacci iterativo de {numero} es: {resultado}")
        except ValueError as e:
            print(e)
    elif opcion == '5':
        print("Saliendo del programa...")
        return False  # Indica que el programa debe terminar

    return True  # Indica que el programa debe continuar
