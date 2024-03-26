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
