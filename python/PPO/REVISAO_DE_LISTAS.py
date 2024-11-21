#%%


# Criando uma lista de numeros
numeros = [1,2,3,4,5,6,7,8,9]



#%%
# Criando uma lista de filmes TRASH
filmes = ['BorderLands','Panico naFloresta','Çhuky','Sharknado','Piranha','Morbius','Madame Teia']

mista = [29, 'Centopeia Humana', False]

print(filmes[0])
print(numeros[2])
print(mista[-1])


#%%
#Modificando lista

filmes[2] = 'AnnaBelle'
print(filmes)
#%%


#Adicionando um elemento na lista
filmes.append("Ultimo Filme")
print(filmes)

filmes.extend(mista)
print(filmes)

filmes.append(mista)
print(filmes)
# %%


#Removendo um Elemento da lista
mista.remove(False)
print(mista)


# %%
mista.pop(0)
print(mista)



#%%
for num in numeros:
    print(num)


# %%
# Funcao ENUMERATE

for i, numero in enumerate(numeros):
    print(f'indice: {i}, valor: {numero}')
    
# %%
