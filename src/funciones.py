def factorial(n):
    """Calcula el factorial de un número entero no negativo"""
    if not isinstance(n, int):
        raise TypeError("El número debe ser un entero")
    
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")
    
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    
    return resultado

