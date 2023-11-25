from collections import deque

def bfs(g, s, t):
    a = deque([(s, 0)])
    b = set([s])

    while a:
        node, distance = a.popleft()
        if node == t:
            return distance
        for neighbor in g.get(node, []):
            if neighbor not in b:
                a.append((neighbor, distance + 1))
                b.add(neighbor)

    return None