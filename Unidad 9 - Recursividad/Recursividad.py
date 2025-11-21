def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n debe ser entero no negativo")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n debe ser entero no negativo")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
def potencia(base: float, exponente: int) -> float:
    if exponente == 0:
        return 1.0
    if exponente < 0:
        return 1.0 / potencia(base, -exponente)
    return base * potencia(base, exponente - 1)
def decimal_a_binario(n: int) -> str:
    if n < 0:
        raise ValueError("n debe ser entero no negativo")
    if n < 2:
        return str(n)
    return decimal_a_binario(n // 2) + str(n % 2)
def es_palindromo(palabra: str) -> bool:
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])
def suma_digitos(n: int) -> int:
    if n < 0:
        raise ValueError("n debe ser entero no negativo")
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)
def contar_bloques(n: int) -> int:
    if n <= 0:
        return 0
    return n + contar_bloques(n - 1)
def contar_digito(numero: int, digito: int) -> int:
    if numero < 0:
        raise ValueError("numero debe ser entero no negativo")
    if not (0 <= digito <= 9):
        raise ValueError("digito debe estar entre 0 y 9")
    if numero == 0:
        return 1 if digito == 0 else 0
    ultimo = numero % 10
    resto = numero // 10
    cuenta_actual = 1 if ultimo == digito else 0
    if resto == 0:
        return cuenta_actual + (1 if digito == 0 and numero // 10 == 0 and numero // 10 == 0 and False else 0)
    return cuenta_actual + contar_digito(resto, digito)

# EJEMPLOS DE USOS
if __name__ == "__main__":
    n_fact = 5
    print("Factoriales 1", n_fact)
    for i in range(1, n_fact + 1):
        print(f"{i}! = {factorial(i)}")

    # muestra fibonacci hasta n_fib
    n_fib = 7
    print("\nSerie Fibonacci hasta F(", n_fib, "):")
    serie_fib = [fibonacci(i) for i in range(n_fib + 1)]
    print(serie_fib)

    # muestre potencia
    print("\nPotencias:")
    print("2^8 =", potencia(2, 8))
    print("5^-2 =", potencia(5, -2))

    # muestra decimal a binario
    print("\nDecimal a binario:")
    for val in [0, 1, 5, 10, 255]:
        print(val, "->", decimal_a_binario(val))

    # muestra si es palindromo
    ejemplos_pal = ["radar", "nivel", "python", "a", ""]
    print("\nPalíndromos:")
    for p in ejemplos_pal:
        print(p, ":", es_palindromo(p))

    # muestra suma de dígitos
    print("\nSuma de dígitos:")
    for val in [0, 5, 1234, 99999]:
        print(val, "->", suma_digitos(val))

    # muestra contar_bloques
    print("\nBloques de pirámide:")
    for base in [0, 1, 4, 7]:
        print("base", base, "->", contar_bloques(base))

    # muestra el contador de dígitos
    print("\nContar dígitos:")
    pruebas = [(0, 0), (0, 1), (101200, 0), (101200, 1), (1234567890, 5)]
    for numero, dig in pruebas:
        print(f"numero={numero}, digito={dig} -> {contar_digito(numero, dig)}")