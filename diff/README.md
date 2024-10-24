# Máquina Diferencial

__Objetivo:__ (80) Fazer a máquina responder ao próximo valor de entrada da sequência que foi inserida para um polinômio de qualquer grau: encontrar o próximo valor da sequência utilizando a tabela para um polinômio de qualquer grau.

### Tecnologias Usadas 🔧

- Python

## Implementação

A função babbage() cria a tabela de diferenças automaticamente, e conforme a tabela aumenta, ela encontra os níveis correspondentes até que as diferenças se tornem constantes. A tabela de diferenças captura o comportamento de polinômios de qualquer grau, conforme este aumenta, mais níveis de diferenças são gerados.

```
def babbage(eixo_y):
    n = len(eixo_y)
    tabela = [eixo_y]
    for i in range(n - 1):
        linha = []
        for j in range(n - i - 1):
            v = round(tabela[i][j + 1] - tabela[i][j], 2)
            linha.append(v)
        tabela.append(linha)
    return tabela

```

A função "proximo_valor()" pega a última coluna da tabela de diferenças (mais à direita), que representa a diferença mais refinada, e acumula essas diferenças para calcular o próximo valor do polinômio.

"prox_valor" é inicialmente definido como o último valor da primeira linha da tabela de diferenças (que é o valor atual do polinômio para o último valor de x). Em seguida, ele adiciona as diferenças de cada nível subsequente para prever o próximo valor.

```
def proximo_valor(tabela):
    prox_valor = tabela[0][-1]
    for i in range(1, len(tabela)):
        prox_valor += tabela[i][-1]
    return round(prox_valor, 2)
```

A função polinomio() aceita coeficientes para polinômios de qualquer grau e calcula os valores de y para cada valor de x usando a fórmula do polinômio.

O código é feito para funcionar para qualquer grau, basta alterar a lista de coeficientes. Para um polinômio de grau 2, dado no exemplo, os coeficientes podem ser [2, -3, 2], representando 
__2𝑥² −3𝑥 +2__.

```
def polinomio(x, coeficientes):
    grau = len(coeficientes) - 1
    soma = 0
    for i in range(grau + 1):
        soma += coeficientes[i] * (x ** (grau - i))
    return round(soma, 2)

```

### Autora

- [@MelissaOliveiraC](https://github.com/MelissaOliveiraC)