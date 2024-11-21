'''Você deve desenvolver um sistema para gerenciar diferentes tipos de funcionários em
uma empresa.

1. Crie uma classe base chamada Funcionário com os seguintes atributos privados:
nome e salário
2. Adicione métodos públicos para:

get_nome(): retorna o nome do funcionário.
get_salario(): retorna o salário do funcionário.
calcular_bonus(): um método que deve ser implementado nas subclasses.

3. Crie duas subclasses: Gerente e Desenvolvedor, que herdam da classe
Funcionario. Cada uma deve ter seus próprios atributos:
Gerente: um atributo para departamento.
Desenvolvedor: um atributo para linguagem_programacao.

Implemente o método calcular_bonus() de forma que:
Gerente receba 15% do salário como bônus.
Desenvolvedor receba 10% do salário como bônus.
4. Polimorfismo: Crie uma lista de funcionários que inclua instâncias de Gerente e
Desenvolvedor. Percorra a lista e, para cada funcionário, imprima o nome, o
salário e o bônus calculado, utilizando o método calcular_bonus().
'''

class Funcionario:
    def __init__(self, nome, salario):
        self.__nome = nome
        self.__salario = salario
    
    @property    
    def get_nome(self):
        return self.__nome
    
    @property
    def get_salario(self):
        return self.__salario

class Gerente(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
    
    def calcular_bonus(self):
        return self.get_salario * 0.15

class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
    
    def calcular_bonus(self):
        return self.get_salario * 0.10

funcionarios = [
    Gerente('Natálio dos Santas', 8750.36),
    Gerente('Josélio da Silvo', 17367.25),
    Desenvolvedor('Clarisso do Nutella', 811.00),
    Desenvolvedor('Barrélio Silvanno', 31546.54)
]

for funcionario in funcionarios:
    bonus = funcionario.calcular_bonus()
    salario_atualizado = funcionario.get_salario + bonus
    print(f'Funcionário: {funcionario.get_nome}  Salário: {funcionario.get_salario:.2f}  Bônus: {bonus:.2f}  Salário atualizado: {salario_atualizado:.2f}')


