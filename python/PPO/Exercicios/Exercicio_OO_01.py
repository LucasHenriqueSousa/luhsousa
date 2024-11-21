'''
1. Crie uma classe Produto com as seguintes características:
Atributos:
1. Nome;
2. Estoque;
3. Descrição;
4. Preço.
Métodos:
1. Mostrar nome;
2. Mostrar estoque;
3. Mostrar preço;
4. Mudar nome;
5. Mudar estoque;
6. Mudar descrição;
7. Mudar preço;
8. Sumário (mostrar na tela todos os atributos de instância).
'''

class Produtos:
    def __init__(self, nome, estoque, descricao, preco):
        ''' Atributos '''
        self.Nome = nome   
        self.Estoque = estoque
        self.Descricao = descricao
        self.Preco = preco
    
    def mostrar_nome(self):
        return self.Nome
    def mostrar_preco(self):
        return self.Preco
    def mostrar_estoque(self):
        return self.Estoque
    def mostrar_descricao(self):
        return self.Descricao

    def mudar_nome(self, valor):
        self.Nome = valor
    def mudar_estoque(self, valor):
        self.Estoque = valor
    def mudar_descricao(self, valor):
        self.Descricao = valor
    def mudar_preco(self, valor):
        self.Preco = valor
    def __str__(self): #SUMARIO
        return f"NOME = {self.Nome}\nESTOQUE = {self.Estoque}\nDescrição = {self.Descricao}\nPreço = {self.Preco}"


''' ITENS a serem manipulados '''
item1 = Produtos('Sonho de valsa', 100,'Bombom', 1.99)
item2 = Produtos('Maça', 50, 'Fruta', 4.99)
item3 = Produtos('Coca cola 2lt', 200, 'Bebida Gaseificada', 10.00)    

''' Prints dos Itens  '''
print(f'Nome: {item1.mostrar_nome()} --- Preço: {item1.mostrar_preco()}\nDescrição: {item1.mostrar_descricao()} --- Estoque: {item1.mostrar_estoque()}\n\n')
print(f'Nome: {item2.mostrar_nome()} --- Preço: {item2.mostrar_preco()}\nDescrição: {item2.mostrar_descricao()} --- Estoque: {item2.mostrar_estoque()}\n\n')
print(f'Nome: {item3.mostrar_nome()} --- Preço: {item3.mostrar_preco()}\nDescrição: {item3.mostrar_descricao()} --- Estoque: {item3.mostrar_estoque()}\n\n')
print(f'Sumario\n{item1.__str__()}\n\n')
print(f'Sumario\n{item2.__str__()}\n\n')
print(f'Sumario\n{item3.__str__()}\n\n')


''' Mudando item 1 '''
item1.mudar_nome('Água')
item1.mudar_preco(0.99)
item1.mudar_descricao('Bebida')
item1.mudar_estoque(400)


''' print do item alterado '''
print(f'Nome: {item1.mostrar_nome()} --- Preço: {item1.mostrar_preco()}\nDescrição: {item1.mostrar_descricao()} --- Estoque: {item1.mostrar_estoque()}\n\n')
print(f'Sumario\n{item1.__str__()}\n\n')