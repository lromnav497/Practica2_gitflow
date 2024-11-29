from operaciones import sumar, restar, multiplicar, dividir, factorial_recursivo, fibonacci

def mostrar_menu():
    print("Seleccione una opción:")
    print("1 - Sumar")
    print("2 - Restar")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Salir")


    print("6- Calcular el factorial de un número")

    print("6- Calcular el factorial (iterativo)")
    print("7- Calcular el factorial (recursivo)")  # Asegúrate de que esta opción sea 7
    print("8- Calcular el fibonacci de un número (iterativo)")


    print("1- Sumar")
    print("2- Restar")
    print("3- Multiplicar")
    print("4- Dividir")
    print("5- Salir")
    print("6- Calcular el factorial de un número (recursivo)")
    

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

    # Lógica para manejar las opciones
    if opcion == "7":  # Cambiar el número de la opción
        numero = int(input("Introduzca un número para calcular el Factorial Recursivo: "))
        resultado = factorial_recursivo(numero)
        print(f"El factorial recursivo de {numero} es: {resultado}")
    # Aquí seguirían las demás opciones de cálculo...

    if opcion == 1:
        # Sumar

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



    elif opcion == 5:
        print("Saliendo del programa...")
    else:
        print("Opción no válida. Intente nuevamente.")

    if opcion == 6:
        numero = int(input("Ingrese un número para calcular su factorial: "))
        try:
            resultado = factorial_iterativo(numero)
            print(f"El factorial de {numero} es: {resultado}")
        except ValueError as e:
            print(f"Error: {e}")
    else:
        # Aquí iría el código para las otras opciones del menú (1-5)
        pass
    
    return opcion, numero


if __name__ == "__main__":
    while True:
        opcion, numero1, numero2 = mostrar_menu()
        if opcion is None:
            continue
        ejecutar_opcion(opcion, numero1, numero2)
        if opcion == '5':
            break

