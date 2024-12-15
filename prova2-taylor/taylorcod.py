import math

def calcular_ex_taylor(x, n):
    """
    Calcula e^x utilizando a série de Taylor com n termos.
    :param x: Valor de x
    :param n: Número de termos da série
    :return: Aproximação de e^x
    """
    resultado = 0
    for i in range(n):
        resultado += (x ** i) / math.factorial(i)
    return resultado

def calcular_ex_negativo(x, n):
    """
    Calcula e^x para valores negativos de x de duas formas:
    - Usando diretamente x na série de Taylor
    - Transformando y = -x e usando 1/e^x
    :param x: Valor de x (negativo)
    :param n: Número de termos da série
    :return: Tupla com (resultado direto, resultado 1/e^x)
    """
    # Usando x diretamente
    resultado_direto = calcular_ex_taylor(x, n)

    # Usando y = -x e calculando 1/e^x
    y = -x
    resultado_inverso = 1 / calcular_ex_taylor(y, n)

    return resultado_direto, resultado_inverso

if __name__ == "__main__":
    print("Cálculo de e^x utilizando a série de Taylor")

    # Entrada de valores
    x = float(input("Digite o valor de x: "))
    n = int(input("Digite o número de termos da série (n): "))

    # Verifica se x é negativo ou positivo
    if x >= 0:
        resultado = calcular_ex_taylor(x, n)
        print(f"O valor aproximado de e^{x} com {n} termos é: {resultado}")
    else:
        resultado_direto, resultado_inverso = calcular_ex_negativo(x, n)
        print(f"O valor aproximado de e^{x} com {n} termos (usando x diretamente) é: {resultado_direto}")
        print(f"O valor aproximado de e^{x} com {n} termos (usando 1/e^x) é: {resultado_inverso}")