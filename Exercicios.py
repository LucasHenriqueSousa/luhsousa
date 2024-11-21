''''  
1 -
Escreva um programa que cria dois conjuntos: um com os números pares entre 1 e 10,
e outro com os números ímpares entre 1 e 10. Então, encontre a união, interseção e
diferença entre esses dois conjuntos. O programa deve apresentar um menu em que o
usuário escolha a opção desejada.

'''

#%%
menu = int(input('Escolha uma das opções. 1 - unição \n 2 - Intersecção  \n 3 - Diferença A e B  \n 4 - Diferença de B e A \n' ))
a = {2, 4, 6, 8, 10}
b = {1, 3, 5, 7, 9}
print(f'Conjunto A = {a}\n')
print(f'Conjunto B = {b}\n')
if menu < 5:
    if menu == 1:
        
        r = a.union(b) 
        print(f'{r} Está é a União dos conjuntos')
        
    elif menu == 2:
        r = a.intersection(b)
        print(f'{r} Está é a Intersecção dos conjuntos A e B')
        
    elif menu == 4:
        r = b.difference(a)
        print(f'{r} Está é a Diferença dos conjuntos B e A')
    else:
        r = a.difference(b)
        print(f'{r} Está é a Diferença dos conjuntos')
else:
    print('Está opção não é valida.')
    
    
    
    
    
    
# %%
'''
2 - 

Escreva um programa que cria três conjuntos: um com nomes de frutas, outro com
nomes de verduras e um terceiro com nomes de laticínios. Em seguida, encontre a
interseção entre o conjunto de frutas e verduras, a diferença entre o conjunto de frutas
e laticínios, e a união de todos os três conjuntos. O programa deve obrigatoriamente
apresentar um menu em que o usuário escolha a opção desejada.

'''

frutas = {'Maçã', 'Banana', 'Pera', 'Uva'}
verduras = {'Rúcula', 'Alface', 'Agrião', 'Salsinha'}
lacticínos = {'Queijo', 'Iorgute', 'Leite Fermentado', 'Danone'}

conjuntos = {
    1: frutas,    
    2: verduras,
    3: lacticínos
}
nomes_conjuntos = {
    1: '*Frutas',    
    2: '*Verduras',
    3: '*Lacticínos'
}
menu = int(input(' Escolha uma opção abaixo \n  1 - União. \n  2 - Intersecção. \n  3 - diferença. \n'))

print(f' Conjuntos de Frutas = {frutas} \n Conjuntos de Verduras = {verduras} \n Conjuntos de Lacticínios = {lacticínos} \n ')

if menu < 4:
    x = int(input(' Escolha uma opção para fazer a operação desejada abaixo. \n  1 - Frutas. \n  2 - Verduras. \n  3 - Lacticínios. \n'))
    y = int(input(' Escolha uma opção para fazer a operação desejada abaixo. \n  1 - Frutas. \n  2 - Verduras. \n  3 - Lacticínios. \n'))
    conjunto_x = conjuntos.get(x)
    conjunto_y = conjuntos.get(y)
    if menu == 1 and x < 4 and y < 4:
        resposta = conjunto_x.union(conjunto_y)
        print(f'A União de {nomes_conjuntos.get(x)} com {nomes_conjuntos.get(y)} que será = {resposta} ')
    elif menu == 2 and x < 4 and y < 4:
        resposta = conjunto_x.intersection(conjunto_y)
        print(f'A Intersecção de {nomes_conjuntos.get(x)} com {nomes_conjuntos.get(y)} que será = {resposta} ')
    elif menu == 3 and x < 4 and y < 4:
        resposta = conjunto_x.difference(conjunto_y)
        print(f'A Diferença de {nomes_conjuntos.get(x)} com {nomes_conjuntos.get(y)} que será = {dict(sorted(resposta))} ')    
    else:
        print('Essa Opção não é valida.')
          
    
# %%
'''
3. Escreva um programa que recebe uma lista de números e retorna o maior e o menor
valor da lista. Use função.
'''
def maior_menor(a):    
    maior = max(a)
    menor = min(a)
    return maior, menor
lista = []
while True:
    x = input('DIGITE UM NUMERO PARA ADICIONAR A LISTA.\n SE QUISER PARA DIGITE PARE\n')
    
    if x.lower() == 'pare':
        break
    
    try:
        numero = int(x) 
        lista.append(numero)
            
    except ValueError:
        print("Por favor, digite um número válido ou 'PARE' para encerrar.")
    
try:    
    maior, menor = maior_menor(lista)
except ValueError:
    print('Sua lista esta vazia')
   
print(lista, '\n')

try:
    print(f'\n Seu maior numero e {maior}, e seu menor numero e {menor}')
except NameError:
   print('Sua lista esta vazia')

# %%
'''
4 - Escreva um programa que recebe uma lista e retorna uma nova lista com os elementos
invertidos. Use função.

'''
def inverter(a):
    return a[::-1]

numeros = input('digite uma sequencia de numeros')
x = list(map(int, numeros.split()))

print(f'Lista sem inversão = {x} \n  Lista invertida = {inverter(x)}')

# %%
