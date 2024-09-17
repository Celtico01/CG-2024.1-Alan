from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from objetos import losango, cubo

losango = losango.Losango()
cubo = cubo.Cubo(1)

WIDTH = 600
HEIGHT = 600
CAM_SPEED = 0.1

CAM_X = 1.0
CAM_Y = 1.0
CAM_Z = 1.0

trans_pos_x = 0.0
trans_pos_y = 0.0
trans_pos_z = 0.0
rot_ang_x = 0.0
rot_ang_y = 0.0
rot_ang_z = 0.0
scale_eixo_x = 1.0
scale_eixo_y = 1.0
scale_eixo_z = 1.0
# c
scale_objetos = [1.0, 1.0, 1.0]
# c
# d
espelhar_x = False
espelhar_y = False
# d
def letra_c():
    glPushMatrix()
    glTranslatef(-2.0, 0.0, 0.0)
    glScalef(scale_objetos[0], scale_objetos[0], scale_objetos[0])
    glutSolidCube(0.5)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0, 0.0, 0.0)
    glScalef(scale_objetos[1], scale_objetos[1], scale_objetos[1])
    glutSolidSphere(0.5, 20, 20)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(2.0, 0.0, 0.0)
    glScalef(scale_objetos[2], scale_objetos[2], scale_objetos[2])
    glutSolidTorus(0.2, 0.5, 20, 20)
    glPopMatrix()

def triangulo_d():
    glShadeModel(GL_FLAT)

    glBegin(GL_TRIANGLES)
    
    glVertex2f(-1.0, 0.0)
    glVertex2f(0.0, 1.5)
    glVertex2f(1.0, 0.0)

    glEnd()

def letra_d():
    #glColor3f(1.0, 0.0, 0.0)
    #triangulo_d()

    if espelhar_x:
        glPushMatrix()
        glScalef(-1, 1, 1)
        glColor3f(0.0, 1.0, 0.0)
        triangulo_d()
        glPopMatrix()
    
    if espelhar_y:
        glPushMatrix()
        glScalef(1, -1, 1)
        glColor3f(0.0, 0.0, 1.0)
        triangulo_d()
        glPopMatrix()
        
def letra_e():

    glPushMatrix()
    glColor3f(0.0, 0.8, 0.8)
    glTranslatef(0.0, 0.0, 0.0)
    glutSolidSphere(0.7, 100, 100)
    glPopMatrix()
    
def idle() -> None:
    glutPostRedisplay()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    cam()

    glBegin(GL_LINES)

    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(-5.0, 0.0, 0.0)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(5.0, 0.0, 0.0)

    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(0.0,-5.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, 5.0, 0.0)

    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0,-5.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, 5.0)
    glEnd()
    
    glTranslatef(trans_pos_x, trans_pos_y, trans_pos_z)
    glScalef(scale_eixo_x, scale_eixo_y, scale_eixo_z)
    glRotatef(rot_ang_x, 1, 0, 0)
    glRotatef(rot_ang_y, 0, 1, 0)
    glRotatef(rot_ang_z, 0, 0, 1)

    # draw here

    glutSwapBuffers()

def key (key : chr, x : int, y : int):
    global CAM_X, CAM_Y, CAM_Z
    global trans_pos_x, trans_pos_y, trans_pos_z
    global rot_ang_x, rot_ang_y, rot_ang_z
    global scale_eixo_x, scale_eixo_y, scale_eixo_z
    global scale_objetos
    global espelhar_x, espelhar_y

    match key:
        case b'1':
            scale_objetos[0] += 0.1
        case b'2':
            scale_objetos[1] += 0.1
        case b'3': 
            scale_objetos[2] += 0.1
        case b'4':
            espelhar_x = not espelhar_x
        case b'5':
            espelhar_y = not espelhar_y
        case b'\x1b':
            glutLeaveMainLoop()
        case b'X':
            CAM_X += CAM_SPEED
        case b'x':
            CAM_X -= CAM_SPEED
        case b'C':
            CAM_Y += CAM_SPEED
        case b'c':
            CAM_Y -= CAM_SPEED
        case b'Z':
            CAM_Z += CAM_SPEED
        case b'z':
            CAM_Z -= CAM_SPEED
        case b'A':
            trans_pos_x += 0.1
        case b'a':
            trans_pos_x -= 0.1
        case b'S':
            trans_pos_y += 0.1
        case b's':
            trans_pos_y -= 0.1
        case b'D':
            trans_pos_z += 0.1
        case b'd':
            trans_pos_z -= 0.1
        case b'Q':
            rot_ang_x += 1.0
        case b'q':
            rot_ang_x -= 1.0
        case b'W':
            rot_ang_y += 1.0
        case b'w':
            rot_ang_y -= 1.0
        case b'E':
            rot_ang_z += 1.0
        case b'e':
            rot_ang_z -= 1.0
        case b'R':
            scale_eixo_x += 0.1
        case b'r':
            scale_eixo_x -= 0.1
        case b'F':
            scale_eixo_y += 0.1
        case b'f':
            scale_eixo_y -= 0.1
        case b'V':
            scale_eixo_z += 0.1
        case b'v':
            scale_eixo_z -= 0.1
        
def cam():
    global CAM_X, CAM_Y, CAM_Z

    glViewport(0, 0, WIDTH, HEIGHT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(90, WIDTH / HEIGHT, 0.1, 100)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(CAM_X, CAM_Y, CAM_Z,
              0    , 0    , 0    ,
              0    , 1    , 0    )

def main(windowName):
    glutInit(sys.argv)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutInitWindowPosition(750, 100)
    glutInitDisplayMode(GLUT_RGBA | GLUT_SINGLE)
    glutCreateWindow(windowName)

    glutDisplayFunc(display)
    glutKeyboardFunc(key)
    glutIdleFunc(idle)

    #cor de fundo RGBA
    glClearColor(0.0, 0.0, 0.0, 1.0)
    cam()
    #habilitando algumas coisas
    glEnable(GL_DEPTH_TEST)
    
    glutMainLoop()

if __name__ == "__main__":
    main('Alan')