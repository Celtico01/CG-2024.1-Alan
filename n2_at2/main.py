from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    #adicionar os códigos

    glFlush()

def fundo_tela():
    #RGBA
    return [1.0, 1.0, 1.0, 1.0]

#configura o campo de visualizaÁ„o
def confCamera():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-5, 5, -5, 5, -1, 1)  # Left, right, bottom, top, near, and far planes
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    #gluLookAt(1, 1, 2,  # Camera position
    #         0, 0, 0,  # Look-at point
    #         0, 1, 0)  # Up direction

def teclado(key : chr, posX: int, posY : int):
    if (key == 27): #//O codigo ASC da tecla ESC
        exit(1)
    
def init(cor_fundoRGBA : list):
    glClearColor (cor_fundoRGBA[0], cor_fundoRGBA[1], cor_fundoRGBA[2], cor_fundoRGBA[3])
    confCamera()
    glEnable (GL_DEPTH_TEST)

def main(width, height, WindowName, cor_fundoRGBA):
    #configurando e exibindo uma janela
    #if bool(glutInit):
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
    glutInitWindowSize(width, height)
    glutCreateWindow (WindowName)
    
    #registrando funÁ„o de callback
    glutDisplayFunc (draw)
    glutKeyboardFunc(teclado)
    #RGBA
    init(cor_fundoRGBA)
    
    #loop de tratamento de eventos
    glutMainLoop ()


if __name__ == '__main__':
    main(600, 600, 'Alan', fundo_tela())



"""1)a:
    glShadeModel(GL_FLAT)
    glBegin(GL_QUADS)

    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(-4.0, 4.0)
    glVertex2f(4.0, 4.0)
    glVertex2f(4.0, -4.0)
    glVertex2f(-4.0, -4.0)

    glEnd()

    glEnd()
"""

"""1)b1: 
    glBegin(GL_TRIANGLES)

    glVertex2f(-5.0, 0.0)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(5.0, 0.0)   
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(0.0, 5.0)
    glColor3f(1.0, 1.0, 1.0)
    
    glEnd()
"""

"""1)b2:
    glBegin(GL_TRIANGLES)

    #triangulo superior branco
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(-5.0, 0.0)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(5.0, 0.0)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(0.0, 5.0)

    #triangulo inferior suavizado com azul
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(-5.0, 0.0)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(5.0, 0.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(0.0, -5.0)

    glEnd()"""

"""1)b3:
    glShadeModel(GL_FLAT)
    glBegin(GL_LINE_STRIP)

    glColor3f(0.0, 0.0, 0.0)
    glVertex2f(-2.0, 0.0)
    glVertex2f(3.0, 3.0)
    glVertex2f(0.0, -5.0)

    glEnd()
"""

"""1)b4:
    glShadeModel(GL_SMOOTH)
    glBegin(GL_QUADS)

    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(5.0, 5.0)
    glColor3f(0.0, 0.0, 0.0)
    glVertex2f(0.0, 5.0)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(0.0, 0.0)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(5.0, 0.0)

    glEnd()
"""

"""1)c1:
    # Linhas dos eixos
    glShadeModel(GL_FLAT)
    glBegin(GL_LINES)
    
    glColor3f(0.0, 1.0, 0.2)
    glVertex2f(-5.0, 0.0)
    glVertex2f(5.0, 0.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(0.0, -5.0)

    glEnd()
    # Linhas dos eixos
    #figura
    glShadeModel(GL_FLAT)
    glBegin(GL_TRIANGLES)
    
    glColor3f(0.8, 0.3, 0.3)
    glVertex2f(0.0, 0.0)
    glVertex2f(2.5, 4.0)
    glVertex2f(5.0, 0.0)

    glEnd()
    #figura
"""

