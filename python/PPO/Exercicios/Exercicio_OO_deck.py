'''
1-) Simule um sistema de fila de atendimento em um banco. Crie uma classe Banco que utilize a classe Fila e tenha os métodos:
adicionar_cliente(nome): adiciona um cliente à fila.
atender_cliente(): remove e retorna o nome do cliente que está sendo atendido.
Adicione 5 clientes e atenda somente os 3 primeiros. Seu programa deve mostrar quais foram os clientes atendidos e o tamanho da fila.

Mostre o programa em funcionamento.

'''

class Fila:
    def __init__(self):
        self.nome = [] #Clientes qu chegaram na fila
        self.clientes_atendidos = []  #clientes atendidos

    def fila_vazia(self):
        return len(self.nome) == 0

    def adicionar_cliente(self, item):
        self.nome.append(item)
        return f'O cliente {item} foi adicionado à fila.'

    def atender_cliente(self):
        if not self.fila_vazia():
            cliente = self.nome.pop(0)
            self.clientes_atendidos.append(cliente)  # Guarda o cliente atendido
            return f'O cliente {cliente} está sendo atendido.'
        else:
            return "Nenhum cliente na fila para atender."

    def tamanho_fila(self):
        return len(self.nome)

class Banco(Fila):
    def __init__(self):
        super().__init__()

# Programa principal # --> aprendi a usar assim pelo video. (https://www.youtube.com/watch?v=Wr4wcfYSSoI)
if __name__ == "__main__":
    banco = Banco()
    banco.adicionar_cliente("Claudia")
    banco.adicionar_cliente("Debora")
    banco.adicionar_cliente("Zípora")
    banco.adicionar_cliente("Cleonice")
    banco.adicionar_cliente("Deoleia")

    # Atendendo os três primeiros clientes
    print(banco.atender_cliente())
    print(banco.atender_cliente())
    print(banco.atender_cliente())

    # Mostra os clientes atendidos e o tamanho da fila restante
    print("Clientes atendidos:", banco.clientes_atendidos)
    print(f'Tamanho da fila:{banco.tamanho_fila()}, \nFaltam: {banco.nome}')