# %%
import threading
import multiprocessing
import time
import random
import matplotlib.pyplot as plt

# Função que as threads vão executar
def tarefa(process_id, thread_id, resultados):
    start_time = time.time()  # Tempo de início
    duracao = random.uniform(0.5, 2)  # Simulando o tempo de execução da tarefa
    time.sleep(duracao)

    # Adicionando resultados
    resultados.append((process_id, thread_id, duracao, time.time() - start_time))
    print(f"[Processo {process_id}, Thread {thread_id}] Durou {duracao:.2f} segundos")

# Função que os processos vão executar
def processo(process_id, num_threads, resultados):
    threads = []
    
    for thread_id in range(num_threads):
        thread = threading.Thread(target=tarefa, args=(process_id, thread_id, resultados))
        threads.append(thread)
        thread.start()

    # Esperar todas as threads terminarem
    for thread in threads:
        thread.join()

# Função principal
def executar(num_processos, num_threads):
    with multiprocessing.Manager() as manager:
        resultados = manager.list()  # Lista compartilhada segura entre processos
        processos = []

        for process_id in range(num_processos):
            p = multiprocessing.Process(target=processo, args=(process_id, num_threads, resultados))
            processos.append(p)
            p.start()

        # Esperar todos os processos terminarem
        for p in processos:
            p.join()

        return list(resultados)

# Função para plotar os resultados em um gráfico de linhas
def plotar_resultados(resultados):
    if not resultados:
        print("Nenhum resultado foi gerado.")
        return

    # Preparar dados para o gráfico
    processos = sorted(set(r[0] for r in resultados))  # IDs dos processos
    duracoes_por_processo = {p: [] for p in processos}

    for r in resultados:
        process_id, thread_id, duracao, _ = r
        duracoes_por_processo[process_id].append((thread_id, duracao))

    # Ordenar threads dentro de cada processo
    for process_id in duracoes_por_processo:
        duracoes_por_processo[process_id].sort()  # Ordenar por thread_id

    # Plotar os resultados
    plt.figure()
    for process_id, duracoes in duracoes_por_processo.items():
        thread_ids = [d[0] for d in duracoes]
        duracao_threads = [d[1] for d in duracoes]
        plt.plot(thread_ids, duracao_threads, label=f'Processo {process_id}')

    # Personalizar o gráfico
    plt.xlabel('Thread ID')
    plt.ylabel('Duração (s)')
    plt.title('Duração de Execução das Threads por Processo')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    num_processos = 4  # Quantidade de processos
    num_threads = 5    # Quantidade de threads por processo

    # Executar e coletar os resultados
    resultados = executar(num_processos, num_threads)
    
    # Verificar se os resultados foram coletados
    if resultados:
        for r in resultados:
            print(f"Processo {r[0]} - Thread {r[1]}: Duração {r[2]:.2f} segundos")
    else:
        print("Nenhum dado foi coletado.")

    # Plotar o gráfico de resultados
    plotar_resultados(resultados)



    
#%%
import threading
import multiprocessing
import time
import random
import matplotlib.pyplot as plt
# Semáforo global para limitar o número de threads executando tarefas ao mesmo tempo
semaforo = threading.Semaphore(3)  # Limitar a 3 threads simultâneas

# Bloqueio para garantir a segurança em operações críticas (Thread-Safe)
lock = threading.Lock()

# Função que as threads vão executar
def tarefa(process_id, thread_id, resultados, conc_duracoes):
    with semaforo:
        start_time = time.time()  # Tempo de início

        # Simulando a execução de uma tarefa
        duracao = random.uniform(0.5, 2)
        time.sleep(duracao)

        end_time = time.time()

        # Adicionar os tempos para análise de concorrência
        conc_duracoes[thread_id].append(end_time - start_time)

        with lock:
            resultados.append((process_id, thread_id, duracao, end_time - start_time))
            print(f"[Processo {process_id}, Thread {thread_id}] Durou {duracao:.2f} segundos (Thread-Safe)")

# Função que os processos vão executar
def processo(process_id, num_threads, resultados, conc_duracoes):
    threads = []
    
    for thread_id in range(num_threads):
        thread = threading.Thread(target=tarefa, args=(process_id, thread_id, resultados, conc_duracoes))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

