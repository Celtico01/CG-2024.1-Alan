from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

class Prisma():
    def __init__(self, raio_base : float, centroX : float = 0, centroZ : float = 0, numSegments : int = 8):
        self.base_raio = raio_base
        self.centroX = centroX
        self.centroZ = centroZ
        self.numSegments = numSegments 

    def draw(self) -> None:
        
        glShadeModel(GL_SMOOTH)
        #parte de cima
        glBegin(GL_TRIANGLE_FAN)

        glColor3f(1.0, 1.0, 0.0)
        glVertex3f(0.0, 4.0, 0.0)

        for i in range(self.numSegments):
            angulo = 2.0 * math.pi * i / self.numSegments

            x = self.base_raio * math.cos(angulo) + self.centroX 
            z = self.base_raio * math.sin(angulo) + self.centroZ

            glColor3f(0.0, 1.0, 1.0)
            glVertex3f(x, 0.0, z)

            if i == 0:
                aux_x = x
                aux_z = z
            
            if i == 7:
                glColor3f(0.0, 1.0, 1.0)
                glVertex3f(aux_x, 0.0, aux_z)

        glEnd()
        #
        #base
        glBegin(GL_POLYGON)
        
        for i in range(self.numSegments):
            angulo = 2.0 * math.pi * i / self.numSegments

            x = self.base_raio * math.cos(angulo) + self.centroX 
            z = self.base_raio * math.sin(angulo) + self.centroZ

            glColor3f(1.0, 0.0, 1.0)
            glVertex3f(x, 0.0, z)

        glEnd()