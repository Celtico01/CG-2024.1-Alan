from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import random

class T_3D():
    def __init__(self):
        self.estrutura = []
        self.cores = []

    def draw(self):
        glShadeModel(GL_SMOOTH)
        #glBegin(GL_POINTS)
        glBegin(GL_QUADS)

        for vertice, cor in zip(self.estrutura, self.cores):
            glColor3f(cor.r, cor.g, cor.b)
            glVertex3f(vertice.x, vertice.y, vertice.z)
        
        glEnd()

    def adicionar_vertice(self, x, y, z):
        self.estrutura.append(noVertice(x, y, z))

    def adicionar_cor(self, r, g, b):
        self.cores.append(noCor(r, g, b))

class noVertice():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class noCor():
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b