"""1)c2:
    #figura
    glShadeModel(GL_FLAT)
    glBegin(GL_LINE_STRIP)
    
    glColor3f(0.8, 0.3, 0.3)
    glVertex2f(0.0, 0.0)
    glVertex2f(2.5, 4.0)
    glVertex2f(5.0, 0.0)
    glVertex2f(0.0, 0.0)

    glEnd()
    #figura 
    # Linhas dos eixos
    glShadeModel(GL_FLAT)
    glBegin(GL_LINES)
    
    glColor3f(0.0, 1.0, 0.2)
    glVertex2f(-5.0, 0.0)
    glVertex2f(5.0, 0.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(0.0, -5.0)

    glEnd()
    # Linhas dos eixos
"""

"""1)c3:
    #figura
    glShadeModel(GL_FLAT)
    glBegin(GL_TRIANGLES)
    
    glColor3f(0.8, 0.3, 0.3)
    glVertex2f(0.0, 0.0)
    glVertex2f(-2.5, -4.0)
    glVertex2f(-5.0, 0.0)

    glEnd()
    #figura

    #figura (triangulo vazio)
    glShadeModel(GL_FLAT)
    glBegin(GL_LINE_STRIP)
    
    glColor3f(0.8, 0.3, 0.3)
    glVertex2f(0.0, 0.0)
    glVertex2f(2.5, 4.0)
    glVertex2f(5.0, 0.0)
    glVertex2f(0.0, 0.0)

    glEnd()
    #figura 

    # Linhas dos eixos
    glShadeModel(GL_FLAT)
    glBegin(GL_LINES)
    
    glColor3f(0.0, 1.0, 0.2)
    glVertex2f(-5.0, 0.0)
    glVertex2f(5.0, 0.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(0.0, -5.0)

    glEnd()
    # Linhas dos eixos
"""

"""1)c4:
    #figura
    glShadeModel(GL_FLAT)
    glBegin(GL_LINE_STRIP)

    glColor3f(0.0706, 0.0392, 0.5608)
    glVertex2f(-2.0, 4.0)
    glVertex2f(-4.0, 0.0)
    glVertex2f(-2.0, -4.0)
    glVertex2f(2.0, -4.0)
    glVertex2f(4.0, 0.0)
    glVertex2f(2.0, 4.0)

    glEnd()
    #figura 

    # Linhas dos eixos
    glShadeModel(GL_FLAT)
    glBegin(GL_LINES)
    
    glColor3f(0.0, 1.0, 0.2)
    glVertex2f(-5.0, 0.0)
    glVertex2f(5.0, 0.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(0.0, -5.0)

    glEnd()
    # Linhas dos eixos"""

"""1)d1:
    #linhas perpendiculares
    glShadeModel(GL_FLAT)
    glBegin(GL_LINES)

    glColor3f(0.0, 0.0, 0.0)
    # linha horizontal
    glVertex2f(-5.0, 2.0)
    glVertex2f(5.0, 2.0)

    # linha vertifical
    glVertex2f(2.5, -5.0)
    glVertex2f(2.5, 5.0)

    glEnd()
    #linhas perpendiculares

    # Linhas dos eixos
    glShadeModel(GL_FLAT)
    glBegin(GL_LINES)
    
    glColor3f(0.0, 1.0, 0.2)
    glVertex2f(-5.0, 0.0)
    glVertex2f(5.0, 0.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(0.0, -5.0)

    glEnd()
    # Linhas dos eixos
    #figura
    glShadeModel(GL_FLAT)
    glBegin(GL_TRIANGLES)
    
    glColor3f(0.8, 0.3, 0.3)
    glVertex2f(0.0, 0.0)
    glVertex2f(2.5, 4.0)
    glVertex2f(5.0, 0.0)

    glEnd()
    #figura
"""

