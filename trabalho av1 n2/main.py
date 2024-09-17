import sys
import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from modelos.casa import Casa, Quadro

path_imagens = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'imagens')

angle_light = 0.0

SWITCH = False

WIDTH, HEIGHT = 800, 600

LIGHT_POS_X = 0.0
LIGHT_POS_Y = 0.0
LIGHT_POS_Z = 0.0

CAM_POS_X = 3.0
CAM_POS_Y = 3.0
CAM_POS_Z = 3.0

LOOK_AT_X = 0.0
LOOK_AT_Y = 3.0
LOOK_AT_Z = 0.0

casa = Casa(10, 10, 10)
#quadro_vasco = Quadro(os.path.join(path_imagens, 'vasco.png'), -9.9, 5.0, 0.0)

def init_light():
    glEnable(GL_DEPTH_TEST)
    #
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    
    ambient_light_global = (0.05, 0.05, 0.05, 1.0)  # Intensidade e cor da luz ambiente global
    #glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient_light_global)
    glLight(GL_LIGHT0, GL_AMBIENT, ambient_light_global)
    #glLight(GL_LIGHT0, GL_POSITION, (1.0, 1.0, 1.0, 0.0))
    glLight(GL_LIGHT0, GL_DIFFUSE, (0.6, 0.6, 0.6, 1.0))
    glLight(GL_LIGHT0, GL_SPECULAR, (1.0, 1.0, 1.0, 1.0))

    glMaterial(GL_FRONT_AND_BACK, GL_DIFFUSE, (0.6, 0.6, 0.6, 1.0))
    glMaterial(GL_FRONT_AND_BACK, GL_SPECULAR, (1.0, 1.0, 1.0, 1.0))
    glMaterial(GL_FRONT_AND_BACK, GL_SHININESS, 50.0)

def idle():
    glutPostRedisplay()

def display():
    global angle_light, SWITCH
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    cam()

    if SWITCH:
        init_light()

        glPushMatrix()
        glTranslatef(LIGHT_POS_X, LIGHT_POS_Y, LIGHT_POS_Z)
        glutWireSphere(0.5, 10, 10)
        light_pos = (LIGHT_POS_X, LIGHT_POS_Y, LIGHT_POS_Z, 1.0)
        glLight(GL_LIGHT0, GL_POSITION, light_pos)
        glPopMatrix()
    else:
        glDisable(GL_LIGHTING)
        glDisable(GL_LIGHT0)
    
    #casa.draw()
    casa.draw_eixos()
    #quadro_vasco.draw_quadro_na_parede()
    glutSolidCube(10)

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
    

    glutDisplayFunc(display)
    glutKeyboardFunc(key)
    glutIdleFunc(idle)

    #cor de fundo RGBA
    glClearColor(0.0, 0.0, 0.0, 1.0)

    #habilitando algumas coisas
    glEnable(GL_DEPTH_TEST)

    glutMainLoop()

if __name__ == "__main__":
    main('Alan')
