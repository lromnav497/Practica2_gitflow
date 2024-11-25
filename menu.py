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

def ejecutar_opcion(opcion, numero):
    if opcion == '1':
        print(f"Resultado de sumar: {numero + numero}")
    elif opcion == '2':
        print(f"Resultado de restar: {numero - numero}")
    elif opcion == '3':
        resultado = 0
        for _ in range(int(numero)):
            resultado += numero
        print(f"Resultado de multiplicar: {resultado}")
    elif opcion == '4':
        if numero == 0:
            print("Error: No se puede dividir por cero.")
        else:
            resultado = 0
            temp = numero
            while temp >= numero:
                temp -= numero
                resultado += 1
            print(f"Resultado de dividir: {resultado}")
    elif opcion == '5':
        print("Saliendo...")

if __name__ == "__main__":
    while True:
        opcion, numero = mostrar_menu()
        if opcion is None:
            continue
        ejecutar_opcion(opcion, numero)
        if opcion == '5':
            break
