from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import ambiente
room = ambiente.Ambiente()
from modelos import prisma, T
prisma = prisma.Prisma(3, 0, 0, 8)
tower_t = T.T_3D()
##
tower_t.adicionar_cor(1.0, 0.0, 0.0)
tower_t.adicionar_cor(1.0, 0.0, 0.0)
tower_t.adicionar_cor(1.0, 0.0, 0.0)
tower_t.adicionar_cor(1.0, 0.0, 0.0)
#
tower_t.adicionar_cor(0.0, 1.0, 0.0)
tower_t.adicionar_cor(0.0, 1.0, 0.0)
tower_t.adicionar_cor(0.0, 1.0, 0.0)
tower_t.adicionar_cor(0.0, 1.0, 0.0)
#
tower_t.adicionar_cor(0.0, 0.0, 1.0)
tower_t.adicionar_cor(0.0, 0.0, 1.0)
tower_t.adicionar_cor(0.0, 0.0, 1.0)
tower_t.adicionar_cor(0.0, 0.0, 1.0)
#
tower_t.adicionar_cor(1.0, 0.0, 0.0)
tower_t.adicionar_cor(1.0, 0.0, 0.0)
tower_t.adicionar_cor(1.0, 0.0, 0.0)
tower_t.adicionar_cor(1.0, 0.0, 0.0)
#
tower_t.adicionar_cor(0.0, 1.0, 0.0)
tower_t.adicionar_cor(0.0, 1.0, 0.0)
tower_t.adicionar_cor(0.0, 1.0, 0.0)
tower_t.adicionar_cor(0.0, 1.0, 0.0)
#
tower_t.adicionar_cor(0.0, 0.0, 1.0)
tower_t.adicionar_cor(0.0, 0.0, 1.0)
tower_t.adicionar_cor(0.0, 0.0, 1.0)
tower_t.adicionar_cor(0.0, 0.0, 1.0)
#
tower_t.adicionar_cor(1.0, 0.0, 0.0)
tower_t.adicionar_cor(1.0, 0.0, 0.0)
tower_t.adicionar_cor(1.0, 0.0, 0.0)
tower_t.adicionar_cor(1.0, 0.0, 0.0)
#
tower_t.adicionar_cor(0.0, 1.0, 0.0)
tower_t.adicionar_cor(0.0, 1.0, 0.0)
tower_t.adicionar_cor(0.0, 1.0, 0.0)
tower_t.adicionar_cor(0.0, 1.0, 0.0)
#
tower_t.adicionar_cor(0.0, 0.0, 1.0)
tower_t.adicionar_cor(0.0, 0.0, 1.0)
tower_t.adicionar_cor(0.0, 0.0, 1.0)
tower_t.adicionar_cor(0.0, 0.0, 1.0)
#
tower_t.adicionar_cor(1.0, 0.0, 0.0)
tower_t.adicionar_cor(1.0, 0.0, 0.0)
tower_t.adicionar_cor(1.0, 0.0, 0.0)
tower_t.adicionar_cor(1.0, 0.0, 0.0)
#
tower_t.adicionar_cor(0.0, 1.0, 0.0)
tower_t.adicionar_cor(0.0, 1.0, 0.0)
tower_t.adicionar_cor(0.0, 1.0, 0.0)
tower_t.adicionar_cor(0.0, 1.0, 0.0)
#
tower_t.adicionar_cor(0.0, 0.0, 1.0)
tower_t.adicionar_cor(0.0, 0.0, 1.0)
tower_t.adicionar_cor(0.0, 0.0, 1.0)
tower_t.adicionar_cor(0.0, 0.0, 1.0)
#
tower_t.adicionar_cor(1.0, 0.0, 0.0)
tower_t.adicionar_cor(1.0, 0.0, 0.0)
tower_t.adicionar_cor(1.0, 0.0, 0.0)
tower_t.adicionar_cor(1.0, 0.0, 0.0)

