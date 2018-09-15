def gcdIter(a, b):
    if b == 0:
        return a
    else:
        return gcdIter(b, a % b)