"""1)d2:
    # linhas 
    glShadeModel(GL_FLAT)
    glBegin(GL_LINES)

    glColor3f(0.0, 0.0, 0.0)
    # linha horizontal
    glVertex2f(-5.0, 2.0)
    glVertex2f(5.0, 2.0)

    # linha vertifical
    glVertex2f(2.5, -5.0)
    glVertex2f(2.5, 5.0)

    glEnd()
    #linhas perpendiculares
    # linhas

    #figura
    glShadeModel(GL_FLAT)
    glBegin(GL_LINE_STRIP)
    
    glColor3f(0.8, 0.3, 0.3)
    glVertex2f(0.0, 0.0)
    glVertex2f(2.5, 4.0)
    glVertex2f(5.0, 0.0)
    glVertex2f(0.0, 0.0)

    glEnd()
    #figura 
    # Linhas dos eixos
    glShadeModel(GL_FLAT)
    glBegin(GL_LINES)
    
    glColor3f(0.0, 1.0, 0.2)
    glVertex2f(-5.0, 0.0)
    glVertex2f(5.0, 0.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(0.0, -5.0)

    glEnd()
    # Linhas dos eixos
"""

"""1)d3:
    
    #linhas
    glShadeModel(GL_FLAT)
    glBegin(GL_LINES)

    glColor3f(0.0, 0.0, 0.0)
    #triangulo do terceiro quadrante

    glVertex2f(-5.0, -2.0)
    glVertex2f(0.0, -2.0)

    glVertex2f(-2.5, -5.0)
    glVertex2f(-2.5, 0.0)

    #triangulo do primeiro quadrante

    glVertex2f(0.0, 2.0)
    glVertex2f(5.0, 2.0)

    glVertex2f(2.5, 0.0)
    glVertex2f(2.5, 5.0)

    glEnd()
    # linhas

    #figura
    glShadeModel(GL_FLAT)
    glBegin(GL_TRIANGLES)
    
    glColor3f(0.8, 0.3, 0.3)
    glVertex2f(0.0, 0.0)
    glVertex2f(-2.5, -4.0)
    glVertex2f(-5.0, 0.0)

    glEnd()
    #figura

    #figura (triangulo vazio)
    glShadeModel(GL_FLAT)
    glBegin(GL_LINE_STRIP)
    
    glColor3f(0.8, 0.3, 0.3)
    glVertex2f(0.0, 0.0)
    glVertex2f(2.5, 4.0)
    glVertex2f(5.0, 0.0)
    glVertex2f(0.0, 0.0)

    glEnd()
    #figura 

    # Linhas dos eixos
    glShadeModel(GL_FLAT)
    glBegin(GL_LINES)
    
    glColor3f(0.0, 1.0, 0.2)
    glVertex2f(-5.0, 0.0)
    glVertex2f(5.0, 0.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(0.0, -5.0)

    glEnd()
    # Linhas dos eixos
"""

"""1)e:
    # Circulo Sem preenchimento
    glShadeModel(GL_FLAT)
    glBegin(GL_LINE_LOOP) # igual ao strip mas desenha um linha entre o ultimo e o primeiro

    glColor3f(0.0, 0.0, 0.0)

    raio = 1 # raio do circulo
    centroX = -2 # posição central do circulo no eixo x
    centroY = 0 # posição central do circulo no eixo y
    numSegments = 10 # o quão preciso sera o circulo
    
    for i in range(numSegments):
        angulo = 2.0 * math.pi * i / numSegments  # Calcula o ângulo

        x = raio * math.cos(angulo) + centroX 
        y = raio * math.sin(angulo) + centroY  

        glVertex2f(x, y)

    glEnd()

    # Circulo sem preenchimento
    # Circulo com preenchimento
    glShadeModel(GL_FLAT)
    glBegin(GL_POLYGON)

    glColor3f(0.0, 0.5, 0.5)

    raio = 1 # raio do circulo
    centroX = 2 # posição central do circulo no eixo x
    centroY = 0 # posição central do circulo no eixo y
    numSegments = 10 # o quão preciso sera o circulo
    
    for i in range(numSegments):
        angulo = 2.0 * math.pi * i / numSegments  # Calcula o ângulo

        x = raio * math.cos(angulo) + centroX 
        y = raio * math.sin(angulo) + centroY  

        glVertex2f(x, y)  # Define o vértice

    glEnd()

    # Circulo com preenchimento
"""

