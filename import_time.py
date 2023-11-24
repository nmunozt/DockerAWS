import time

# Inicia el temporizador
start_time = time.perf_counter()

# Itera desde 1 hasta 100.000
for number in range(1, 100001):
    # Calcula el tiempo transcurrido
    elapsed_time = time.perf_counter() - start_time

    # Imprime el número actual y el tiempo transcurrido
    print(f"Número: {number}, Tiempo transcurrido: {elapsed_time:.2f} segundos")
