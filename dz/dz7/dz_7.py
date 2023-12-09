from collections import deque

def check(node, t):
    return node == t


def bfs(g, s, t, check):
    a = deque([(s, 0)])
    b = set([s])

    while a:
        node, distance = a.popleft()
        if check(node, t):
            return distance
        for neighbor in g.get(node, []):
            if neighbor not in b:
                a.append((neighbor, distance + 1))

    return None