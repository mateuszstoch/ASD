class Node:
    def __init__(self):
        self.parent = None
        self.d = float("inf")


def relax(u, v, w, uid):
    if v.d > u.d + w:
        v.d = u.d + w
        v.parent = uid


def bellmanFord(G, s):
    Verteces = [Node(i) for i in range(len(G))]
    Verteces[s].d = 0
    for i in range(len(G)):
        for edge in G[i]:
            relax(Verteces[i], Verteces[edge[0]], edge[1], i)
    for i in range(len(G)):
        for edge in G[i]:
            if Verteces[edge[0]].d != float("inf") and Verteces[edge[0]].d > Verteces[i].d + edge[1]:
                return False
    return True
