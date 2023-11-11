def f(n):
    f = [0, 1]
    for _ in range(n - 2):
        f.append(f[-1] + f[-2])
    return f[:n]
print(f(int(input())))

