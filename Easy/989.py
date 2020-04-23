# 989. Add to Array-Form of Integer

##method 1  (convert arrary to int, after addition, then convert to array)
def addToArrayForm(self, A, K):
    """
    :type A: List[int]
    :type K: int
    :rtype: List[int]
    """
    m = len(A)
    A = list(reversed(A))
    for i in range(m):
        K += A[i]
        A[i] = K % 10
        K //= 10
    while K:
        A.append(K % 10)
        K //= 10
    A = list(reversed(A))
    return A


##2
def addToArrayForm(self, A, K):
    """
    :type A: List[int]
    :type K: int
    :rtype: List[int]
    """
    a = 0
    for i in A:
        a = a * 10 + i

    tmp = a + K
    if tmp == 0:
        return [0]
    res = list()
    while tmp:
        res.insert(0, tmp % 10)
        tmp //= 10
    return res


##https://blog.csdn.net/qq_17550379/article/details/86913572 reference


