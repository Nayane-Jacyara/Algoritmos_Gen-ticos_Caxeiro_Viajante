import numpy as np

# Função de Crossover Ordenado com cortes de mesmo tamanho
def order_crossover(parent1, parent2):
    print("\nPai 1:", parent1)
    print("Pai 2:", parent2)
    
    # Escolher o tamanho do segmento
    segment_size = np.random.randint(1, len(parent1))
    
    # Escolher o ponto inicial aleatório para o segmento em ambos os pais
    start_point1 = np.random.randint(0, len(parent1) - segment_size + 1)
    start_point2 = np.random.randint(0, len(parent2) - segment_size + 1)
    
    end_point1 = start_point1 + segment_size
    end_point2 = start_point2 + segment_size
    
    print(f"\nTamanho do segmento: {segment_size}")
    print(f"Pontos de corte para Pai 1: {start_point1}, {end_point1}")
    print(f"Pontos de corte para Pai 2: {start_point2}, {end_point2}")
    
    # Inicializar os filhos com None ou um marcador indicando posições não preenchidas
    child1 = [None] * len(parent1)
    child2 = [None] * len(parent1)
    
    # Copiar a subsequência dos pais para os filhos correspondentes
    child1[start_point1:end_point1] = parent1[start_point1:end_point1]
    child2[start_point2:end_point2] = parent2[start_point2:end_point2]
    
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
    fill_child(child1, parent2, end_point1)
    fill_child(child2, parent1, end_point2)
    
    print("\nFilho 1 completo:", child1)
    print("Filho 2 completo:", child2)
    
    return child1, child2

# Exemplo de pais para teste
parent1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
parent2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]

# Testar o crossover
child1, child2 = order_crossover(parent1, parent2)
