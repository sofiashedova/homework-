numbers = input("Введите список чисел через запятую").split(",")
numbers.sort(reverse = True)
result = " ".join(str(num) for num in numbers)
print("Максимально возможное число:", result)