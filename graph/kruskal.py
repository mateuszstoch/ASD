class Node:
    def __init__(self, parent=None):
        self.parent = parent or self
        self.val = 0


# G - lista wszystkich krawedzi [u,v,cost] , v - liczba wierzcholkow
def kurskal_mst(G, v):
    G.sort(key=lambda x: x[2])
    unionlist = [Node() for i in range(v)]
    A = []
    for i in range(len(G)):
        if union(unionlist[G[i][0]], unionlist[G[i][1]]):
            A.append(G[i])
    return A


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return False
    elif x.val < y.val:
        x.parent = y
    else:
        if x.val == y.val:
            x.val += 1
        y.parent = x
    return True


def find(x):
    while x.parent != x:
        x = x.parent
    return x
