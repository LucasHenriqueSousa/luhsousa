gamesTuple = ('Fifa 23', 'Red Dead 2' , 'Star Wars', 
              'Mario Odyssey', 'The legend of Zelda')
print(gamesTuple)
print(type(gamesTuple))

# name = ('Lucas',)
# print(type(name))

# -Nao podemos adicionar valores na tupla
# - Nao podemos remover valores na Tupla
# - Nao podemos ordenar valores na tupla

# 1 - Buscar os dois primeiros itens da tupla
print(gamesTuple[:2])

 # 2 - Buscar os dois itens da lista
print(gamesTuple[-1])

# 3 - Buscar jogos ate uma determinada posicao
print(gamesTuple[:3])

#4 - Buscar jogos de uma posicao em diante
print(gamesTuple[2:])

#5 - Recuperar um item da tupla pelo indice
print(gamesTuple.index('Red Dead 2'))