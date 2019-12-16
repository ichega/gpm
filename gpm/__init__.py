from graphviz import Digraph
from datetime import datetime


class Node:
    def __init__(self):
        self.caption = 'Node'
        self.net = None
        self.color = '#FF0000'

    def update(self, delta=1):
        pass

    def render(self, digraph: Digraph):
        digraph.node(self.caption)


class Edge:
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2
        self.net = None

    def update(self, delta=1):
        pass

    def render(self, digraph: Digraph):
        digraph.edge(self.node1.caption, self.node2.caption)


class Plugin:
    def __init__(self):
        self.net = None
        self.priority = 0

    def update(self, delta=1):
        pass


class Map:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.plugins = []
        self.time = 0
        self.start_time = datetime.now()

    def update(self, delta=1):
        for plugin in self.plugins:
            plugin.update(delta)

        for node in self.nodes:
            node.update(delta)

        for edge in self.edges:
            edge.update(delta)

    def add_node(self, node):
        self.nodes.append(node)
        node.net = self

    def add_edge(self, edge):
        self.edges.append(edge)
        edge.net = self

    def add_plugin(self, plugin):
        self.plugins.append(plugin)
        plugin.map = self
        self.plugins = sorted(self.plugins, key=lambda plugin: plugin.priority)

    def run(self, iters=60):
        self.it = 0
        while self.it < iters:
            self.update(1)
            self.it += 1
            self.save(f'history/iter_{self.it}.png')

    def save(self, filename='graph.png'):
        d = Digraph('hello', filename='assets/graph.gv')
        d.attr('node', shape='circle')
        for node in self.nodes:
            d.attr('node', fillcolor=node.color, style='filled')
            node.render(d)
        for edge in self.edges:
            edge.render(d)
        parts = filename.split('.')
        d.render(filename=parts[0], format=parts[1])