"""1)f:
    glShadeModel(GL_FLAT)
    glBegin(GL_TRIANGLES)

    glColor3f(1.0, 0.0, 0.0)
    # up
    glVertex2f(-1.2, 3.0)
    glVertex2f(0.0, 2.0)
    glVertex2f(1.2, 3.0)
    #
    glVertex2f(0.0, 2.0)
    glVertex2f(-0.7, 2.7)
    glVertex2f(-0.7, 2.0)
    #
    glVertex2f(0.0, 2.0)
    glVertex2f(0.7, 2.7)
    glVertex2f(0.7, 2.0)
    # right
    glVertex2f(3.0, -1.2)
    glVertex2f(2.0, 0.0)
    glVertex2f(3.0, 1.2)
    #
    glVertex2f(2.0, 0.0)
    glVertex2f(2.7, -0.7)
    glVertex2f(2.0, -0.7)
    #
    glVertex2f(2.0, 0.0)
    glVertex2f(2.7, 0.7)
    glVertex2f(2.0, 0.7)
    #left
    glVertex2f(-3.0, -1.2)
    glVertex2f(-2.0, 0.0)
    glVertex2f(-3.0, 1.2)
    #
    glVertex2f(-2.0, 0.0)
    glVertex2f(-2.7, -0.7)
    glVertex2f(-2.0, -0.7)
    #
    glVertex2f(-2.0, 0.0)
    glVertex2f(-2.7, 0.7)
    glVertex2f(-2.0, 0.7)
    #down
    glVertex2f(-1.2, -3.0)
    glVertex2f(0.0, -2.0)
    glVertex2f(1.2, -3.0)
    #
    glVertex2f(0.0, -2.0)
    glVertex2f(-0.7, -2.7)
    glVertex2f(-0.7, -2.0)
    #
    glVertex2f(0.0, -2.0)
    glVertex2f(0.7, -2.7)
    glVertex2f(0.7, -2.0)

    glEnd()
    ##
    glBegin(GL_QUADS)
    
    #up 1
    glVertex2f(-0.7, 2.7)
    glVertex2f(-0.4, 2.7)
    glVertex2f(-0.4, 0.4)
    glVertex2f(-0.7, 0.4)
    #
    #up 2
    glVertex2f(0.7, 2.7)
    glVertex2f(0.4, 2.7)
    glVertex2f(0.4, 0.4)
    glVertex2f(0.7, 0.4)

    # down 1
    glVertex2f(-0.7, -2.7)
    glVertex2f(-0.4, -2.7)
    glVertex2f(-0.4, -0.4)
    glVertex2f(-0.7, -0.4)
    #
    # down 2
    glVertex2f(0.7, -2.7)
    glVertex2f(0.4, -2.7)
    glVertex2f(0.4, -0.4)
    glVertex2f(0.7, -0.4)
    
    # right 1
    glVertex2f(2.7, -0.7)
    glVertex2f(2.7, -0.4)
    glVertex2f(0.4, -0.4)
    glVertex2f(0.4, -0.7)
    #
    #right 2
    glVertex2f(2.7, 0.7)
    glVertex2f(2.7, 0.4)
    glVertex2f(0.4, 0.4)
    glVertex2f(0.4, 0.7)
    #
    # left 1
    glVertex2f(-2.7, -0.7)
    glVertex2f(-2.7, -0.4)
    glVertex2f(-0.4, -0.4)
    glVertex2f(-0.4, -0.7)
    #
    # left 2
    glVertex2f(-2.7, 0.7)
    glVertex2f(-2.7, 0.4)
    glVertex2f(-0.4, 0.4)
    glVertex2f(-0.4, 0.7)
    glEnd()
    ##
"""

