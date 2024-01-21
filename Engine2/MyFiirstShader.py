from glApp.PyOGApp import *
import numpy as np
from glApp.Utils import *
from OpenGL.arrays.vbo import VBO

vertex_shader = r'''
#version 330 core

void main()
{
   gl_Position = vec4(0.5, 0, 0, 1.0);
}
'''

fragment_shader = r'''
#version 330 core
out vec4 FragColor;
void main()
{
FragColor = vec4(1, 1, 0, 1.0f);
}
'''

class MyFirstShader(PyOGApp):
    def __init__(self):
        super().__init__(850, 200, 1000, 800)
        self.vao_ref = None

    def initialise(self):
        self.program_id = create_program(vertex_shader, fragment_shader)
        self.vao_ref = glGenVertexArrays(1)
        glBindVertexArray(self.vao_ref)
        glHint(GL_POINT_SMOOTH_HINT, GL_NICEST)
        glPointSize(10)

    def camera_init(self):
        pass

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self.program_id)
        glDrawArrays(GL_POINTS, 0, 1)

MyFirstShader().mainloop()