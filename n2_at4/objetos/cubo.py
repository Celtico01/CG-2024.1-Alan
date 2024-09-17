from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Cubo():
    def __init__(self, tamanho):
        self.tamanho = tamanho

    def draw(self):
        glutSolidCube(self.tamanho)
        
        

