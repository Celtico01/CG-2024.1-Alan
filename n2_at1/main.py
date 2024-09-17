from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    #desenhando o plano cartesiano 3D
    glBegin (GL_LINES)
    # eixo X
    glColor3f ( 0.0, 0.0, 0.0)
    glVertex3f(-2.0, 0.0, 0.0)
    glColor3f ( 1.0, 0.0, 0.0)
    glVertex3f( 2.0, 0.0, 0.0)
    # eixo Y
    glColor3f (0.0, 0.0, 0.0)
    glVertex3f(0.0,-2.0, 0.0)
    glColor3f (0.0, 1.0, 0.0)
    glVertex3f(0.0, 2.0, 0.0)
    # eixo Z
    glColor3f (0.0,  0.0, 0.0)
    glVertex3f(0.0,  0.0,-2.0)
    glColor3f (0.0,  0.0, 1.0)
    glVertex3f(0.0,  0.0, 2.0)
    glEnd ()
    
    # desenhando um cubo com linhas brancas
    glColor3f (1.0, 1.0, 1.0)
    glutWireCube (1.5)
    
    glFlush ()

#configura o campo de visualizaÁ„o
def confCamera ():
    glMatrixMode (GL_PROJECTION)
    glLoadIdentity ()
    gluPerspective(45,1.0, 0.1, 10)
    #glOrtho (-2, 2, -2, 2, 1, 5)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity ()
    gluLookAt (1,1,2, 0,0,0, 0,1,0)

def teclado(key : chr, posX: int, posY : int):
    if (key == 27): #//O codigo ASC da tecla ESC
        exit(1)
    
def init ():
    glClearColor (0.0, 0.0, 0.0, 0.0)
    confCamera ()
    glEnable (GL_DEPTH_TEST)

def main(width, height):
    #configurando e exibindo uma janela
    #if bool(glutInit):
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
    glutInitWindowSize(width, height)
    glutCreateWindow ("Fº Alan R. Mesquita")
    
    #registrando funÁ„o de callback
    glutDisplayFunc (draw)
    
    #callback que responde pelo teclado
    glutKeyboardFunc(teclado)
    
    #inicializaÁ„o das vari·veis de estado
    init ()
    
    #loop de tratamento de eventos
    glutMainLoop ()


if __name__ == '__main__':
    main(800, 600)
