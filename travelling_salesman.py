# Problema do caxeiro viajante para a matéria de Análise de Algoritmos do Mestrado em Computação Aplicada - MCA
# Por: George Borba e Teddy Ordoñez
# V 1.0
from sys import maxsize
'''
MÉTODO DE FORÇA BRUTA APLICANDO DFS
def caxeiro_viajante_hamiltoniano(grafo, visitados, posicao_cidade_atual, tamanho, contador, custo):
    if (contador == tamanho and grafo[posicao_cidade_atual][0]):
        distancia_percorrida.append(custo + grafo[posicao_cidade_atual][0])
        return

    for i in range(tamanho):
        if (visitados[i] == False and grafo[posicao_cidade_atual][i]):
            visitados[i] =  True
            caxeiro_viajante_hamiltoniano(grafo, visitados, i, tamanho, contador + 1, custo + grafo[posicao_cidade_atual][i])
            visitados[i] = False

matriz_distancia = [[ 0, 10, 15, 20 ],
                    [ 10, 0, 35, 25 ],
                    [ 15, 35, 0, 30 ],
                    [ 20, 25, 30, 0 ]]
tamanho = 4
inicio = 0
visitados = [False for i in range(tamanho)]
distancia_percorrida = []

caxeiro_viajante_hamiltoniano(matriz_distancia, visitados, inicio, tamanho, 1, 0)

print(min(distancia_percorrida))
print(visitados)    # Tentar colocar a ordem dos visitados numa variavel
'''
# MÉTODO COM HEURISTÍCA DO VIZINHO MAIS PRÓXIMO

matriz_distancia = [[0, 15, 12, 60, 38, 90],
                    [15, 0, 76, 19, 40, 7],
                    [12, 76, 0, 81, 33, 24],
                    [60, 19, 81, 0, 51, 45],
                    [38, 40, 33, 51, 0, 30],
                    [90, 7, 24, 45, 30, 0]]

visitados = [False for i in range(len(matriz_distancia))]
rota = [0]

# salva elemento inicial
elemento_inicial = 0

# variavel para armazenar elemento cidade_atual
cidade_atual = elemento_inicial
# marca cidade_atual como visitado
visitados[cidade_atual] = True 

# Custo da rota
custo = 0

while False in visitados: # enquanto houver elemento não visitado    
    menor_distancia = maxsize # valor da menor distância
    indice_do_elemento = -1 # indice do elemento de menor distância
    for j in range(0, len(matriz_distancia[0])):
        
        # se não é o próprio elemento e não foi visitado
        if cidade_atual != j and (not visitados[j]):
            
            # verifica se a distância é menor q a menor distância
            if matriz_distancia[cidade_atual][j] < menor_distancia:
                menor_distancia = matriz_distancia[cidade_atual][j]
                
                indice_do_elemento = j
    
    # atribui novo cidade_atual
    cidade_atual = indice_do_elemento
    # marca como visitado
    visitados[cidade_atual] = True
    # Soma o custo de visitar a cidade
    custo += menor_distancia
    # adiciona à rota
    rota.append(cidade_atual)

# retorna ao elemento inicial    
rota.append(elemento_inicial)
# Soma o custo de voltar à cidade inicial
custo += matriz_distancia[cidade_atual][elemento_inicial]    

print('Rota percorrida:', rota)
print('Custo dessa rota:', custo)
