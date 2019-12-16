from gpm import Plugin
import gpm
import uuid
import random


class Generator(Plugin):
    def __init__(self):
        super().__init__()
        self.map = None

    def update(self, delta=1):
        if random.randint(0, 1) == 0:
            n = gpm.Node()
            n.caption = str(uuid.uuid4())
            self.map.add_node(n)
