#%%
def busca_linear(lista,valor):
    for elemento in lista:
        if elemento == valor:
            return True
    return False    

lista = [1,2,3,4,5]
print(busca_linear(lista,7))
#%%
t1=[10, 11, 12]
t2=[20, 21, 22]
t3=[30, 31, 32]
t=[t1, t2, t3]

t[1][0]
# %%
alunos = [[5.5, 7.0, 8.7],
          [8.0, 6.0, 9.2],
          [7.8, 8.3, 8.5],
          [0.0, 9.9, 9.1]]
alunos[1][2]
for aluno in alunos:
    print(aluno)
medias = []

for aluno in alunos:
    soma = 0
    for nota in aluno:
        soma += nota
    media = soma / len(aluno)
    medias.append(media)
    print(medias)
# %%
import copy
lista = [[1,2,3], ['a','b','c']]

copia = copy.copy(lista)
copia[0][1] = 5
print(copia,lista)
# %%
'''Crie um programa em Python que recebe duas matrizes e devolve a soma
delas. Lembre-se de validar as dimensões das matrizes antes de realizar a
soma.'''

def soma_matriz(matriz1,matriz2):

    linhas=len(matriz1)
    colunas = len(matriz1[0])
    
    matriz = linhas*[0]
    n = 0
    while n < linhas:
        linha = colunas*[0]    
        matriz[n]=linha 
        m = 0      
        while m < colunas:
            matriz[n][m] = matriz1[n][m] + matriz2[n][m]
            m += 1
        n += 1
    return matriz
    
matriz1 = [[0, 2, 4],
           [6, 8, 10],
           [12, 14 ,16],
           [18, 20, 22]]       
matriz2 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9],
           [10, 11, 12]]

soma_matriz(matriz1,matriz2)
    
# %%
