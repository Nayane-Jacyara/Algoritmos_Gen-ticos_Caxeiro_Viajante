# Resolução do Problema do Caixeiro Viajante com Algoritmos Genéticos

## Descrição Geral

Este projeto explora a resolução do Problema do Caixeiro Viajante (PCV) utilizando Algoritmos Genéticos (AG). O PCV é um problema clássico de otimização combinatória, onde o objetivo é determinar a rota mais curta que permite visitar um conjunto de cidades exatamente uma vez e retornar ao ponto de partida. Devido à sua complexidade, especialmente com o aumento do número de cidades, encontrar a solução exata pode ser computacionalmente inviável, o que torna os Algoritmos Genéticos uma abordagem atraente para encontrar soluções aproximadas.

## Definição do Problema

Dado um conjunto de 58 cidades brasileiras e as distâncias entre cada par de cidades, o desafio é encontrar a sequência de visitas que minimize a distância total percorrida. O conjunto de dados utilizado é o **"brazil58"** da biblioteca TSPLIB, que é amplamente usada em problemas de otimização e pesquisa operacional.

## Abordagem com Algoritmos Genéticos

Os Algoritmos Genéticos são métodos inspirados nos princípios da evolução natural, como seleção, cruzamento (crossover) e mutação, para encontrar soluções próximas do ótimo. Neste projeto, o AG é implementado para evoluir uma população de possíveis soluções (rotas) ao longo de várias gerações, buscando minimizar a distância total da rota.

### Componentes Principais do Algoritmo:
- **População Inicial:** Uma coleção de rotas geradas aleatoriamente.
- **Seleção:** Escolha de rotas mais adaptadas (menores distâncias) para reprodução.
- **Crossover:** Combinação de duas rotas para criar novas rotas (filhos), mantendo características dos pais.
- **Mutação:** Alteração aleatória em uma rota para introduzir diversidade e evitar estagnação.
- **Avaliação (Fitness):** Soma das distâncias entre cidades na rota, com o objetivo de minimizar esse valor.

## Resultados Esperados

Através da aplicação de Algoritmos Genéticos, espera-se encontrar uma rota que, embora não necessariamente a ótima, seja significativamente curta, demonstrando a eficácia do AG na resolução de problemas de otimização complexos como o PCV.
