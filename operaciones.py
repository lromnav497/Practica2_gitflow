# operaciones.py
def sumar(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    else:
        print("Ambos parámetros deben ser int o float")

def restar(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a - b
    else:
        print("Ambos parámetros deben ser int o float")

def multiplicar(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        resultado = 0
        for _ in range(int(b)):
            resultado += a
        return resultado
    else:
        print("Ambos parámetros deben ser int o float")

# Función para dividir dos números sin usar el operador "/"
def dividir(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Ambos parámetros deben ser de tipo int o float")
    if b == 0:
        raise ValueError("No se puede dividir por cero")

    resultado = 0
    resto = abs(a)
    divisor = abs(b)

    # Restamos el divisor del dividendo hasta que el dividendo sea menor que el divisor
    while resto >= divisor:
        resto -= divisor
        resultado += 1

    # Si el divisor o el dividendo son negativos, el resultado debe ser negativo
    if (a < 0) != (b < 0):  # Si uno de los números es negativo
        resultado = -resultado

    return resultado


def factorial_iterativo(n):
    if not isinstance(n, int):  # Comprobar que el valor es un entero
        raise ValueError("El valor debe ser un número entero.")
    if n < 0:
        raise ValueError("El número no puede ser negativo.")
    
    resultado = 1
    for i in range(1, n + 1):  # Calcular el factorial de forma iterativa
        resultado *= i
    return resultado
