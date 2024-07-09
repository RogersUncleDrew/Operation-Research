import heapq


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def a_star(grid, start, goal):
    m, n = len(grid), len(grid[0])
    queue = []
    heapq.heappush(queue, (start, 0))
    pre = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    while queue:
        current = heapq.heappop(queue)[0]
        if current == goal:
            path = []
            while current in pre:
                path.append(current)
                current = pre[current]
            path.append(start)
            path.reverse()
            return path
        for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbour = (current[0] + x, current[1] + y)
            if 0<=neighbour[0]<m and 0<=neighbour[1]<n and grid[neighbour[0]][neighbour[1]] == 0:
                real_distance = g_score[current] + 1
                if neighbour not in g_score or real_distance < g_score[neighbour]:
                    g_score[neighbour] = real_distance
                    pre[neighbour] = current
                    f_score[neighbour] = real_distance + heuristic(neighbour, goal)
                    heapq.heappush(queue, (neighbour, f_score[neighbour]))
    return None
# 示例网格：0表示可以通过，1表示障碍
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

path = a_star(grid, start, goal)
if path:
    print("Path found:", path)
else:
    print("No path found.")
