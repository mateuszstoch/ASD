class vertex:
    def __init__(self):
        self.parent = None
        self.d = float("inf")
        self.f = float("inf")
        self.visited = False


time = 0


def dfs(G):
    V = [vertex() for _ in range(len(G))]
    for e in range(len(G)):
        if not V[e].visited:
            dfsVisit(G, e, V)
    return


def dfsVisit(G, u, V):
    global time
    time += 1
    V[u].d = time
    V[u].visited = True
    for e in G[u]:
        if not V[e].visited:
            V[e].parent = u
            dfsVisit(G, u, V)
    time += 1
    V[u].f = time
