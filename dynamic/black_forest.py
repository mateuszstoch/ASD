# A - array of length n of gain from cutting this tree. you cant cut 2 adjusted trees
# find maximumg gain.


def find_gain(A):
    n = len(A)
    G = [0 for _ in range(n)]
    G[0] = A[0]
    G[1] = max(A[0], A[1])
    for i in range(2, n):
        G[i] = max(G[i-2]+A[i], A[i-1])
    return G[n-1]


print(find_gain([2, 9, 3, 1, 4, 8]))
