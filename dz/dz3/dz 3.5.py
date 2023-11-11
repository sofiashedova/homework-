def f(n):
    return sum(n) / len(n)
lst = [int(n) for n in input().split()]
print(f(lst))