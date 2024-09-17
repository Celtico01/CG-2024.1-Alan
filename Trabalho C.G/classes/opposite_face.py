import numpy as np

class Estrutura:
    def __init__(self):
        self.primeiroVertex = None
        self.ultimoVertex = None
        self.sizeVertex = 0
        self.primeiroFace = None
        self.ultimoFace = None
        self.sizeFace = 0

    def addVertex(self, noVertex):
        if noVertex is None:
            return
        elif self.sizeVertex == 0:
            self.primeiroVertex = noVertex
            self.ultimoVertex = noVertex
            self.sizeVertex += 1
        else:
            self.ultimoVertex.proximo = noVertex
            self.ultimoVertex = noVertex
            self.sizeVertex += 1

    def addFace(self, noFace):
        if noFace is None:
            return
        elif self.sizeFace == 0:
            self.primeiroFace = noFace
            self.ultimoFace = noFace
            self.sizeFace += 1
        else:
            self.ultimoFace.proximo = noFace
            self.ultimoFace = noFace
            self.sizeFace += 1

        #atualiza as faces incidentes dos vertexs
        noFace.v0.face = noFace.id
        noFace.v1.face = noFace.id
        noFace.v2.face = noFace.id

    def defineVizinhos(self):
        faces = self.listOfFaces()
        for f1 in faces:
            v0 = f1.v0
            v1 = f1.v1
            v2 = f1.v2
            for f2 in faces:
                if f2 != f1:
                    if (f2.v0 == v0 or f2.v1 == v0 or f2.v2 == v0) and (f2.v0 == v1 or f2.v1 == v1 or f2.v2 == v1):
                        f1.vizinho1 = f2.id
                    elif (f2.v0 == v1 or f2.v1 == v1 or f2.v2 == v1) and (f2.v0 == v2 or f2.v1 == v2 or f2.v2 == v2):
                        f1.vizinho2 = f2.id
                    elif (f2.v0 == v2 or f2.v1 == v2 or f2.v2 == v2) and (f2.v0 == v0 or f2.v1 == v0 or f2.v2 == v0):
                        f1.vizinho3 = f2.id

    def listOfVertex(self):
        if self.sizeVertex == 0:
            return []
        aux = self.primeiroVertex
        listVertex = []
        while aux != None:
            listVertex.append(aux)
            aux = aux.proximo
        return listVertex

    def listOfFaces(self):
        if self.sizeFace == 0:
            return []
        aux = self.primeiroFace
        listFace = []
        while aux != None:
            listFace.append(aux)
            aux = aux.proximo
        return listFace

    def translacao(self, matriz_t, x, y):
        aux = self.primeiroVertex

        while aux != None:
            try:
                xn = aux.x - x // 2
                yn = aux.y - y // 2

                m = np.array([xn, yn])

                fn = m + matriz_t

                aux.x = int(fn[0] + x // 2)
                aux.y = int(fn[1] + y // 2)

                if aux.x > x - 1 or aux.x < 0 or aux.y > y - 1 or aux.y < 0:
                    raise Exception('Terminate')

                print(fn[0] + x // 2)
                print(fn[1] + y // 2)

                aux = aux.proximo
            except:
                print('Index out of bounds!')
                input('O programa será encerrado após você apertar ENTER.')
                return -1
            
        
    def rotacao(self, matriz_r, x, y):
        aux = self.primeiroVertex

        while aux != None:
            try:
                xn = aux.x - x // 2
                yn = aux.y - y // 2

                m = np.array([xn, yn])

                fn = np.dot(m, matriz_r)
                aux.x = int(fn[0] + x // 2)
                aux.y = int(fn[1] + y // 2)

                if aux.x > x - 1 or aux.x < 0 or aux.y > y - 1 or aux.y < 0:
                    raise Exception('Terminate')
                aux = aux.proximo
            except:
                print('Index out of bounds!')
                input('O programa será encerrado após você apertar ENTER.')
                return -1