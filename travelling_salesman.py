# Problema do caxeiro viajante para a matéria de Análise de Algoritmos do Mestrado em Computação Aplicada - MCA
# Por: George Borba e Teddy Ordoñez
# V 1.0
from sys import maxsize

def caxeiro_viajante(matriz_distancia, inicio, tamanho):
    vertices = []
    vertices.append(inicio)
    for i in range(tamanho):
        if i != inicio:
            vertices.append(i)

    distancia_minima = maxsize
    while True:
        costo_atual = 0
        k = inicio
        for i in range(len(vertices)):
            costo_atual += matriz_distancia[k][vertices[i]]
            k = vertices[i]
        costo_atual += matriz_distancia[k][inicio]
        distancia_minima = min(distancia_minima, costo_atual)

        if not outro_caminho(vertices):
            break
    vertices.append(inicio)
    return distancia_minima, vertices

def outro_caminho(vertices):
    tamanho = len(vertices)
    i = tamanho - 2

    while i >= 0 and vertices[i] > vertices[i+1]:
        i -= 1

    if i == -1:
        return False
    
    j = i + 1
    while j < tamanho and vertices[j] > vertices[i]:
        j += 1

    j -= 1

    vertices[i], vertices[j] = vertices[j], vertices[i]
    
    esquerda = i + 1
    direita = tamanho - 1

    while esquerda < direita:
        vertices[esquerda], vertices[direita] = vertices[direita], vertices[esquerda]
        esquerda += 1
        direita -= 1
    return True

matriz_distancia = [[0,10,15,20],
                    [10,0,35,25],
                    [15,35,0,30],
                    [20,25,30,0]]
tamanho = 4
inicio = 0
distancia_percorrida, caminho = caxeiro_viajante(matriz_distancia, inicio, tamanho)
print(f'Distancia minima: {distancia_percorrida} \nCaminho Percorrido: {caminho}')