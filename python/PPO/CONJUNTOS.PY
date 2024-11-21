#AULA DE QUINTA DIA 15/08/24 (SET)
"""
Conjuntos -> Set
- Coleção: Listas, Tuplas, Dicionários, Conjuntos.
- Não ordenadas;
- Mutáveis;
- Não indexadas;
- Não permitem membros repetidos
Obs: 
lista = []
conjunto = {}
"""
# 1ª Forma

linguagens1 = set(("Python","Java","Pascal","PHP"))
print(f"Valores do 1º set: {linguagens1}")

#2ª Forma
linguagens2 = {"Python","Java","Pascal","Cobol"}
print(f"Valores do 2º set: {linguagens2}")

# Criar um conjunto a partir de outro
linguagens3 = set(linguagens1)
print(f"Valores do set criado a partir de outro: {linguagens3}")

linguagens4 = {"Python","JAVA","Pascal","Cobol","Python","Java"}
print(f"Set com valores únicos: {linguagens4}")

indices = {"A","B","C"}
# print (indices[1]) ERRO

elementos = {"A Lagoa Azul",18,True,"AMO PYTHON"}

for elemento in elementos:
    print(elemento)

print()
print("***** OPERAÇÕES *****")
print()

linguagens_programacao = {"Python", "C#", "Lisp", "Lua"}

if "Lua" in linguagens_programacao:
    print("O elemento buscado está no conjunto")

if "KOBOL" not in linguagens_programacao:
    print("O elemento buscado NÃO está no conjunto")

print(f"Tamanho do set: {len(linguagens_programacao)}")

linguagens_programacao.add("Kobol")
print(f"Set após ADD: {linguagens_programacao}")

linguagens_programacao.update(["Javascript","C++","Ruby"])
print(f"Set após Update: {linguagens_programacao}")

#linguagens_programacao.pop()
#print(f"Exclusão Roleta Russa: {linguagens_programacao}")

linguagens_programacao.remove("Kobol")
print(f"Set após Remove: {linguagens_programacao}")

linguagens_programacao.discard("Javascript")
print(f"Set após Discard: {linguagens_programacao}")

linguagens_programacao.clear()
print(f"Set após Clear: {linguagens_programacao}")

del linguagens_programacao
#print(linguagens_programacao)

linguagens = {"X",1,"Y"}
ling = linguagens.copy()
print(f"Linguagens: {linguagens}")
print(f"Ling: {ling}")



#%%
set1 = {"a", "b" , "c", 1}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(f'Unindo dois conjuntos: {set3}')

set4 = {"a", "b" , "c", 1,3}
set5 = {1, 2, 3}

set6 = set4.intersection(set5)
print(f'Intersecção de dois conjuntos: {set6}')



set3 = set1.difference(set2)
print(f'Elementos do set1 que não há no set2: {set3}')


set4 = set2.difference(set1)
print(f'Elementos do set2 que não há no set1: {set4}')

# %%
