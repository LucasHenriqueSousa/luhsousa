'''import numpy as np

def calcular_determinante():
    matriz = []
    for i in range(3):
        linha = []
        for j in range(3):
            valor = float(input(f"Insira o valor para a posição [{i+1},{j+1}]: "))
            linha.append(valor)
        matriz.append(linha)
    matriz = np.array(matriz)
    return np.linalg.det(matriz)

# Exemplo de uso
print("O determinante da matriz é: ", calcular_determinante())
'''
'''
import numpy as np

def calcular_inversa():
    matriz = []
    for i in range(3):
        linha = []
        for j in range(3):
            valor = float(input(f"Insira o valor para a posição [{i+1},{j+1}]: "))
            linha.append(valor)
        matriz.append(linha)
    matriz = np.array(matriz)
    return np.linalg.inv(matriz)

# Exemplo de uso
print("A inversa da matriz é: \n", calcular_inversa())
'''
'''
import numpy as np

def multiplicar_matrizes():
    # Solicita ao usuário as dimensões das matrizes
    linhas_matriz1 = int(input("Insira o número de linhas da primeira matriz: "))
    colunas_matriz1 = int(input("Insira o número de colunas da primeira matriz: "))
    linhas_matriz2 = int(input("Insira o número de linhas da segunda matriz: "))
    colunas_matriz2 = int(input("Insira o número de colunas da segunda matriz: "))

    # Verifica se a multiplicação é possível
    if colunas_matriz1 != linhas_matriz2:
        return "A multiplicação dessas matrizes não é possível."

    # Solicita ao usuário os valores das matrizes
    matriz1 = []
    for i in range(linhas_matriz1):
        linha = []
        for j in range(colunas_matriz1):
            valor = float(input(f"Insira o valor para a posição [{i+1},{j+1}] da primeira matriz: "))
            linha.append(valor)
        matriz1.append(linha)

    matriz2 = []
    for i in range(linhas_matriz2):
        linha = []
        for j in range(colunas_matriz2):
            valor = float(input(f"Insira o valor para a posição [{i+1},{j+1}] da segunda matriz: "))
            linha.append(valor)
        matriz2.append(linha)

    # Converte as listas para arrays numpy
    matriz1 = np.array(matriz1)
    matriz2 = np.array(matriz2)

    # Calcula e retorna o produto das matrizes
    return np.dot(matriz1, matriz2)

# Exemplo de uso
print("O produto das matrizes é: \n", multiplicar_matrizes())
''''''
import sympy 
def resolver_sistema():
    # Solicita ao usuário os coeficientes e constantes das equações
    coef1 = [float(input(f"Insira o coeficiente {i+1} da primeira equação: ")) for i in range(3)]
    coef2 = [float(input(f"Insira o coeficiente {i+1} da segunda equação: ")) for i in range(3)]

    # Define as equações
    equacao1 = {'x': coef1[0], 'y': coef1[1], 'const': coef1[2]}
    equacao2 = {'x': coef2[0], 'y': coef2[1], 'const': coef2[2]}

    # Solicita ao usuário a operação
    operacao = input("Insira a operação (adição ou subtração): ")

    # Verifica se a operação é uma adição ou subtração
    if operacao.lower() == "adição":
        equacao_resultante = {key: equacao1[key] - equacao2[key] for key in equacao1}
    elif operacao.lower() == "subtração":
        equacao_resultante = {key: equacao1[key] + equacao2[key] for key in equacao1}
    else:
        return "A operação deve ser uma adição ou subtração."

    # Retorna a equação resultante
    return f"{equacao_resultante['x']}x + {equacao_resultante['y']}y = {equacao_resultante['const']}"

# Exemplo de uso
print("A equação resultante é: ", resolver_sistema())
'''

