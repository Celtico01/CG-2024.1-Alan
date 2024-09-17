from classes.vertex import Vertex
from classes.face import Face
from classes.sru import SRU
from classes.opposite_face import Estrutura
import numpy as np
import os
import math
import sys

def inserir_pontos(x,y, qtde_elem, of):
    meio_linha = x // 2
    meio_coluna = y // 2
    id = qtde_elem

    while True:
        try:
            print('[1] Inserir novo ponto.')
            print('[0] Volta para menu.')
            escolha = int(input('Escolha: '))
            os.system('cls')

            if escolha != 0 and escolha != 1:
                raise Exception()
        except:
            print('Escolha inválida.')
        
        if escolha == 1:
            try:
                x = int(input('X:'))
                y = int(input('Y:'))
                if (x > 12 or x < -12) or (y > 12 or y < -12):
                    raise Exception()
                vertex = Vertex(id, meio_coluna - y, meio_linha + x) # parte principal
                of.addVertex(vertex)
                id += 1
                os.system('cls')
            except:
                print('Insira valores válidos. (bound (-12, 12))')
                os.system('cls')
        elif escolha == 0:
            break

def inserir_faces(qtde_elem, of):
    id = qtde_elem
    lim = len(of.listOfVertex())
    vertexs = of.listOfVertex()

    while True:
        for v in vertexs:
            print(f'ID: {v.id}, X: {v.x}, Y:{v.y}')
        try:
            print('[1] Inserir nova face.')
            print('[0] Volta para menu.')
            escolha = int(input('Escolha: '))

            os.system('cls')

            if escolha != 0 and escolha != 1:
                raise Exception()
        except:
            print('Escolha inválida.')

        if escolha == 1:
            try:
                v0 = int(input('Primeiro vertice: '))
                v1 = int(input('Segundo vertice: '))
                v2 = int(input('Terceiro vertice: '))

                if (v0 < 0 or v0 > lim) or (v1 < 0 or v1 > lim) or (v2 < 0 or v2 > lim) or (v0 == v1 or v0 == v2 or v1 == v2):
                    raise Exception()
                
                face = Face(id, vertexs[v0], vertexs[v1], vertexs[v2])
                of.addFace(face)
                id += 1
                os.system('cls')
            except:
                print('ERRO!')
                os.system('cls')
        elif escolha == 0:
            break

def exibir_sru(x, y, of, sru):
    for i in range(x):
        for j in range(y):  
            print(sru.matriz[i, j], end=' ') # precisa inverter i e j pois o numpy trata linhas e colunas diferente
        print()
    
    # Dados da estrutura
    print("Dados Pontos:")
    print("Pontos:")
    for v in of.listOfVertex():
        print("id:" + str(v.id) + " x:" + str(v.x) + " y:" + str(v.y) + " Face:" + str(v.face))
    
    print("Faces:")
    for f in of.listOfFaces():
        print("id:" + str(f.id) + " v0:" + str(f.v0.id) + " v1:" + str(f.v1.id) + " v2:" + str(f.v2.id) + " Vizinhos:(" + str(f.vizinho1) + ", " + str(f.vizinho2) + ", " + str(f.vizinho3) + ")")

    print('Coordenadas no plano cartesiano:')
    for v in of.listOfVertex():
        print("id:" + str(v.id) + " x:" + str(v.y - y // 2) + " y:" + str(-(v.x - x // 2)) + " Face:" + str(v.face))

    input('Pressione ENTER para voltar para o menu!')
    os.system('cls')

def main():
    x = 25
    y = 25

    of = Estrutura()
    encerrar = 0
    
    while True:
        if encerrar == -1:
            break
        try:
            escolha = int(input('[1] Inserir pontos.\n[2] Inserir faces.\n[3] Exibir Matriz.\n[4] Translandar.\n[5] Rotacionar.\n[0] Sair.\nEscolha: '))
            os.system('cls')

            if escolha > 6 or escolha < 0:
                raise Exception()

            match escolha:
                case 1: 
                    #desabilitado para apresentação
                    #inserir_pontos(x, y, len(of.listOfVertex()) if len(of.listOfVertex()) != 0 else 0, of)

                    #remover '#' e apagar codigo abaixo

                    meio_linha = x // 2
                    meio_coluna = y // 2

                    v0 = Vertex(0, meio_linha, meio_coluna)
                    v1 = Vertex(1, meio_coluna - 0, meio_linha + (-8))
                    v2 = Vertex(2, meio_coluna - 7, meio_linha + (-4))
                    v3 = Vertex(3, meio_coluna - 7, meio_linha + 4)
                    v4 = Vertex(4, meio_coluna - 0, meio_linha + 8)
                    v5 = Vertex(5, meio_coluna - (-7), meio_linha + 4)
                    v6 = Vertex(6, meio_coluna - (-7), meio_linha + (-4))

                    of.addVertex(v0)
                    of.addVertex(v1)
                    of.addVertex(v2)
                    of.addVertex(v3)
                    of.addVertex(v4)
                    of.addVertex(v5)
                    of.addVertex(v6)
                case 2:
                    #desabilitado para apresentação
                    #inserir_faces(len(of.listOfFaces()) if len(of.listOfFaces()) != 0 else 0, of)
                    #of.defineVizinhos()

                    #remover '#' acima e apagar codigo abaixo
                    of.addFace(Face(0, v0, v1, v2))
                    of.addFace(Face(1, v0, v2, v3))
                    of.addFace(Face(2, v0, v3, v4))
                    of.addFace(Face(3, v0, v4, v5))
                    of.addFace(Face(4, v0, v5, v6))
                    of.addFace(Face(6, v0, v6, v1))
                    of.defineVizinhos()
                case 3:
                    espaco_sru = SRU(x, y, of)
                    espaco_sru.adicionarVertexs()
                    espaco_sru.adicionarFaces()
                    espaco_sru.desenharObjeto()
                    exibir_sru(x, y, of, espaco_sru)
                case 4:
                    while True:
                        try:
                            sx = float(input('Insira o deslocamento em relação a \'x\': '))
                            sy = float(input('Insira o deslocamento em relação a \'y\': '))
                            
                            m_translandar = np.array([sx, -sy])

                            encerrar = of.translacao(m_translandar, x, y)
                        
                            break
                        except:
                            print('Tente Novamente!')
                            os.system('cls')
                case 5:
                    while True:
                        try:
                            angulo = float(input('Insira o angulo: '))
                        except:
                            print('Tente novamente!')
                            os.system('cls')

                        if angulo > 360:
                            angulo_rotacao = math.radians(angulo % 360)
                        else:
                            angulo_rotacao = math.radians(angulo)

                        matriz_rotacao = np.array([
                            [np.cos(angulo_rotacao), -np.sin(angulo_rotacao)],
                            [np.sin(angulo_rotacao), np.cos(angulo_rotacao)]])

                        encerrar = of.rotacao(matriz_rotacao, x, y)
                        break 
                case 0:
                    break
        except:
            print('Escolha Inválida!')

if __name__ == "__main__": #procura e executa o metodo main ao executar
    main()

