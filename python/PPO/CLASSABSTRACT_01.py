'''CLASSES ABSTRATAS :
- Classes abstratas em Python são classes que não podem ser instanciadas diretamente e são projetadas para serem subclasses. Elas fornecem uma interface comum para outras classes, definindo métodos que devem ser implementados nas subclasses, mas sem fornecer uma implementação completa.

Principais Características:
Definição: Uma classe abstrata é definida usando o módulo abc (Abstract Base Class). Para criar uma classe abstrata, você deve herdar de abc.ABC e usar o decorador @abstractmethod para definir métodos abstratos.

Métodos Abstratos: Um método abstrato é um método que é declarado, mas não implementado na classe abstrata. As subclasses que herdam da classe abstrata devem fornecer uma implementação para esses métodos.

Impedir Instanciação: Tentar instanciar uma classe abstrata resultará em um erro. Isso força os desenvolvedores a criar subclasses que implementem a funcionalidade desejada.'''


# abc = Abstract Class
from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def mover(self):
        pass

class Carro(Veiculo):
    def mover(self):
        return 'O carro está se movendo...'
    
class Moto(Veiculo):
    def mover(self):
        return 'A moto está dando grau'

# Uso da Classes
def main():
    carro = Carro()
    moto = Moto()
    print(carro.mover())
    print(moto.mover())
    
if __name__ == '__main__':
    main()
    
    
#%%
# Import do modulo abc (Abstract base class). 
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @abstractmethod
    def emitir_som(self):
        pass

    def info(self):
        return f'{self.nome} tem {self.idade}anos.'
    
class Girafa(Animal):
    def emitir_som(self):
        return 'ÔOOOOOOOOOOOOOooooooooooooo'
class Coruja(Animal):
    def emitir_som(self):
        return 'Huuu-Huuuu'
girafa = Girafa('Amélia', 9)
coruja = Coruja('Noche', 13)

print(girafa.info())
print(girafa.emitir_som())

print(coruja.info())
print(coruja.emitir_som())

# TypeError: Can't instantiate abstract class Animal without an implementation for abstract method.
animal = Animal('Genivalda', 50)

print(animal.info())
print(animal.emitir_som())
# %%
