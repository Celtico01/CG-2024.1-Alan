class Face:
    def __init__(self, id, v0, v1, v2, vizinhos1=-1, vizinhos2=-1, vizinhos3=-1): #EX: vizinhos3=-1 caso o usuario não passe nd inicializa como -1
        self. id = id
        self.v0 = v0
        self.v1 = v1
        self.v2 = v2
        self.vizinho1 = vizinhos1
        self.vizinho2 = vizinhos2
        self.vizinho3 = vizinhos3
        self.proximo = None

# No da face