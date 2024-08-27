import numpy as np

# Função de mutação para trocar dois elementos no cromossomo
def mutate(chromosome):
    # Escolher dois índices aleatórios para trocar
    i = np.random.randint(0, len(chromosome))
    j = np.random.randint(0, len(chromosome))
    
    # Garantir que os índices são diferentes
    while i == j:
        j = np.random.randint(0, len(chromosome))
    
    # Imprimir o cromossomo antes da mutação
    print(f"\nCromossomo antes da mutação: {chromosome}")
    print(f"Trocando cidade: {chromosome[i]} com cidade: {chromosome[j]}")
    
    # Realizar a mutação (trocar os elementos nas posições i e j)
    chromosome[i], chromosome[j] = chromosome[j], chromosome[i]
    
    # Imprimir o cromossomo depois da mutação
    print(f"Cromossomo depois da mutação:  {chromosome}\n")

# Exemplo de cromossomo para teste
test_chromosome = [1, 2, 3, 4, 5]

# Aplicar a mutação
mutate(test_chromosome)
