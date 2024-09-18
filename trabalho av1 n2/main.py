import sys
import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from modelos.base_e_eixos import BaseEixo

base_eixo = BaseEixo(4, 50)

#path_imagens = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'imagens')

angle_light = 0.0

SWITCH = False

WIDTH, HEIGHT = 800, 600

LIGHT_POS_X = 0.0
LIGHT_POS_Y = 1.5
LIGHT_POS_Z = 0.0

CAM_POS_X = 1.0
CAM_POS_Y = 2.5
CAM_POS_Z = 1.0

LOOK_AT_X = 0.0
LOOK_AT_Y = 0.0
LOOK_AT_Z = 0.0

LUZ_AMBIENTE = (0.02, 0.02, 0.02, 1.0)
LUZ_DIFUSA = (0.6, 0.6, 0.6, 1.0)
LUZ_ESPECULAR = (1.0, 1.0, 1.0, 1.0)
ATENUACAO_CONSTANTE = 1.0
ATENUACAO_LINEAR = 1.0
ATENUACAO_QUADRATICA = 0.1
SHININESS = 64


def init_light():
    glEnable(GL_DEPTH_TEST)
    #
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    #
    glEnable(GL_COLOR_MATERIAL)
    #
    
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, LUZ_AMBIENTE)
    glLight(GL_LIGHT0, GL_DIFFUSE, LUZ_DIFUSA)
    glLight(GL_LIGHT0, GL_SPECULAR, LUZ_ESPECULAR)
    
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, ATENUACAO_CONSTANTE)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, ATENUACAO_LINEAR)
    glLightf(GL_LIGHT0, GL_QUADRATIC_ATTENUATION, ATENUACAO_QUADRATICA)

    glMaterial(GL_FRONT, GL_DIFFUSE, LUZ_DIFUSA)
    glMaterial(GL_FRONT, GL_SPECULAR, LUZ_ESPECULAR)
    glMaterial(GL_FRONT, GL_SHININESS, SHININESS)    

def idle():
    glutPostRedisplay()

def display():
    global angle_light, SWITCH
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    cam()

    if SWITCH:
        glEnable(GL_LIGHT0)
        light_pos = (LIGHT_POS_X, LIGHT_POS_Y, LIGHT_POS_Z, 1.0)
        glLight(GL_LIGHT0, GL_POSITION, light_pos)

        glPushMatrix()
        glTranslatef(LIGHT_POS_X, LIGHT_POS_Y, LIGHT_POS_Z)
        glRotated(180, 0, 1, 1)
        glColor3f(1.0, 1.0, 0.0)
        glutSolidCone(0.3, 1.0, 100, 100)
        glPopMatrix()
    else:
        glDisable(GL_LIGHT0)
    

    base_eixo.draw_base()
    base_eixo.draw_eixos()

    # draw objetos abaixo !
    base_eixo.draw_objetos_plano()

    glutSwapBuffers()

def key(key : chr, x : int, y : int):
    global CAM_POS_X, CAM_POS_Y, CAM_POS_Z
    global LOOK_AT_X, LOOK_AT_Y, LOOK_AT_Z
    global LIGHT_POS_X, LIGHT_POS_Y, LIGHT_POS_Z
    global SWITCH

    match key:
        case b'\x1b':
            glutLeaveMainLoop()
        case b's':
            SWITCH = not SWITCH
        case b'X':
            CAM_POS_X += 0.1
        case b'x':
            CAM_POS_X -= 0.1
        case b'C':
            CAM_POS_Y += 0.1
        case b'c':
            CAM_POS_Y -= 0.1
        case b'V':
            CAM_POS_Z += 0.1
        case b'v':
            CAM_POS_Z -= 0.1
        case b'D':
            LOOK_AT_X += 0.1
        case b'd':
            LOOK_AT_X -= 0.1
        case b'F':
            LOOK_AT_Y += 0.1
        case b'f':
            LOOK_AT_Y -= 0.1
        case b'G':
            LOOK_AT_Z += 0.1
        case b'g':
            LOOK_AT_Z -= 0.1
        case b'E':
            LIGHT_POS_X += 0.1
        case b'e':
            LIGHT_POS_X -= 0.1
        case b'R':
            LIGHT_POS_Y += 0.1
        case b'r':
            LIGHT_POS_Y -= 0.1
        case b'T':
            LIGHT_POS_Z += 0.1
        case b't':
            LIGHT_POS_Z -= 0.1

def cam():
    global CAM_POS_X, CAM_POS_Y, CAM_POS_Z
    global LOOK_AT_X, LOOK_AT_Y, LOOK_AT_Z

    glViewport(0, 0, WIDTH, HEIGHT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(110.0, WIDTH / HEIGHT, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(CAM_POS_X, CAM_POS_Y, CAM_POS_Z,
              LOOK_AT_X, LOOK_AT_Y, LOOK_AT_Z,
                 0.0   ,     1.0   ,    0.0   )

def main(windowName):
    glutInit(sys.argv)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutInitWindowPosition((1366 - WIDTH) // 2, (768 - HEIGHT) // 2)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutCreateWindow(windowName)
    
    print("Renderer:", glGetString(GL_RENDERER))
    print("OpenGL version supported:", glGetString(GL_VERSION))

    glutDisplayFunc(display)
    glutKeyboardFunc(key)
    glutIdleFunc(idle)

    #cor de fundo RGBA
    glClearColor(0.0, 0.0, 0.0, 1.0)

    #habilitando algumas coisas
    glEnable(GL_DEPTH_TEST)
    init_light()

    glutMainLoop()

if __name__ == "__main__":
    main('Trabalho AV1N2')
