'''
2-) Crie uma classe Deque que implemente uma fila dupla. A classe deve ter os métodos:

add_front(item): adiciona um item na frente da fila.
add_rear(item): adiciona um item no final da fila.
remove_front(): remove e retorna o item da frente da fila.
remove_rear(): remove e retorna o item do final da fila.
is_empty(): retorna True se a fila estiver vazia, caso contrário, False.
size(): retorna o número de itens na fila.

'''
# Me orientei pelo video (https://www.youtube.com/watch?v=Wr4wcfYSSoI)
class Deque:
    def __init__(self):
        self.items = []

    
    def add_front(self, item):
        self.items.insert(0, item)
        return f'Adicionado {item} à frente do deque.'

    def add_rear(self, item):
        self.items.append(item)
        return f'Adicionado {item} ao final do deque.'

    def remove_front(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def remove_rear(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Programa principal
if __name__ == "__main__":
    deque = Deque()
    print(deque.add_front("1"))
    print(deque.add_rear("2"))
    print(deque.add_front("3"))
    print(deque.add_rear("4"))

    #Fila 
    print('Status da fila', deque.items)
    print("Tamanho do deque:", deque.size())
    # Removendo itens
    print("Removido da frente:", deque.remove_front())
    print('Status da fila', deque.items)
    print("Tamanho do deque:", deque.size())
    print("Removido do final:", deque.remove_rear())
    print('Status da fila', deque.items)
    

    # Verificando o tamanho do deque
    
    print("Tamanho do deque:", deque.size())
    