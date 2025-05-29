# A - n element array of length of cars ordered how they can enter one of 2 lanes of length L
# return how many cars we can fit onto them


def ferry(A, L):
    n = len(A)
    f = [[[0 for _ in range(L+1)]for _ in range(L+1)]for _ in range(n)]
    for a in range(L+1):
        for b in range(L+1):
            if a >= A[0]:
                f[0][a][b] = 1
            if b >= A[0]:
                f[0][a][b] = 1

            for i in range(1, n):
                f[i][a][b] = f[i-1][a][b]
                if a - A[i] >= 0:
                    f[i][a][b] = max(f[i][a][b], f[i-1][a-A[i]][b]+1)
                if b - A[i] >= 0:
                    f[i][a][b] = max(f[i][a][b], f[i-1][a][b-A[i]]+1)
    return f[n-1][L][L]
