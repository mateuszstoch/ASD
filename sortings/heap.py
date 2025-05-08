def left(i):
    return 2*i + 1


def right(i):
    return 2*i + 2


def parent(i):
    return (i-1)//2


def heapify(A, n, i):
    l = left(i)
    r = right(i)
    max_int = i
    if n > l and A[l] > A[max_int]:
        max_int = l
    if n > r and A[r] > A[max_int]:
        max_int = r
    if max_int != i:
        A[i], A[max_int] = A[max_int], A[i]
        heapify(A, n, max_int)


def buildHeap(T):
    n = len(T)
    for i in range(parent(n-1), -1, -1):
        heapify(T, n, i)


def sort(T):
    n = len(T)
    buildHeap(T)
    for i in range(n-1, 0, -1):
        T[i], T[0] = T[0], T[i]
        heapify(T, i, 0)