# Função principal
def executar(num_processos, num_threads):
    with multiprocessing.Manager() as manager:
        resultados = manager.list()  # Lista compartilhada segura entre processos
        conc_duracoes = manager.dict({i: [] for i in range(num_threads)})  # Para medir concorrência por thread
        processos = []

        for process_id in range(num_processos):
            p = multiprocessing.Process(target=processo, args=(process_id, num_threads, resultados, conc_duracoes))
            processos.append(p)
            p.start()

        for p in processos:
            p.join()

        return list(resultados), dict(conc_duracoes)

# Função para gerar gráficos distintos
def gerar_graficos(resultados, conc_duracoes):
    if not resultados:
        print("Nenhum resultado foi gerado.")
        return

    processos = sorted(set(r[0] for r in resultados))
    duracoes_por_processo = {p: [] for p in processos}
    threads_por_processo = {p: [] for p in processos}

    for r in resultados:
        process_id, thread_id, duracao, _ = r
        duracoes_por_processo[process_id].append(duracao)
        threads_por_processo[process_id].append(thread_id)

    # Gráfico 1: Concorrência - Medindo quanto tempo cada thread levou
    plt.figure(figsize=(10, 5))
    for thread_id, duracoes in conc_duracoes.items():
        plt.plot(duracoes, label=f'Thread {thread_id}')
    plt.title('Concorrência: Tempo de execução de cada thread')
    plt.xlabel('Execuções')
    plt.ylabel('Duração (s)')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Gráfico 2: Paralelismo - Tempo de execução das threads por processo
    plt.figure(figsize=(10, 5))
    for process_id, duracoes in duracoes_por_processo.items():
        plt.plot(range(len(duracoes)), duracoes, label=f'Processo {process_id}')
    plt.title('Paralelismo: Tempo de execução das threads por processo')
    plt.xlabel('Número de threads')
    plt.ylabel('Duração (s)')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Gráfico 3: Thread Safety - Mostrando que o acesso à lista de resultados foi feito de forma segura
    plt.figure(figsize=(10, 5))
    thread_count = {t: 0 for t in range(len(resultados))}
    for r in resultados:
        process_id, thread_id, duracao, _ = r
        thread_count[thread_id] += 1
    plt.bar(thread_count.keys(), thread_count.values())
    plt.title('Thread Safety: Acesso seguro aos resultados')
    plt.xlabel('Thread ID')
    plt.ylabel('Quantidade de acessos')
    plt.grid(True)
    plt.show()

    # Gráfico 4: Multi-threads - Duração total por processo com múltiplas threads
    plt.figure(figsize=(10, 5))
    total_duracoes = {p: sum(duracoes_por_processo[p]) for p in processos}
    plt.bar(total_duracoes.keys(), total_duracoes.values())
    plt.title('Multi-Threads: Duração total por processo')
    plt.xlabel('Processo ID')
    plt.ylabel('Duração Total (s)')
    plt.grid(True)
    plt.show()

    # Gráfico 5: Semáforo - Verificando a limitação do número de threads simultâneas
    plt.figure(figsize=(10, 5))
    plt.plot([semaforo._value for _ in range(len(resultados))])
    plt.title('Semáforo: Limitação do número de threads simultâneas')
    plt.xlabel('Execuções')
    plt.ylabel('Número de threads ativas')
    plt.grid(True)
    plt.show()

# Iniciar a execução
if __name__ == '__main__':
    num_processos = 4  # Quantidade de processos
    num_threads = 5    # Quantidade de threads por processo

    # Executar e coletar os resultados
    resultados, conc_duracoes = executar(num_processos, num_threads)
    
    # Verificar se os resultados foram coletados
    if resultados:
        for r in resultados:
            print(f"Processo {r[0]} - Thread {r[1]}: Duração {r[2]:.2f} segundos")
    else:
        print("Nenhum dado foi coletado.")

    # Gerar os gráficos individuais para cada tópico
    gerar_graficos(resultados, conc_duracoes)

# %%
