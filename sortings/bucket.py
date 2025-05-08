from math import floor


def insertionSort(T):
    for i in range(len(T)):
        minV = i
        for j in range(i, len(T)):
            if T[j] < T[minV]:
                minV = j
        if minV != i:
            T[i], T[minV] = T[minV], T[i]


def sort(T):
    n = len(T)
    temp = [[] for _ in range(0, n)]
    for i in range(0, n):
        e = T[i]
        temp[floor(e*n)].append(e)
    output = []
    for i in range(0, n):
        insertionSort(temp[i])
        output += temp[i]
    return output