"""1)g:
    glShadeModel(GL_FLAT)
    glBegin(GL_POLYGON)

    glColor3f(1.0, 0.0, 0.0)
    #corpo
    glVertex2f(-3.6, -3.2)
    glVertex2f(-2.8, -3.8)
    glVertex2f(3.881, 3.3)
    glVertex2f(3.0, 3.8)

    glEnd()
    #corpo
    #bico
    glBegin(GL_POLYGON)

    raio = 0.5 # raio do circulo
    centroX = 3.4 # posição central do circulo no eixo x
    centroY = 3.5 # posição central do circulo no eixo y
    numSegments = 100 # o quão preciso sera o circulo
    
    for i in range(numSegments):
        angulo = 2.0 * math.pi * i / numSegments  # Calcula o ângulo

        x = raio * math.cos(angulo) + centroX 
        y = raio * math.sin(angulo) + centroY  
        glColor3f(1.0, 0.0, 0.0)
        glVertex2f(x, y)  # Define o vértice
    glEnd()
    # bico

    # cauda 
    glBegin(GL_TRIANGLES)

    glVertex2f(-3.1, -3.5)
    glVertex2f(-2.8, -4.6)
    glVertex2f(-2.2, -3.1)

    glVertex2f(-3.3, -3.4)
    glVertex2f(-4.4, -3.1)
    glVertex2f(-2.8, -2.6)

    glEnd()
    # cauda

    # asa esquerda
    glBegin(GL_TRIANGLES)

    glVertex2f(-0.5, 0.0)
    glVertex2f(-4.8, 3.3)
    glVertex2f(0.5, 1.0)

    glVertex2f(-4.8, 3.3)
    glVertex2f(-3.9, 3.2)
    glVertex2f(-3.1, 2.5)

    glEnd()
    
    #motor esquerdo
    glBegin(GL_QUADS)
    
    glVertex2f(-1.9, 1.2)
    glVertex2f(-1.3, 1.2)
    glVertex2f(-0.7, 1.85)
    glVertex2f(-1.3, 2.1)

    glEnd()

    glBegin(GL_POLYGON)

    raio = 0.33 # raio do circulo
    centroX = -1.05 # posição central do circulo no eixo x
    centroY = 1.87 # posição central do circulo no eixo y
    numSegments = 100 # o quão preciso sera o circulo
    
    for i in range(numSegments):
        angulo = 2.0 * math.pi * i / numSegments  # Calcula o ângulo

        x = raio * math.cos(angulo) + centroX 
        y = raio * math.sin(angulo) + centroY  
        glColor3f(1.0, 0.0, 0.0)
        glVertex2f(x, y)  # Define o vértice
    glEnd()

    # asa esquerda

    # asa direita

    glBegin(GL_TRIANGLES)

    glVertex2f(0.0, -0.5)
    glVertex2f(3.3, -4.8)
    glVertex2f(1.0, 0.5)

    glVertex2f(3.3, -4.8)
    glVertex2f(3.2, -3.9)
    glVertex2f(2.5, -3.1)

    glEnd()

    #motor direito
    glBegin(GL_QUADS)
    
    glVertex2f(1.2, -1.9)
    glVertex2f(1.2, -1.3)
    glVertex2f(1.85, -0.7)
    glVertex2f(2.1, -1.3)

    glEnd()

    glBegin(GL_POLYGON)

    raio = 0.33 # raio do circulo
    centroX = 1.89 # posição central do circulo no eixo x
    centroY = -1.04 # posição central do circulo no eixo y
    numSegments = 100 # o quão preciso sera o circulo
    
    for i in range(numSegments):
        angulo = 2.0 * math.pi * i / numSegments  # Calcula o ângulo

        x = raio * math.cos(angulo) + centroX 
        y = raio * math.sin(angulo) + centroY  
        glColor3f(1.0, 0.0, 0.0)
        glVertex2f(x, y)  # Define o vértice
    glEnd()

    # asa direita
"""