##
##### VERTICE
tower_t.adicionar_vertice(-1.0, 0.0, -1.0)
tower_t.adicionar_vertice(-1.0, 0.0, 1.0)
tower_t.adicionar_vertice(1.0, 0.0, 1.0) 
tower_t.adicionar_vertice(1.0, 0.0, -1.0)
#
tower_t.adicionar_vertice(-1.0, 5.0, -1.0)
tower_t.adicionar_vertice(-1.0, 5.0, 1.0)
tower_t.adicionar_vertice(1.0, 5.0, 1.0) 
tower_t.adicionar_vertice(1.0, 5.0, -1.0)
#
tower_t.adicionar_vertice(-1.0, 5.0, -1.0)
tower_t.adicionar_vertice(-1.0, 5.0, 1.0)
tower_t.adicionar_vertice(-4.0, 5.0, 1.0)
tower_t.adicionar_vertice(-4.0, 5.0, -1.0) 
#
tower_t.adicionar_vertice(1.0, 5.0, -1.0)
tower_t.adicionar_vertice(1.0, 5.0, 1.0)
tower_t.adicionar_vertice(4.0, 5.0, 1.0)
tower_t.adicionar_vertice(4.0, 5.0, -1.0) 
#
tower_t.adicionar_vertice(-4.0, 7.0, -1.0)
tower_t.adicionar_vertice(-4.0, 7.0, 1.0) 
tower_t.adicionar_vertice(4.0, 7.0, 1.0)
tower_t.adicionar_vertice(4.0, 7.0, -1.0)
####
tower_t.adicionar_vertice(-1.0, 0.0, -1.0)
tower_t.adicionar_vertice(-1.0, 0.0, 1.0)
tower_t.adicionar_vertice(-1.0, 5.0, 1.0)
tower_t.adicionar_vertice(-1.0, 5.0, -1.0)
####
tower_t.adicionar_vertice(1.0, 0.0, 1.0) 
tower_t.adicionar_vertice(1.0, 0.0, -1.0)
tower_t.adicionar_vertice(1.0, 5.0, -1.0)
tower_t.adicionar_vertice(1.0, 5.0, 1.0) 
####
tower_t.adicionar_vertice(-1.0, 0.0, 1.0)
tower_t.adicionar_vertice(1.0, 0.0, 1.0) 
tower_t.adicionar_vertice(1.0, 5.0, 1.0) 
tower_t.adicionar_vertice(-1.0, 5.0, 1.0)
####
####
tower_t.adicionar_vertice(-1.0, 0.0, -1.0)
tower_t.adicionar_vertice(1.0, 0.0, -1.0)
tower_t.adicionar_vertice(1.0, 5.0, -1.0)
tower_t.adicionar_vertice(-1.0, 5.0, -1.0)
####
tower_t.adicionar_vertice(-4.0, 5.0, 1.0)
tower_t.adicionar_vertice(-4.0, 5.0, -1.0) 
tower_t.adicionar_vertice(-4.0, 7.0, -1.0)
tower_t.adicionar_vertice(-4.0, 7.0, 1.0) 
####
tower_t.adicionar_vertice(4.0, 5.0, 1.0)
tower_t.adicionar_vertice(4.0, 5.0, -1.0) 
tower_t.adicionar_vertice(4.0, 7.0, -1.0)
tower_t.adicionar_vertice(4.0, 7.0, 1.0) 
####
tower_t.adicionar_vertice(-4.0, 7.0, 1.0)
tower_t.adicionar_vertice(-4.0, 5.0, 1.0)
tower_t.adicionar_vertice(4.0, 5.0, 1.0)
tower_t.adicionar_vertice(4.0, 7.0, 1.0)
####
tower_t.adicionar_vertice(-4.0, 7.0, -1.0)
tower_t.adicionar_vertice(-4.0, 5.0, -1.0)
tower_t.adicionar_vertice(4.0, 5.0, -1.0)
tower_t.adicionar_vertice(4.0, 7.0, -1.0)


def idle() -> None:
    glutPostRedisplay()

def display() -> None:
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    #draw everything or call objects
    

    glutSwapBuffers()

#keyboard settings
def key(key : chr, x : int, y : int) -> None:
    if key == b'\x1b':  # escape key
        glutLeaveMainLoop()

def ang_1(width : int, height : int):
    glViewport(0, 0, width, height)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # fovy, aspect(esticar horizontalmente), zNear (o quão perto consegue enxergar), zFar(o quão longe)
    gluPerspective(90.0, width/height, 0.1, 70.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    #angulo 1
    gluLookAt(3.0, 3.0, 8.0, # onde a camera esta
              0.0, 0.0, 0.0, # local que a camera aponta
              0.0, 1.0, 0.0) # vetor up da camera
    
def ang_2(width : int, height : int):
    glViewport(0, 0, width, height)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # fovy, aspect(esticar horizontalmente), zNear (o quão perto consegue enxergar), zFar(o quão longe)
    gluPerspective(90.0, width/height, 0.1, 70.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    #angulo 2
    gluLookAt(3.0, 6.0, 4.0, # onde a camera esta
              0.0, 0.0, 0.0, # local que a camera aponta
              0.0, 1.0, 0.0) # vetor up da camera
    
def ang_3(width : int, height : int):
    glViewport(0, 0, width, height)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # fovy, aspect(esticar horizontalmente), zNear (o quão perto consegue enxergar), zFar(o quão longe)
    gluPerspective(90.0, width/height, 0.1, 70.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    #angulo 3
    gluLookAt(4.0, -0.9, 5.0, # onde a camera esta
              0.0, 0.0, 0.0, # local que a camera aponta
              0.0, 1.0, 0.0) # vetor up da camera

def ang_4(width : int, height : int):
    glViewport(0, 0, width, height)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # fovy, aspect(esticar horizontalmente), zNear (o quão perto consegue enxergar), zFar(o quão longe)
    gluPerspective(100.0, width/height, 0.1, 70.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    #angulo 4
    gluLookAt(3.0, 3.0, -8.0, # onde a camera esta
              0.0, 0.0, 0.0, # local que a camera aponta
              0.0, 1.0, 0.0) # vetor up da camera

def main(width, height, window_name):
    glutInit()
    glutInitWindowSize(width, height)
    glutInitWindowPosition(750, 100)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutCreateWindow(window_name)

    glutDisplayFunc(display)
    glutKeyboardFunc(key)
    glutIdleFunc(idle)

    #cor de fundo RGBA
    glClearColor(0.0, 0.0, 0.0, 1.0)

    #habilitando algumas coisas
    glEnable(GL_DEPTH_TEST)

    glutMainLoop()

if __name__ == '__main__':
    main(600, 600, 'Alan')

"""
    glPushMatrix()
    glRotatef(-90, 1, 0, 0)
    glutWireCone(3, 4, 50, 50)
    glPopMatrix()
"""