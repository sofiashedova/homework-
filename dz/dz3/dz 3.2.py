n = int(input())
def f(n):
    if n == 1 or n == 2 or n == 12:
        return "Зима"
    elif n == 3 or n == 4 or n == 5:
        return "Весна"
    elif n == 6 or n == 7 or n ==8:
        return "Лето"
    elif n == 9 or n == 10 or n == 11:
        return "Осень"
print(f(n))



