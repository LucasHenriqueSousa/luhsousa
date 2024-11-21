'''
EXERCÍCIO 1

Você deve desenvolver um sistema para gerenciar diferentes tipos de veículos. Para isso,
crie uma classe abstrata chamada Veículo, que deve conter os seguintes métodos
abstratos:

1. calcular_consumo(): que deve retornar o consumo de combustível do veículo.

2. info(): que deve retornar informações básicas sobre o veículo (como marca,
modelo e ano).

Em seguida, implemente duas subclasses: Carro e Moto. A classe Carro deve ter um
atributo adicional para a capacidade do tanque de combustível e a classe Moto deve ter
um atributo para o tipo de guidão. Ambas as subclasses devem implementar os métodos
abstratos de forma apropriada.
Por fim, crie instâncias de Carro e Moto, e demonstre o uso dos
métodos calcular_consumo() e info().


'''

from abc import ABC, abstractmethod
# classe Abstrata
class Veiculo(ABC):
    # Metodo inicializador / construtor
    def __init__(self, marca, modelo, ano):
        # atributos 
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    @abstractmethod
    def info(self):
        pass
    
    @abstractmethod
    def calcular_consumo(self):
        pass
    
    
    #sub-classe
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, tanque):
        super().__init__(marca, modelo, ano)
        self.tanque = tanque    
        
        
    # polimorfismo    
    def info(self):
        return f'Marca: {self.marca}, Modelo: {self.modelo}, ano: {self.ano} e capacidade total do tanque é: {self.tanque}'
    # polimorfismo
    def calcular_consumo(self):        
        km = int(input('Qual é a kilometragem percorrida por você em seu carro ?\n'))        
        tanque = int(input('Qual a quantidade em litros de combustivel abastecido no seu carro ?\n'))
        consumo = (km / tanque)        
        return f'{consumo:.2f}'
    
    #sub-classe    
class moto(Veiculo):
    def __init__(self, marca, modelo, ano, guidao):
        super().__init__(marca, modelo, ano)
        self.guidao = guidao
    
    # polimorfismo
    def info(self):
         return f'Marca: {self.marca}, Modelo: {self.modelo}, ano: {self.ano} e seu tipo de Guidão é:{self.guidao}'
    # polimorfismo
    def calcular_consumo(self):        
        km = int(input('Qual é a kilometragem percorrida por você em sua moto ? \n'))        
        tanque = int(input('Qual a quantidade em litros de combustivel abastecido em sua moto?\n'))
        consumo = (km / tanque)        
        return f'{consumo:.2f}'
        
carro1 = Carro('Hyunday','HB20s',2020, '50.L')
carro2 = Carro('Honda','Civic',2024, '55.L')
carro3 = Carro('Ferrari','F450',2010, '60.L')
moto1 = moto('Honda','CBR-1000', 2016, 'tipo-2')
moto2 = moto('Yamaha','Yamaha MT-07',2022, 'tipo-1')
moto3 = moto('Kawasaki','Kawasaki Ninja 400',2023, 'tipo-5')

print(f'Seu Veículo: \n{carro1.info()}, ele fez um consumo de: {carro1.calcular_consumo()}Km/L \n')
print(f'Seu Veículo: \n{carro2.info()}, ele fez um consumo de: {carro2.calcular_consumo()}Km/L \n')
print(f'Seu Veículo: \n{carro3.info()}, ele fez um consumo de: {carro3.calcular_consumo()}Km/L \n')
print(f'Seu Veículo: \n{moto1.info()}, ele fez um consumo de: {moto1.calcular_consumo()}Km/L \n')
print(f'Seu Veículo: \n{moto2.info()}, ele fez um consumo de: {moto2.calcular_consumo()}Km/L \n')
print(f'Seu Veículo: \n{moto3.info()}, ele fez um consumo de: {moto3.calcular_consumo()}Km/L \n')
