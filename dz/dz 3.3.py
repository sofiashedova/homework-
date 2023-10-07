f1 = f2 = 1
f_sum = f1 + f2
n = int(input("Номер элемента"))
i = 0
while i < n - 2:
    f_sum = f1 + f2
    f2 = f_sum
    i = i + 1
print(f2)


