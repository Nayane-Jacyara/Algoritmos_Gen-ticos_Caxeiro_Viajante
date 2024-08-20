import tsplib95
import numpy as np

# Carregar o arquivo .tsp
problem = tsplib95.load('C:/Users/Nayane Jacyara/Documents/Faculdade/sistemaInteligentes/Caxeiro_Viajante/Algoritmos_Geneticos_PCV/brazil58.tsp')

# Obter as coordenadas das cidades
nodes = list(problem.get_nodes())
distances = {(i, j): problem.get_weight(i, j) for i in nodes for j in nodes if i != j}

# Representação do Cromossomo: Cada cromossomo será uma lista que representa uma sequência de cidades
def create_chromosome(nodes):
    chromosome = nodes.copy()
    np.random.shuffle(chromosome)
    return chromosome

# Verificar se a Solução é Válida
def is_valid_chromosome(chromosome, nodes):
    return sorted(chromosome) == sorted(nodes)

# Função de Avaliação (Fitness): A função de fitness será a soma das distâncias entre as cidades no percurso definido pelo cromossomo
def calculate_fitness(chromosome, distances):
    return sum(distances[(chromosome[i], chromosome[i+1])] for i in range(len(chromosome) - 1)) + distances[(chromosome[-1], chromosome[0])]

# Seleção: Implemente uma seleção por torneio
def tournament_selection(population, fitnesses, k=3):
    selected_indices = np.random.choice(len(population), k, replace=False)
    selected_fitness = [fitnesses[i] for i in selected_indices]
    best_index = selected_indices[selected_fitness.index(min(selected_fitness))]
    return population[best_index]

# Crossover: Implemente o crossover de ciclo (Cycle Crossover)
def cycle_crossover(parent1, parent2):
    child1, child2 = parent1[:], parent2[:]
    
    for i in range(len(parent1)):
        if child1[i] == parent2[i]:
            continue
        value = parent1[i]
        index = parent2.index(value)
        
        while True:
            child1[i], child2[i] = child2[i], child1[i]
            i = index
            value = parent1[index]
            if value == parent1[i]:
                break
            index = parent2.index(value)
    
    return child1, child2

# Mutação: Implemente a mutação de troca (swap mutation) com impressão
def mutate(chromosome):
    i, j = np.random.randint(0, len(chromosome)), np.random.randint(0, len(chromosome))
    print(f"Mutação aplicada: trocando cidade na posição {i} com cidade na posição {j}")
    chromosome[i], chromosome[j] = chromosome[j], chromosome[i]

# Loop Principal: Implemente o loop do algoritmo genético
def genetic_algorithm(nodes, distances, population_size=100, generations=500, mutation_rate=0.01):
    # Inicialização da população
    population = [create_chromosome(nodes) for _ in range(population_size)]
    
    for generation in range(generations):
        # Avaliação
        fitnesses = [calculate_fitness(chromosome, distances) for chromosome in population]
        
        # Melhor solução da geração atual
        best_fitness = min(fitnesses)
        best_chromosome = population[fitnesses.index(best_fitness)]
        print(f"Geração {generation + 1}: Melhor distância = {best_fitness}")
        
        # Nova geração
        new_population = []
        
        for _ in range(population_size // 2):
            parent1 = tournament_selection(population, fitnesses)
            parent2 = tournament_selection(population, fitnesses)
            
            child1, child2 = cycle_crossover(parent1, parent2)
            
            if np.random.rand() < mutation_rate:
                mutate(child1)
                mutate(child2)
                
            new_population.extend([child1, child2])
        
        population = new_population
    
    # Melhor solução encontrada
    best_fitness = min(fitnesses)
    best_chromosome = population[fitnesses.index(best_fitness)]
    
    return best_chromosome, best_fitness

# Executando o Algoritmo: Chame a função genetic_algorithm e exiba o melhor caminho encontrado
best_solution, best_distance = genetic_algorithm(nodes, distances)
print("Melhor caminho:", best_solution)
print("Distância mínima:", best_distance)
