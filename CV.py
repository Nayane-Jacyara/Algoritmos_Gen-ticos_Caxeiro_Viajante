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

# Seleção: seleção por torneio
def tournament_selection(population, fitnesses, k=3):
    selected_indices = np.random.choice(len(population), k, replace=False)
    selected_fitness = [fitnesses[i] for i in selected_indices]
    best_index = selected_indices[selected_fitness.index(min(selected_fitness))]
    return population[best_index]

# Crossover
def order_crossover(parent1, parent2):
    print("\nPai 1:", parent1)
    print("Pai 2:", parent2)
    
    # Escolher dois pontos de corte aleatórios para cada pai
    point1_p1, point2_p1 = np.sort(np.random.randint(0, len(parent1), 2))
    point1_p2, point2_p2 = np.sort(np.random.randint(0, len(parent2), 2))
    print(f"\nPontos de corte para Pai 1: {point1_p1}, {point2_p1}")
    print(f"Pontos de corte para Pai 2: {point1_p2}, {point2_p2}")
    
    # Inicializar os filhos com None ou um marcador indicando posições não preenchidas
    child1 = [None] * len(parent1)
    child2 = [None] * len(parent1)
    
    # Copiar a subsequência do pai para o filho correspondente
    child1[point1_p1:point2_p1] = parent1[point1_p1:point2_p1]
    child2[point1_p2:point2_p2] = parent2[point1_p2:point2_p2]
    
    # Função para preencher o filho com os genes restantes, mantendo a ordem do segundo pai
    def fill_child(child, parent, start_pos):
        current_position = start_pos
        for gene in parent:
            if gene not in child:
                if current_position >= len(child):
                    current_position = 0
                child[current_position] = gene
                current_position += 1
    
    # Preencher os filhos com os genes restantes do outro pai
    fill_child(child1, parent2, point2_p1)
    fill_child(child2, parent1, point2_p2)
    
    print("\nFilho 1 completo:", child1)
    print("Filho 2 completo:", child2)
    
    return child1, child2

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
    print(f"\nTrocando cidade: {chromosome[i]} com cidade: {chromosome[j]}")
    
    # Realizar a mutação (trocar os elementos nas posições i e j)
    chromosome[i], chromosome[j] = chromosome[j], chromosome[i]
    
    # Imprimir o cromossomo depois da mutação
    print(f"Cromossomo depois da mutação:  {chromosome}\n")


# Algoritmo genético
def genetic_algorithm(nodes, distances, population_size=30, generations=15, mutation_rate=0.05):
    # Inicialização da população
    population = [create_chromosome(nodes) for _ in range(population_size)]
    
    for generation in range(generations):
        # Avaliação
        fitnesses = [calculate_fitness(chromosome, distances) for chromosome in population]
        
        # Melhor solução da geração atual
        best_fitness = min(fitnesses)
        best_chromosome = population[fitnesses.index(best_fitness)]
        print(f"\nGeração {generation + 1}: Melhor distância = {best_fitness}")
        
        # Nova geração
        new_population = []
        
        for _ in range(population_size // 2):
            # Garantir que parent1 e parent2 sejam diferentes
            parent1 = tournament_selection(population, fitnesses)
            parent2 = parent1
            while parent2 == parent1:
                parent2 = tournament_selection(population, fitnesses)
            
            child1, child2 = order_crossover(parent1, parent2)
            
            if np.random.rand() < mutation_rate:
                mutate(child1)
                mutate(child2)
                
            new_population.extend([child1, child2])
        
        population = new_population
    
    # Melhor solução encontrada
    fitnesses = [calculate_fitness(chromosome, distances) for chromosome in population]
    best_fitness = min(fitnesses)
    best_chromosome = population[fitnesses.index(best_fitness)]
    
    return best_chromosome, best_fitness

best_solution, best_distance = genetic_algorithm(nodes, distances)
print("\nMelhor caminho:", best_solution)
print("Distância mínima:", best_distance)
