import tsplib95

# Carregar o arquivo .tsp
problem = tsplib95.load('Caxeiro_Viajante\Algoritmos_Geneticos_PCV\brazil58.tsp')

# Obter as coordenadas das cidades
nodes = list(problem.get_nodes())
distances = {(i, j): problem.get_weight(i, j) for i in nodes for j in nodes if i != j}
