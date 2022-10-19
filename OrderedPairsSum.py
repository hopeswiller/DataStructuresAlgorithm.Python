a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
k = 30

# Considering two arrays where arr2 is the reverse of arr1
# calc the ordered pairs sum less than K


def solution(a, b, k):
    (x, y) = 0, 0
    res = []
    for m, n in zip(a, reversed(b)):
        concat = int(str(m) + str(n))
        print(concat)
        if concat < k:
            (x, y) = m, n
            res.append((x, y))

    return res


print(solution(a, b, k))
