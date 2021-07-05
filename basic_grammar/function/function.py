def compute(n):
    if n == 1:
        return 1
    else:
        return n + compute(n - 1)


print(compute(100))
