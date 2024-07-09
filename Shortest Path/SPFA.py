from collections import deque


class graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = {i:[] for i in range(self.V)}

    def add_edge(self, u, v, w):
        self.edges[u].append([v, w])

    def SPFA(self, iniPoint):
        distance = [float("inf") for i in range(self.V)]
        distance[iniPoint] = 0
        inQueue = [False for i in range(self.V)]
        queue = deque([iniPoint])
        inQueue[iniPoint] = True
        while queue:
            u = queue.popleft()
            inQueue[u] = False
            for v, w in self.edges[u]:
                if distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w
                    if not inQueue[v]:
                        queue.append(v)
                        inQueue[v] = True
        for i in range(self.V):
            print("点{}到点{}的最小距离为{}".format(iniPoint, i, distance[i]))
g = graph(5)
g.add_edge(0, 1, -1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, -3)

distances = g.SPFA(0)
