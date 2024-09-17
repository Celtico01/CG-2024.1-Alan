class Vertex:
    def __init__(self, id, x, y, face=None):
        self.id = id
        self.x = x
        self.y = y
        self.face = face
        self.proximo = None

#No do vertex