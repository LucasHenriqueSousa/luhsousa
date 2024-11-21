#%% # ---->  Exercicio para entregar. 

'''

Exercício: Contador Simultâneo

Objetivo: Criar um programa em Python que utilize threads para contar até números específicos em paralelo.

Descrição: Você deve implementar um programa que cria múltiplas threads, onde cada thread conta de 1 até um número definido e imprime os resultados. Cada thread deve mostrar seu próprio nome e o número atual da contagem.

Requisitos:
Função contador(num):
A função deve receber um número inteiro como argumento e contar de 1 até esse número.
Durante a contagem, deve imprimir o número atual e o nome da thread que está executando a contagem.
Adicione uma pausa de 0,5 segundos entre as impressões para melhor visualização.
Programa Principal:
Crie uma lista de números que cada thread irá contar.
Para cada número na lista, inicie uma nova thread que chamará a função contador.
Utilize threading.Thread para criar e gerenciar as threads.
Após iniciar todas as threads, o programa deve aguardar a conclusão de todas elas antes de imprimir "Contagem finalizada!".
Exemplo de Uso:
Se a lista de números for [5, 3, 7], a saída deve mostrar as contagens intercaladas das threads até que todas as contagens estejam completas.
Tarefas Adicionais (opcionais):
Modifique a lista de números para experimentar diferentes contagens.
Adicione controle de concorrência utilizando threading.Lock se necessário.

'''
        
import threading
import time

def contador(num):
    nome_thread = threading.current_thread().name
    for i in range(1, num + 1):
        print(f'Thread {nome_thread}: {i}')
        print(f'-----------------')
        time.sleep(0.5)

# Lista dos números até onde cada thread vai contar
numeros = [5, 7, 3]

# Criar e iniciar threads
threads = []
for num in numeros:
    thread = threading.Thread(target=contador, args=(num,))
    threads.append(thread)
    thread.start()

# Esperar todas as threads terminarem
for thread in threads:
    thread.join()

print("Contagem finalizada!")
# %%
def contador(num, nome_thread):
    for i in range(1, num + 1):
        print(f'{nome_thread}: {i}')
        

# Programa principal
def main():
    # Lista de números para cada contador
    numeros = [5, 3, 7]
    
    # Lista de nomes de "threads" simulados
    nomes_threads = ["Thread-1", "Thread-2", "Thread-3"]

    # Lista de contadores
    contadores = [0] * len(numeros)
    
    # Simular a execução intercalada
    while any(contadores[i] < numeros[i] for i in range(len(numeros))):
        for i in range(len(numeros)):
            if contadores[i] < numeros[i]:
                contadores[i] += 1
                print(f'{nomes_threads[i]}: {contadores[i]}')
                print('------------------------------')
    print("Contagem finalizada!")

if __name__ == "__main__":
    main()



# %%
