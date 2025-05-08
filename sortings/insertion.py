def sort(T):
    for i in range(len(T)):
        minV = i
        for j in range(i, len(T)):
            if T[j] < T[minV]:
                minV = j
        if minV != i:
            T[i], T[minV] = T[minV], T[i]
