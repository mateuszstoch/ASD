from queue import PriorityQueue


class Node:
    def __init__(self):
        self.parent = None
        self.visited = False
        self.d = float("inf")


def dijkstra(G, s):
    V = [Node() for _ in range(len(G))]
    V[s].d = 0
    Q = PriorityQueue()
    Q.put((0, s))

    while not Q.empty():
        _, u = Q.get()
        if not V[u].visited:
            V[u].visited = True
            for v, w in G[u]:
                if V[v].d > V[u].d+w:
                    V[v].d = V[u].d + w
                    V[v].parent = u
                    Q.put((V[v].d, v))
