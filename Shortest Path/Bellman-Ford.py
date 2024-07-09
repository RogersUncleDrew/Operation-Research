class graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, w):
        self.edges.append([u, v, w])

    def bellman_ford(self, iniPoint):
        distance = [float("inf") if i != iniPoint else 0 for i in range(self.V)]
        pre = [0 for i in range(self.V)]
        for i in range(self.V - 1):
            for u, v, w in self.edges:
                if distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w
                    pre[v] = u
        print("Vertex Distance from Source")
        for i in range(self.V):
            print(f"{i}\t\t{distance[i]}")


# 示例图
g = graph(5)
g.add_edge(0, 1, -1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, -3)

# 从顶点0开始的最短路径
g.bellman_ford(0)
