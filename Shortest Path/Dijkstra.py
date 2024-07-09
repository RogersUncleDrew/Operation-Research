import heapq


def dijkstra(graph, start_node):
    distances = {node: float("inf") for node in graph}
    priority = []
    previousNode = {node: None for node in graph}
    distances[start_node] = 0
    heapq.heappush(priority, (0, start_node))
    while priority:
        currentDistance, currentNode = heapq.heappop(priority)
        if currentDistance > distances[currentNode]:
            continue
        for neighbor, width in graph[currentNode].items():
            distance = width + distances[currentNode]
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previousNode[neighbor] = currentNode
                heapq.heappush(priority, (distance, neighbor))
    return distances, previousNode


def get_shortest_path(previous_nodes, target):
    path = []
    current_node = target

    while current_node is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node]

    path.reverse()
    return path


graph = {
    'A': {'B': 3, 'C': 2, 'D': 6},
    'B': {'A': 3, 'E': 1, 'F': 7},
    'C': {'A': 2, 'D': 4, 'G': 8},
    'D': {'A': 6, 'C': 4, 'H': 3},
    'E': {'B': 1, 'F': 5, 'I': 2},
    'F': {'B': 7, 'E': 5, 'J': 4},
    'G': {'C': 8, 'H': 6, 'I': 3},
    'H': {'D': 3, 'G': 6, 'J': 1},
    'I': {'E': 2, 'G': 3, 'J': 7},
    'J': {'F': 4, 'H': 1, 'I': 7}
}

# 计算从节点'A'出发的最短路径
start_node = 'A'
distances, previous_nodes = dijkstra(graph, start_node)

# 打印从节点'A'到所有节点的最短路径
for target_node in graph:
    path = get_shortest_path(previous_nodes, target_node)
    print(f"从节点 {start_node} 到节点 {target_node} 的最短路径为 {path}，距离为 {distances[target_node]}")
