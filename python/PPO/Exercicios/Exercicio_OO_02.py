'''
2. Crie uma classe Lâmpada com os seguintes atributos e métodos:
Atributos:
1. Cor;
2. Voltagem;
3. Luminosidade;
4. Ligada (a lâmpada deve inicializar desligada).
Métodos:
1. Verificar se a lâmpada está ligada/desligada
2. Ligar/desligar a lâmpada.
Todos os atributos devem ser privados.
Crie um objeto da classe Lâmpada e teste os métodos criados.

'''
class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False  

    def verificar_estado(self):
        return "Ligada" if self.__ligada else "Desligada"

    def ligar(self):
        self.__ligada = True

    def desligar(self):
        self.__ligada = False


lampada = Lampada("Branca", 220, 800)


print(f"Estado inicial da lâmpada: {lampada.verificar_estado()}")
lampada.ligar()
print(f"Estado da lâmpada após ligar: {lampada.verificar_estado()}")
lampada.desligar()
print(f"Estado da lâmpada após desligar: {lampada.verificar_estado()}")
# %%

class Lampada:
    def __init__(self,cor,voltagem,luminosidade,):
        self.__Cor = cor
        self.__Voltagem = voltagem
        self.__Luminosidade = luminosidade
        self.__Estado = 'Desligada'
    @property
    def Estado(self):
        if self.__Estado == 'Ligada':
            return f'Lampada está Ligada'
        else:
            return f'Lampada está Desligada'
    @Estado.setter
    def mudar(self, valor):
        if valor.lower() in ['Ligada', 'Desligada']:
            self.__Estado = valor.lower()
        
        
    @property
    def cor(self):
        return self.__Cor 
    @property
    def voltagem(self):
        return self.__Voltagem
    @property
    def luminosidade(self):
        return self.__Luminosidade

luz = Lampada('azul', 220, '12k lumens')

luz.mudar = 'Ligada'

print(luz.Estado)