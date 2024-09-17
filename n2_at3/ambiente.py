from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Ambiente():
    def __init__(self):
        pass
    
    def draw(self):
        """Desenha um ambiente para facilitar a visualisação das formas 3D"""
        # Piso
        glPushMatrix()
        glColor3f(0.7, 0.7, 0.7)  # Cinza claro
        glBegin(GL_QUADS)
        glVertex3f(-10.0, -1.0, -10.0)
        glVertex3f(10.0, -1.0, -10.0)
        glVertex3f(10.0, -1.0, 10.0)
        glVertex3f(-10.0, -1.0, 10.0)
        glEnd()
        glPopMatrix()

        # Parede de fundo
        glPushMatrix()
        glColor3f(0.8, 0.8, 0.8)  # Cinza médio
        glBegin(GL_QUADS)
        glVertex3f(-10.0, -1.0, -10.0)
        glVertex3f(10.0, -1.0, -10.0)
        glVertex3f(10.0, 10.0, -10.0)
        glVertex3f(-10.0, 10.0, -10.0)
        glEnd()
        glPopMatrix()

        # Parede direita
        glPushMatrix()
        glColor3f(0.85, 0.85, 0.85)  # Cinza claro
        glBegin(GL_QUADS)
        glVertex3f(10.0, -1.0, -5.0)
        glVertex3f(10.0, -1.0, 5.0)
        glVertex3f(10.0, 10.0, 10.0)
        glVertex3f(10.0, 10.0, -10.0)
        glEnd()
        glPopMatrix()

        # Parede esquerda
        glPushMatrix()
        glColor3f(0.85, 0.85, 0.85)  # Cinza claro
        glBegin(GL_QUADS)
        glVertex3f(-10.0, -1.0, -10.0)
        glVertex3f(-10.0, -1.0, 10.0)
        glVertex3f(-10.0, 10.0, 10.0)
        glVertex3f(-10.0, 10.0, -10.0)
        glEnd()
        glPopMatrix()
    
    def draw_eixos(self):
        """Uma função para desenhar linhas no eixo X, Y e Z"""
        # Desenha o eixo X (vermelho)
        glBegin(GL_LINES)
        glColor3f(1.0, 0.0, 0.0) # Vermelho
        glVertex3f(-10.0, 0.0, 0.0)
        glVertex3f(10.0, 0.0, 0.0)
        glEnd()

        # Desenha o eixo Y (verde)
        glBegin(GL_LINES)
        glColor3f(0.0, 1.0, 0.0) # Verde
        glVertex3f(0.0, -10.0, 0.0)
        glVertex3f(0.0, 10.0, 0.0)
        glEnd()

        # Desenha o eixo Z (azul)
        glBegin(GL_LINES)
        glColor3f(0.0, 0.0, 1.0); # Azul
        glVertex3f(0.0, 0.0, -10.0)
        glVertex3f(0.0, 0.0, 10.0)
        glEnd()