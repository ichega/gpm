import gpm
from gpm.plugins import Generator
import graphviz
import random
import math
import time

g_plugin = Generator()


# class SinNode(gpm.Node):
#     def update(self, delta=1):
#         super().update(delta)
#         self.current += delta
#         self.signal = math.sin(self.current)
#


map = gpm.Map()
map.add_plugin(g_plugin)

map.run(10)






