from OpenGL.GL import *
#from OpenGL.GLUT import *
#from OpenGL.GLU import *
from PIL import Image
from PIL.Image import Transpose
import os

class Casa():
    def __init__(self, comprimento, altura, profundidade):
        self.comprimento = comprimento
        self.altura = altura
        self.profundidade = profundidade

    def draw(self):
        glBegin(GL_QUADS)
    
        # Piso
        glNormal3f(0.0, -1.0, 0.0)
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(-self.comprimento, 0, -self.profundidade)
        glVertex3f(self.comprimento, 0, -self.profundidade)
        glVertex3f(self.comprimento, 0, self.profundidade)
        glVertex3f(-self.comprimento, 0, self.profundidade)
        
        # Teto
        glNormal3f(0.0, -1.0, 0.0)
        glColor3f(0.0, 1.0, 1.0)
        glVertex3f(-self.comprimento, self.altura, -self.profundidade)
        glVertex3f(self.comprimento, self.altura, -self.profundidade)
        glVertex3f(self.comprimento, self.altura, self.profundidade)
        glVertex3f(-self.comprimento, self.altura, self.profundidade)
        
        # Parede de trás
        glNormal3f(0.0, 0.0, 1.0)
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(-self.comprimento, 0, -self.profundidade)
        glVertex3f(self.comprimento, 0, -self.profundidade)
        glVertex3f(self.comprimento, self.altura, -self.profundidade)
        glVertex3f(-self.comprimento, self.altura, -self.profundidade)
        
        # Parede da frente
        glNormal3f(0.0, 0.0, -1.0)
        glColor3f(0.0, 0.0, 1.0)        
        glVertex3f(-self.comprimento, 0, self.profundidade)
        glVertex3f(self.comprimento, 0, self.profundidade)
        glVertex3f(self.comprimento, self.altura, self.profundidade)
        glVertex3f(-self.comprimento, self.altura, self.profundidade)
        
        # Parede esquerda
        glNormal3f(-1.0, 0.0, 0.0)
        glColor3f(1.0, 1.0, 0.0)
        glVertex3f(-self.comprimento, 0, -self.profundidade)
        glVertex3f(-self.comprimento, 0, self.profundidade)
        glVertex3f(-self.comprimento, self.altura, self.profundidade)
        glVertex3f(-self.comprimento, self.altura, -self.profundidade)
        
        # Parede direita
        glNormal3f(1.0, 0.0, 0.0)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f(self.comprimento, 0, -self.profundidade)
        glVertex3f(self.comprimento, 0, self.profundidade)
        glVertex3f(self.comprimento, self.altura, self.profundidade)
        glVertex3f(self.comprimento, self.altura, -self.profundidade)
        
        glEnd()

    def draw_eixos(self):
        """Uma função para desenhar linhas no eixo X, Y e Z"""
        # Desenha o eixo X (vermelho)
        glBegin(GL_LINES)
        glColor3f(1.0, 1.0, 0.0) # Vermelho
        glVertex3f(-11.0, 1.0, 1.0)
        glVertex3f(11.0, 1.0, 1.0)
        glEnd()

        # Desenha o eixo Y (verde)
        glBegin(GL_LINES)
        glColor3f(0.0, 1.0, 0.0) # Verde
        glVertex3f(1.0, -11.0, 1.0)
        glVertex3f(1.0, 11.0, 1.0)
        glEnd()

        # Desenha o eixo Z (azul)
        glBegin(GL_LINES)
        glColor3f(0.0, 0.0, 1.0); # Azul
        glVertex3f(1.0, 1.0, -11.0)
        glVertex3f(1.0, 1.0, 11.0)
        glEnd()

class Quadro():
    def __init__(self, texture_path, posX, posY, posZ):
        self.posX = posX
        self.posY = posY
        self.posZ = posZ

        self.texture_id = glGenTextures(1) 
        glBindTexture(GL_TEXTURE_2D, self.texture_id)

        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

        image = Image.open(texture_path)
        image = image.convert('RGBA')
        image_data = image.transpose(Transpose.FLIP_TOP_BOTTOM).tobytes()

        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, image.width, image.height, 0, GL_RGB, GL_UNSIGNED_BYTE, image_data)

    def draw_quadro_na_parede(self):
        """ Desenha um quadro em uma das paredes e aplica uma textura """

        if self.texture_id is not None:
            glEnable(GL_TEXTURE_2D)
            glBindTexture(GL_TEXTURE_2D, self.texture_id)

            glPushMatrix()
            glTranslatef(self.posX, self.posY, self.posZ)  # Um pouco à frente da parede
            glScalef(2.0, 1.0, 0.1)  # Quadro retangular

            glBegin(GL_QUADS)
            glTexCoord2f(0.0, 0.0)
            glVertex3f(-0.5, -0.5, 0.0)
            glTexCoord2f(1.0, 0.0)
            glVertex3f(0.5, -0.5, 0.0)
            glTexCoord2f(1.0, 1.0)
            glVertex3f(0.5, 0.5, 0.0)
            glTexCoord2f(0.0, 1.0)
            glVertex3f(-0.5, 0.5, 0.0)
            glEnd()

            glPopMatrix()

            glDisable(GL_TEXTURE_2D)
    