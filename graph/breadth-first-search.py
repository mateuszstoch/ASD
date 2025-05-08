class vertex:
    def __init__(self):
        self.parent = None
        self.d = float("inf")
        self.visited = False


def bfs(edges, n):
    V = [vertex() for _ in range(len(edges))]
    V[n].d = 0
    queue = [n]
    p = 0
    while p < len(queue):
        for e in edges[queue[p]]:
            if not V[e].visited:
                V[e].visited = True
                V[e].d = V[p].d+1
                V[e].parent = p
                queue.append(e)
        p += 1
