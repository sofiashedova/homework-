def f(n):
    f = [0, 1]
    for _ in range(2, n):
        f.append(f[-1] + f[-2])
        return f[:n]
print(f(int(input())))

