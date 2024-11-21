#JOGO DO TOM E MEGAM

def expert(a, b):
    if a > b:
        print('mais esperto = tom')
    elif a < b:    
        print('mais esperto = megan')
    else:
         print('mais esperto = empate')
def soma(x,y):
    b = x+y
    return(b)    
def mult(x,y):
    b = x*y
    return(b)    
def sub(x,y):
    b = x-y
    return(b)    
def div(x,y):
    b = x//y
    return(b)
operadores = {
    '+':soma,        
    '*':mult,
    '-':sub,
    '/':div
}
tom = 0
megan = 0
i = int(input())
while 1 <= i <= 1000:
    entrada = input()
    separador_str = entrada.split()        
    nome = separador_str[0]
    operando = int(separador_str[1])
    operador = separador_str[2]
    operando1 = int(separador_str[3])
    resposta = int(input())
    resultado_correto = operadores[operador](operando, operando1)
    
    if  nome == 'tom' and resposta == resultado_correto:
        megan += 1
    elif nome == 'megan' and resposta == resultado_correto:
        tom +=1
    elif nome == 'tom' and resposta != resultado_correto:
        megan -= 1
    elif nome == 'megan' and resposta != resultado_correto:
        tom -=1
    else:
        print()
    i -= 1
print(f'megan = {megan}')
print(f'tom = {tom}')
expert(tom, megan)


#invista!

def porcent(a, b):
    porcentagem = ((a/100)*b)+b
    return(porcentagem)
investidor = input()    
separador_str = investidor.split()
valor_salario = float(separador_str[0])
meses_strg = int(float(separador_str[1]))
retorno_investimento = float(separador_str[2])
corretora = input()    
separador_str2 = corretora.split()
valor_corretora = float(separador_str2[0])
meses_strg2 = int(float(separador_str2[1]))
percent_investimento = float(separador_str2[2])

if valor_corretora <= valor_salario and meses_strg2 <= meses_strg and retorno_investimento <= porcent(percent_investimento, valor_salario):
    print('invista!')
else:
    print('nao invista!')

# BONIFICACAO
def aumenta(a, b):
    return a + b
def reduz(a, b):
    return a - b
operador = {'aumenta': aumenta,'reduz': reduz}
nomes = {}
repetir = int(input())
while repetir > 0:
    entrada = input()
    nomes_str = entrada.split()
    nomes[nomes_str[0]] = float(nomes_str[1])
    repetir -= 1
a = ''    
while a != 'FIM':
    a = input() 
    if a != 'FIM': 
        separador = a.split()
        operadores = separador[0]
        valor = float(separador[1])        
        nome = separador[2]
        if nome in nomes:
            valor2 = nomes[nome]
            nomes[nome] = operador[operadores](valor2, valor)
    if a == 'FIM':
        
        for chave in sorted(nomes.keys()):
            if nomes[chave] < 0:
                nomes[chave] = 0
            print(f'Nome: {chave}')    
            print(f'Bonificacao: R$ {nomes[chave]:.2f}')
            print('--------------------')
#%%            
# Quantas Estrelas
N = int(input())
a = 1
if 1 <= N <= 50000:
    while N > 1:
        a += N
        N -= 1

print(f'Teremos {a} estrelas!')

#%%
# DATA IMPAR OU PAR
data = input()
separador = data.split('/')
dia = int(separador[0])
mes = int(separador[1])
ano = int(separador[2])
soma = dia + mes + ano
if soma %2 == 0: # type: ignore
    print('par')
else:
    print('impar')
# %%
def interseccao(a,b):
    conjunto = []
    for elemento in a:        
        if elemento in b:            
            conjunto.append(elemento)    
    return conjunto
a = [1,2,3,4,5,9]
b = [4,5,6,7,8]

print(interseccao(a,b))

# %%
def uniao(a,b):
    conjunto = a
    for elemento2 in b:
        if elemento2 not in conjunto:
            conjunto.append(elemento2)    
    return conjunto
a = [1,2,3,4,5,9]
b = [1,2,3,4,5,6,7,8,9]

print(uniao(a,b))
# %%
import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn3 # type: ignore

# Exemplo para um diagrama de Venn de dois conjuntos
def plot_venn2():
    # Definindo os tamanhos dos conjuntos e suas interseções
    set1_size = 10
    set2_size = 5
    intersection_size = 3

    # Criando o diagrama de Venn
    venn2(subsets=(set1_size, set2_size, intersection_size),
          set_labels=('Set 1', 'Set 2'))
    
    plt.title("Diagrama de Venn de Dois Conjuntos")
    plt.show()

# Exemplo para um diagrama de Venn de três conjuntos
def plot_venn3():
    # Definindo os tamanhos dos conjuntos e suas interseções
    set1_size = 10
    set2_size = 8
    set3_size = 6
    intersection_12 = 4
    intersection_13 = 3
    intersection_23 = 2
    intersection_123 = 1

    # Criando o diagrama de Venn
    venn3(subsets=(set1_size, set2_size, set3_size, intersection_12, intersection_13, intersection_23, intersection_123),
          set_labels=('Set 1', 'Set 2', 'Set 3'))
    
    plt.title("Diagrama de Venn de Três Conjuntos")
    plt.show()

# Plotando os diagramas
plot_venn2()
plot_venn3()

# %%
import time

# Espera ativa por uma condição externa
start_time = time.time()
timeout = 10  # segundos
condition_met = False

while not condition_met:
    # Simular condição externa sendo satisfeita
    if time.time() - start_time > 5:
        condition_met = True
    
    print("Esperando a condição ser satisfeita...")
    time.sleep(1)  # Espera 1 segundo antes de checar novamente

print("Condição satisfeita!")

# %%
