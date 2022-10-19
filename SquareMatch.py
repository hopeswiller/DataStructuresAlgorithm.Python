size = 8


def square(n):

    res = []
    for j in range(1, size + 1):
        if j == 1 or j == 8:
            res.append("*" * size)
        else:
            res.append("*" + ((size - 2) * " ") + "*")

    for r in res:
        print("\t" + r)


square(size)
