numbers = input("Введите список чисел через запятую").split(",")
numbers.sort(reverse = True)
result = " ".join(numbers) 
print("Максимально возможное число:", result)