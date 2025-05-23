def floydWarshall(W, n):
    D = W[:][:]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                D[i][j] = min(D[i][j], D[i][k]+D[k][j])
    return D
