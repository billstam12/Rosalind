
def increasing(seq):
    P = [None] * len(seq)
    M = [None] * len(seq)

    L = 1
    M[0] = 0
    for i in range(1, len(seq)):
        lo = 0
        hi = L
        if seq[M[hi - 1]] < seq[i]:
            j = hi
        else:
            while hi - lo > 1:
                mid = (hi + lo) // 2
                print M
                if seq[M[mid - 1]] < seq[i]:
                    lo = mid
                else:
                    hi = mid

            j = lo
        P[i] = M[j - 1]
        if j == L or seq[i] < seq[M[j]]:
            M[j] = i
            L = max(L, j + 1)

    result = []
    pos = M[L - 1]
    for k in range(L):
        result.append(seq[pos])
        pos = P[pos]

    return (result[::-1])


def decreasing(seq):
    P = [None] * len(seq)
    M = [None] * len(seq)

    L = 1
    M[0] = 0
    for i in range(1, len(seq)):
        lo = 0
        hi = L
        if seq[M[hi - 1]] > seq[i]:
            j = hi
        else:
            while hi - lo > 1:
                mid = (hi + lo) // 2
                if seq[M[mid - 1]] > seq[i]:
                    lo = mid
                else:
                    hi = mid

            j = lo
        P[i] = M[j - 1]
        if j == L or seq[i] > seq[M[j]]:
            M[j] = i
            L = max(L, j + 1)
    result = []
    pos = M[L - 1]
    for k in range(L):
        result.append(seq[pos])
        pos = P[pos]

    return (result[::-1])
f = open("dataset.txt", "r")
no = f.readline()
data = map(int,f.readline().split()) #convert to int

ls = increasing(data)
print ' '.join(map(str, ls))


ls = decreasing(data)
print ' '.join(map(str, ls))
