import numpy
from collections import deque
from sortedcontainers import SortedSet

class Grafo:

    def __init__(self):
        self.id = 0
        self.x = 0
        self.y = 0
        self.p = []
        self.s = []

            
grafo1 = Grafo()
grafo2 = Grafo()
grafo1.id = 1
grafo2.id = grafo1.id+1
grafo1.x = 1
grafo1.y = 1
grafo2.x = 2
grafo2.y = 2
grafo1.p = None
grafo2.p = grafo1.id
grafo1.s = grafo2.id
grafo2.s = None
