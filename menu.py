# menu.py
def mostrar_menu():
    print("Seleccione una opción:")
    print("1- Sumar")
    print("2- Restar")
    print("3- Multiplicar")
    print("4- Dividir")
    print("5- Salir")
    
    # Pedir al usuario que elija una opción
    opcion = input("Ingrese una opción (1-5): ")
    
    # Validar que la opción esté en el rango esperado
    if opcion not in ['1', '2', '3', '4', '5']:
        print("Opción inválida. Por favor, ingrese un número entre 1 y 5.")
        return None
    
    # Pedir al usuario un número
    numero = float(input("Ingrese un número: "))
    
    return opcion, numero
