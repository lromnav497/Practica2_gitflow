def factorial_recursivo(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("El valor debe ser un entero no negativo")
    if n == 0:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

def sumar(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    else:
        raise ValueError("Ambos parámetros deben ser int o float")

def restar(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a - b
    else:
        raise ValueError("Ambos parámetros deben ser int o float")

def multiplicar(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        resultado = 0
        for _ in range(int(b)):
            resultado += a
        return resultado
    else:
        raise ValueError("Ambos parámetros deben ser int o float")

def dividir(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Ambos parámetros deben ser de tipo int o float")
    if b == 0:
        raise ValueError("No se puede dividir por cero")

    resultado = 0
    resto = abs(a)
    divisor = abs(b)

    while resto >= divisor:
        resto -= divisor
        resultado += 1

    if (a < 0) != (b < 0):
        resultado = -resultado

    return resultado

def factorial_iterativo(n):
    if not isinstance(n, int):
        raise ValueError("El valor debe ser un número entero.")
    if n < 0:
        raise ValueError("El número no puede ser negativo.")
    
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def fibonacci(n):
    if not isinstance(n, int):
        raise ValueError("El valor debe ser un entero.")
    if n < 0:
        raise ValueError("El valor debe ser un entero no negativo.")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
