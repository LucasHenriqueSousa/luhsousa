#%%
##Roteiro Experimental: Semáforos e Monitores em Python

##------------------------------
##INTRODUÇÃO
##------------------------------

##Neste experimento, você irá trabalhar com conceitos de sincronização de threads usando semáforos e monitores.
##Essas ferramentas de controle de concorrência permitem que múltiplas threads acessem recursos compartilhados
##de forma organizada, evitando condições de corrida e garantindo a integridade dos dados.

##------------------------------
##SEMÁFOROS
##------------------------------

##Neste exemplo, você usará um semáforo para controlar o acesso de múltiplas threads a um recurso compartilhado.
##O semáforo limita o número de threads que podem acessar o recurso simultaneamente.

#DESCOMENTE O CÓDIGO ABAIXO
##------------------------------
##DESAFIOS ADICIONAIS
##------------------------------
#%%    
import threading
import time

# Cria um semáforo com um limite de 3 threads simultâneas
sem = threading.Semaphore(3)

def acessar_recurso(id_thread):
    sem.acquire()  # Adquire o semáforo
    inicio = time.time()  # Marca o início do uso do recurso
    print(f"Thread {id_thread} acessou o recurso.")
    
    time.sleep(2)  # Simula o uso do recurso por 2 segundos
    
    fim = time.time()  # Marca o término do uso do recurso
    duracao = fim - inicio  # Calcula o tempo passado no recurso
    print(f"Thread {id_thread} liberou o recurso. Tempo no recurso: {duracao:.4f} segundos")
    
    sem.release()  # Libera o semáforo

# Cria e inicia múltiplas threads, cada uma com um identificador único
threads = [threading.Thread(target=acessar_recurso, args=(i,)) for i in range(1, 6)]
for thread in threads:
    thread.start()

# Aguarda todas as threads terminarem
for thread in threads:
    thread.join()

print("Todos os threads finalizaram.")



### Instruções
##1. Execute o código e observe como as threads adquirem e liberam o recurso.
##2. Experimente modificar o valor no `Semaphore(3)` para diferentes valores e observe como o número de threads
##   simultâneas muda.
##3. Perguntas para reflexão:
##   - O que acontece quando o número de threads excede o limite do semáforo?
##   - Como o `sem.release()` afeta o comportamento das threads?

##------------------------------
##MONITOR
##------------------------------

##Neste exemplo, você usará um monitor para proteger o acesso a um recurso compartilhado usando a classe `Lock`.
##Com o monitor, apenas uma thread pode acessar a seção crítica por vez, garantindo a exclusividade.

#COMENTE O CÓDIGO INICIAL (ACIMA)
#DESCOMENTE O CÓDIGO ABAIXO

#%%
import threading

class Monitor:
    def __init__(self):
        self.lock = threading.Lock()
        self.recurso = 0

    def acessar_recurso(self):
        with self.lock:  # Adquire o bloqueio automaticamente
            self.recurso += 1
            print(f"{threading.current_thread().name} acessou o recurso: {self.recurso}")

monitor = Monitor()

# Cria e inicia múltiplas threads
threads = [threading.Thread(target=monitor.acessar_recurso) for _ in range(5)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()


## Instruções
##1. Execute o código e observe como apenas uma thread acessa o recurso de cada vez.
##2. Experimente comentar a linha `with self.lock` e observe o que acontece.
##3. Perguntas para reflexão:
##   - Como o `Lock` controla o acesso ao recurso compartilhado?
##   - O que acontece com `self.recurso` quando o `Lock` não é utilizado?

##------------------------------
##DISCUSSÃO
##------------------------------
    
##- Quais as principais diferenças entre o semáforo e o monitor em relação ao controle de concorrência?
##- Em que situações o semáforo é mais indicado que o monitor, e vice-versa?
##- Como esses conceitos podem ser aplicados em sistemas reais, como bancos de dados, sistemas de reserva
##  e redes de telecomunicações?

##------------------------------
##DESAFIOS ADICIONAIS
##------------------------------
    
##1. Modifique o exercício de semáforo para que cada thread tenha um identificador único e registre o tempo que
##   passou no recurso.

##2. No exercício de monitor, adicione um contador para verificar quantas vezes o recurso foi acessado no total.

##3. Explore o uso de `RLock` no exercício de monitor e veja como ele permite que uma mesma thread adquira o
##   bloqueio múltiplas vezes.

##4. Em um escritório, várias pessoas precisam imprimir documentos. Porém, há apenas uma impressora disponível.
##   Além disso, somente três pessoas podem estar na fila de espera para a impressão de cada vez.
##   Usar um `Semaphore` para controlar a fila de espera e um `Lock` para garantir que apenas uma pessoa imprima por vez.

##------------------------------
##CONCLUSÃO
##------------------------------
    
##Este roteiro apresentou uma introdução prática ao uso de semáforos e monitores em Python, permitindo que você
##explore o comportamento dessas estruturas de sincronização em ambientes concorrentes. Esses conceitos são
##fundamentais para o desenvolvimento de sistemas robustos e seguros, onde o controle de acesso a recursos
##compartilhados é essencial.
# %%
