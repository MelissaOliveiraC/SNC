def babbage(eixo_y):
    n = len(eixo_y)
    tabela = [eixo_y]
    for i in range(n - 1):
        linha = []
        for j in range(n - i - 1):
            v = round(tabela[i][j + 1] - tabela[i][j], 2) # modificação: uso do round controlar o número de casas decimais (2).
            linha.append(v)
        tabela.append(linha)
    return tabela

# modificações: o grau do polinômio é calculado automaticamente com base no número de coeficientes fornecidos.
def polinomio(x, coeficientes):
    grau = len(coeficientes) - 1
    soma = 0
    for i in range(grau + 1): # percorre desde o termo de maior grau até o termo const
        soma += coeficientes[i] * (x ** (grau - i))
    return round(soma, 2)

# Acha próx valor da seq (NOVO)
def proximo_valor(tabela):
    prox_valor = tabela[0][-1] # pega o último valor do Nível 1 da tab-diff
    for i in range(1, len(tabela)): # percorre os níveis restantes da tab-diff e [...]
        prox_valor += tabela[i][-1] # soma últimos valores de cada nível ao prox_valor
    return round(prox_valor, 2)

# Exemplo de coeficientes para um polinômio de grau 2: 2x^2 - 3x + 2
coeficientes = [2, -3, 2]
# Valores de x em intervalos regulares de 0.1
eixo_x = [round(i * 0.1, 2) for i in range(5)]  # modificações: valores de x em intervalos (0.0 a 0.4)
eixo_y = [polinomio(x, coeficientes) for x in eixo_x] 

# Gerar tabela de diff
diffs = babbage(eixo_y)

# Resultados
print("Eixo X:", eixo_x)
print("Eixo Y:", eixo_y)
print("Tabela de diferenças:")
for c, linha in enumerate(diffs):
    print(f"Nível {c}: {linha}")

# Próximo valor da sequência (NOVO)
prox_valor = proximo_valor(diffs)
print(f"\nPróximo valor de y para x = {eixo_x[-1] + 0.1}: {prox_valor}")
print("\n")


# ---------------------------------
# testes para o polinômio de 3 grau
# 1x^3 - 2x^2 + 3x + 4
# coeficientes = [1, -2, 3, 4]
# eixo_x = [0, 0.1, 0.2, 0.3, 0.4]