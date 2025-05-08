def merge(A, B):
    n = len(A)+len(B)
    T = [0 for _ in range(n)]
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            T[i+j] = A[i]
            i += 1
        else:
            T[i+j] = B[j]
            j += 1
    while i < len(A):
        T[i+j] = A[i]
        i += 1
    while j < len(B):
        T[i+j] = B[j]
        j += 1
    return T


def sort(A):
    if len(A) <= 1:
        return A

    left = sort(A[:len(A)//2])
    rigth = sort(A[len(A)//2:])

    return merge(left, rigth)
