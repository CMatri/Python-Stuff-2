import numpy as np
from vispy import app, gloo

fragment = """
varying vec4 v_color;

void main()
{
    gl_FragColor = v_color;
}
"""

vertex = """
uniform float scale;
attribute vec2 position;
attribute vec4 color;
varying vec4 v_color;

void main()
{
    gl_Position = vec4(position, 0.0, 1.0);
    v_color = color;
}
"""

class Canvas(app.Canvas):
    def __init__(self):
        app.Canvas.__init__(self, size=(512, 512), title='scaling quad',
                            keys='interactive')
        program = gloo.Program(vert=vertex, frag=fragment, count=4)
        program['position'] = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        program['color'] = [(1, 0, 0, 1),
                            (0, 1, 0, 1),
                            (0, 0, 1, 1),
                            (1, 1, 0, 1)]
        program['scale'] = 1.0
        self.program = program

        gloo.set_viewport(0, 0, *self.physical_size)

        self.clock = 0.0
        self.timer = app.Timer('auto', self.on_timer)
        self.timer.start()
        self.show()
    
    @staticmethod
    def on_resize(event):
        gloo.set_viewport(0, 0, *event.physical_size)

    def on_draw(self, event):
        gloo.set_clear_color('white')
        gloo.clear()
        self.program.draw('triangle_strip')

    def on_timer(self, event):
        self.clock += 0.01 * np.pi
        self.program['scale'] = 0.5 + 0.5 * np.cos(self.clock)
        self.update()

c = Canvas()
app.run()