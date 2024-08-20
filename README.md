## Problema do Caixeiro Viajante com Algoritmos Genéticos

Este projeto aborda a resolução do **Problema do Caixeiro Viajante (PCV)** utilizando **Algoritmos Genéticos (AG)**. O PCV é um problema clássico de otimização combinatória, onde o objetivo é determinar o menor caminho que percorre todas as cidades de um conjunto, visitando cada uma exatamente uma vez e retornando ao ponto de partida. Este problema é notório por sua complexidade computacional, especialmente à medida que o número de cidades aumenta.

### Descrição do Problema

Dado um conjunto de cidades e as distâncias entre cada par de cidades, o desafio é encontrar a sequência de visitas que minimize a distância total percorrida. Este projeto utiliza o conjunto de dados "brazil58" da biblioteca TSPLIB, que contém 58 cidades no Brasil e suas respectivas distâncias, representadas em uma matriz de adjacência.

### Abordagem com Algoritmos Genéticos

Os Algoritmos Genéticos são inspirados no processo de evolução natural e são utilizados aqui para encontrar uma solução aproximada para o PCV. O AG opera em uma população de soluções (caminhos) e utiliza operações como seleção, crossover (recombinação) e mutação para evoluir soluções cada vez melhores ao longo de várias gerações.