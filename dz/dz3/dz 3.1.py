def f():
    a, b = input(), []
    while a:
        b.append(a)
        a = input()
    return b

print(f())