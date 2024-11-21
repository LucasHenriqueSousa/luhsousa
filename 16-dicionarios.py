#%%
gameFifa = {
    "name":"Fifa 23",
    "yearLaunch": 2022,
    "gamePrice": 90.50,
    "classification": 8.5,
    "genre": ["Esporte", "Familia"]
}
print(gameFifa)
print(len(gameFifa))
print(type(gameFifa))

# recuperar um elemento no dicionario.
print(gameFifa['genre'])
print(gameFifa.get('classification'))

# 2 - Buscar apenas as chaves do dicionario
print(gameFifa.keys())

# 3 - buscar apenas os valores do dicionario
print(gameFifa.values())

# 4 - buscar itens do dioconario com chave e valor
print(gameFifa.items())
 
# 5 - Adiconar itens no dicionario
gameFifa['players'] = 2
print(gameFifa)

# 6 - Atualizar iten no dicionario
gameFifa.update({"players": 1})
print(gameFifa)

# 7 - remover itens do dicionario.
gameFifa.pop("players")
print(gameFifa)

# %%
NT = float(input())
PR = float(input())
 
if (NT/2)+(PR/2) >= 6:
    print('aprovado')
elif ((NT/2) >= 2 or (PR/2) >= 0) and (((NT/2)+(PR/2) < 6) and ((NT/2)+(PR/2) > 2) and (NT > 2)):
    print('talvez com a sub')
else:
    print('reprovado')
# %%
n = int(input())
i=1
while i <= 10:
    x = i * n
    print(f'{n} x {i} = {x}')
    i += 1

# %%
def desenhar_triangulo_alfabetico(N):
    if 1 <= N <= 26:
        for i in range(N):
            char = chr(ord('A') + i)
            print(char * (i + 1))
N = int(input())
desenhar_triangulo_alfabetico(N)
# %%
def main():
    vcoin_to_brl = 2.50  
    total_vcoin = 0.0
    total_brl = 0.0

    while True:
        donation = float(input())
        if donation == -1.0:
            break
        total_vcoin += donation
        total_brl += donation * vcoin_to_brl

    print(f"VC$ {total_vcoin:.2f}")
    print(f"R$ {total_brl:.2f}")
main()

# %%

# %%
def eh_bissexto(ano):
    return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)

def anos_bissextos_no_intervalo(INICIO, FIM):
    anos_bissextos = []
    for ano in range(INICIO, FIM + 1):
        if eh_bissexto(ano):
            anos_bissextos.append(ano)
            print(ano)
    print("bissextos:", len(anos_bissextos))
INICIO = int(input())
FIM = int(input())
anos_bissextos_no_intervalo(INICIO, FIM)



# %%
def segunda_chance(n):
    if 1 <= n <= 999:         
        notas_original = []
        for _ in range(n): 
            notas_original.append(float(input()))                        
            print(f'-({len(notas_original):03d}) {notas_original} ')f33333333333333333333333333333333333
        notas_final = []         
        for _ in range(n):            
            notas_final.append(float(input()))
            print(f'*({len(notas_final):03d})')
n = int(input())                
segunda_chance(n)    
# %%
def calcular_nota_final(nota_original, nota_segunda_chance):
   
    if nota_segunda_chance == 10:
         nota_final = nota_original + 2 
     
    else: 
        nota_final = nota_segunda_chance
    
    return min(nota_final, 10)

def processar_notas_alunos(N, notas_originais, notas_segunda_chance):
    notas_alteradas = 0
    for i in range(N):
        nota_original = notas_originais[i]
        nota_segunda_chance = notas_segunda_chance[i]
        nota_final = calcular_nota_final(nota_original, nota_segunda_chance)
        
        # Verifica se a nota foi alterada
        if nota_final != nota_original:
            notas_alteradas += 1
            print(f"*{(i+1):03d} original: {nota_original:05.2f} | final: {nota_final:05.2f}")
        else:
            print(f"-{(i+1):03d} original: {nota_original:05.2f} | final: {nota_final:05.2f}")

    # Exibe a quantidade de notas alteradas
    print(f"NOTAS ALTERADAS: {notas_alteradas}")

# Leitura dos dados de entrada
N = int(input())
notas_originais = [float(input()) for _ in range(N)]
notas_segunda_chance = [float(input()) for _ in range(N)]

# Processamento e exibição das notas dos alunos
processar_notas_alunos(N, notas_originais, notas_segunda_chance)

# %%

nomes = []

for _ in range(5):

    nomes.append(input('Nome: '))

qtd = 0

for nome in nomes:

    if nome[0] in ['A','E','I','O','U']:

        qtd += 1

print(f'{qtd} dos nomes começam com vogal')
