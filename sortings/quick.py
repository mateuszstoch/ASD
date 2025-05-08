from random import randrange


def sort(T, p, r):
    if p < r:
        q = partition(T, p, r)
        sort(T, p, q-1)
        sort(T, q+1, r)


def partition(T, p, r):
    x = randrange(p, r)
    T[r], T[x] = T[x], T[r]
    i = p-1
    for j in range(p, r):
        if T[j] <= T[r]:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i+1], T[r] = T[r], T[i+1]
    return i+1
