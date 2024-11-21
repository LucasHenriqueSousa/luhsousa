name = input("Digite o nome do jogo\n")
yaerLaunch = int(input("digite o ano de lancamento do jogo\n"))
gamePrice = float(input("DIGITE O valor do jogo\n"))
planIncluided = (input("Esta incluido no servico mensal\n"))

print("###Dados fo Jogo###")
print("==================")
# Alternativa 1
# print("Nome do jogo:", name)
# print("Ano do jogo:", yaerLaunch)
# print("Preco do Jogo:", gamePrice)
# print("Está incluído no plano?:", planIncluided)

# # Alternativa 2 
# print("Nome do Jogo:", name, "\nAno de lancamento:", yaerLaunch ,
#       "\nPreco do Jogo:", gamePrice, "\nEsta incluso no servico?", planIncluided)

# Alternativa 3
print(f"Nome do jogo: {name}    \nAno de lancamento: {yaerLaunch}   \n Preco do Jogo: {gamePrice} \nEsta incluso no servico?: {planIncluided}")