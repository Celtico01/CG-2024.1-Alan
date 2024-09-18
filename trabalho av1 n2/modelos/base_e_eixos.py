from OpenGL.GL import *
from OpenGL.GLUT import *
import random

class BaseEixo():
    def __init__(self, tamanho_base : int, subdivisoes : int):
        self.tamanho_base = tamanho_base
        self.subdivisoes = subdivisoes
        self.angulo_rot = 0.0

        self.objetos = []
        i = -self.tamanho_base
        while i < self.tamanho_base:
            j = -self.tamanho_base
            while j < self.tamanho_base:
                objeto_aleatorio = random.randint(0, 4)
                posicao = (i, j)
                self.objetos.append((objeto_aleatorio, posicao))  # Armazena o tipo e a posição do objeto
                j += 1
            i += 1

    def draw_base(self):
        step = (2 * self.tamanho_base) /  self.subdivisoes  # Tamanho de cada subquadrado
        
        glBegin(GL_QUADS)
        
        for i in range(self.subdivisoes):
            for j in range( self.subdivisoes):
                
                x1 = -self.tamanho_base + i * step
                z1 = -self.tamanho_base + j * step
                x2 = x1 + step
                z2 = z1 + step
                
                glColor3f(1.0, 1.0, 1.0)

                # Define a normal
                glNormal3f(0.0, 1.0, 0.0)

                # Desenha o subquadrado
                glVertex3f(x1, 0.0, z1)
                glVertex3f(x2, 0.0, z1)
                glVertex3f(x2, 0.0, z2)
                glVertex3f(x1, 0.0, z2)
        
        glEnd()

    def draw_eixos(self):
        glBegin(GL_LINES)
        
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(-self.tamanho_base - 5, 0.0, 0.0)
        glVertex3f(self.tamanho_base + 5, 0.0, 0.0)

        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(0.0, -self.tamanho_base - 5, 0.0)
        glVertex3f(0.0, self.tamanho_base + 5, 0.0)

        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(0.0, 0.0, -self.tamanho_base - 5)
        glVertex3f(0.0, 0.0, self.tamanho_base + 5)

        glEnd()

    def draw_objetos_plano(self):
        self.angulo_rot += 0.5
        if self.angulo_rot >= 360:
            self.angulo_rot -= 360
        
        for objeto, (i, j) in self.objetos:
            glPushMatrix()
            glTranslatef(i, 0.3, j)

            glRotatef(self.angulo_rot, 1.0, 1.0, 1.0)

            match objeto:
                case 0:
                    glColor3f(1.0, 0.0, 0.0)
                    glutSolidCone(0.5, 0.5, self.subdivisoes, self.subdivisoes)
                case 1:
                    glColor3f(0.0, 1.0, 0.0)
                    glutSolidCylinder(0.5, 0.5, self.subdivisoes, self.subdivisoes)
                case 2:
                    glColor3f(0.0, 0.0, 1.0)
                    glutSolidSphere(0.5, self.subdivisoes, self.subdivisoes)
                case 3:
                    glColor3f(1.0, 1.0, 0.0)
                    glutSolidTeapot(0.5)
                case 4:
                    glColor3f(0.0, 1.0, 1.0)
                    glutSolidTorus(0.25, 0.5, self.subdivisoes, self.subdivisoes)

            glPopMatrix()


