time = 0
dag = []


def scc(G):
    global dag
    dfs(G)
    GT = [[] for _ in range(len(G))]
    for i in range(len(G)):
        for edge in G[i]:
            GT[edge].append(i)
    order = dag[:]
    dfsMod(GT, order)


class vertex:
    def __init__(self):
        self.parent = None
        self.d = float("inf")
        self.f = float("inf")
        self.visited = False


def dfsMod(G, order):
    V = [vertex() for _ in range(len(G))]
    scverteces = []
    for i in order:
        if not V[i].visited:
            scverteces.append(i)
            dfsVisit(G, i, V)
    return V


def dfs(G):
    V = [vertex() for _ in range(len(G))]
    for e in range(len(G)):
        if not V[e].visited:
            dfsVisit(G, e, V)


def dfsVisit(G, u, V):
    global time
    global dag
    time += 1
    V[u].d = time
    V[u].visited = True
    for e in G[u]:
        if not V[e].visited:
            V[e].parent = u
            dfsVisit(G, e, V)
    time += 1
    V[u].f = time
    dag.append(u)


g = [[1, 2], [0], [3], [4], [2], [6], [5]]
scc(g)
