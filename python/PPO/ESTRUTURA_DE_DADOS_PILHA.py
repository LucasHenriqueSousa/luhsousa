'''
Estruturas de dados. 
TADS -> Tipos abstratos de dados
Estrutura em Steck 'Pilha'
LIFO -> lest in first out (ultimo a entrar primeiro a sair)
Operações -
          |-> 1. Empilhar *busar o metodo .append()
          |-> 2. Desempilhar * usar o metodo com .pop
          |-> 3. Verificar se esta vazia * usar o metodo len() == 0
          |-> 4. Topo * usar o metodo [-1] para mostrar o ultimo da lista/pilha
          |-> 5. Tamanho * usar o metodo de .len()
          |-> 6. STR * metodo para transformar a lista em string para a visualizacao dos elementos. __str__
'''

class Pilha:
    def __init__(self):
        self.itens = []

    def esta_vazia(self):
        return len(self.itens) == 0 # <-- esse é o metodo .len()
    
    
    def empilhar(self, item):
        self.itens.append(item) # <-- esse é o metodo .append()
    
        
    def desempilhar(self):
        if not self.esta_vazia():
            return self.itens.pop() # <-- esse é o metodo de .pop() 
        
        else:
            return None    
        
    def topo(self):
            if not self.esta_vazia():
                return self.itens[-1]
            else:
                return None
    
    def tamanho(self):
        return len(self.itens)
    
    def __str__(self):
        return str(self.itens)
            
minha_pilha = Pilha()

# empilhando 

minha_pilha.empilhar('P')
minha_pilha.empilhar('Y')
minha_pilha.empilhar('T')
minha_pilha.empilhar('H')
minha_pilha.empilhar('O')
minha_pilha.empilhar('N')
print('pilha após empilhamento: ', minha_pilha)

print('elemento no topo da pilha: ', minha_pilha.topo())

#desempilhando
print('Desemplihando: ', minha_pilha.desempilhar())
print('Verificar status da pilha: ', minha_pilha)
print('Desemplihando: ', minha_pilha.desempilhar())
print('Verificar status da pilha: ', minha_pilha)
print('Tamanho da pilha: ', minha_pilha.tamanho())
