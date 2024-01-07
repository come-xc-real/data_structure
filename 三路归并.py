from SqList import SqList


def fuc(A, B, C=SqList(), a=0, b=0):
    while a < A.getsize() and b < B.getsize():
        if A[a] < B[b]:
            C.Add(A[a])
            a += 1
        else:
            C.Add(B[b])
            b += 1
    if a < A.getsize():
        C, a = Forla(A, C, a)
    else:
        C, b = Forla(B, C, b)
    return [C, a, b]


def middle(A, B, C, D=SqList(), a=0, b=0, c=0):
    # A = A.clear()
    # B = B.clear()
    # C = C.clear()
    while a < A.getsize() and b < B.getsize() and c < C.getsize():
        if A[a] < B[b]:
            if C[c] < A[a]:
                D.Add(C[c])
                c += 1
            else:
                D.Add(A[a])
                a += 1
        else:
            if C[c] < B[b]:
                D.Add(C[c])
                c += 1
            else:
                D.Add(B[b])
                b += 1

    if a < A.getsize() and b < B.getsize():
        D, a, b = fuc(A, B, a=a, b=b, C=D)
    elif b < B.getsize() and c < C.getsize():
        D, b, c = fuc(B, C, a=b, b=c, C=D)
    elif a < B.getsize() and c < C.getsize():
        D, a, c = fuc(B, C, a=a, b=c, C=D)
    # elif a < A.getsize() and b == B.getsize() and c == C.getsize():
    #     D, a = Forla(A, D, a)
    # elif a == A.getsize() and b < B.getsize() and c == C.getsize():
    #     D, b = Forla(B, D, b)
    # elif a == A.getsize() and b == B.getsize() and c < C.getsize():
    #     D, c = Forla(C, D, c)
    else:
        pass

    return D


def Forla(A, D, a):
    while a < A.getsize():
        D.Add(A[a])
        a += 1
    return [D, a]


if __name__ == '__main__':
    from SqList import SqList

    A = SqList()
    B = SqList()
    C = SqList()
    A.CreateList([1, 2, 5])
    B.CreateList([6, 8, 9, 111])
    C.CreateList([3, 7, 10, 80, 87])
    middle(A, B, C).display()
