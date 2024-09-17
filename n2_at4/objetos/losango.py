from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Losango():
    def __init__(self):
        self.cor1 = (0.0, 1.0, 0.0)
        self.cor2 = (0.0, 0.0, 1.0)
        self.corInterm = (0.0, 0.5, 0.5)

    def draw(self):
        glShadeModel(GL_SMOOTH)

        glBegin(GL_TRIANGLES)
        glColor3fv(self.cor1)
        glVertex3f(0.0, -3.0, 0.0)
        glColor3fv(self.corInterm)
        glVertex3f(-3.0, 0.0, 0.0)
        glColor3fv(self.corInterm)
        glVertex3f(3.0, 0.0, 0.0)
        glColor3fv(self.corInterm)
        glVertex3f(3.0, 0.0, 0.0)
        glColor3fv(self.corInterm)
        glVertex3f(-3.0, 0.0, 0.0)
        glColor3fv(self.cor2)
        glVertex3f(0.0, 3.0, 0.0)

        glEnd()
        
