size: int = 1
table: [] = [None] * size
#список table, заполненный значениями None, и его размер равен size. 

def hashing(key: str) -> int:
    result: int = (sum(ord(c) for c in key)) % size
    return result
#использует сумму кодов символов строки (ord(c) возвращает числовое значение символа) и затем берет остаток от деления этой суммы на размер таблицы (size).
#Таким образом, функция хэширования преобразует ключ в индекс для доступа к элементу в таблице.

def resize(size) -> int:
    global table
    old_table = table
    size *= 2
    table = [None] * size
    for bucket in old_table:
        if bucket is not None:
            for pair in bucket:
                set_value(pair[0], pair[1])
    return size
#изменяет размер таблицы хэширования, увеличивая ее вдвое.
#Она сохраняет старую таблицу в переменной old_table, затем создает новую таблицу с увеличенным размером и проходит по всем элементам старой таблицы, перехешируя их и добавляя в новую таблицу.
def set_value(key: str, value: str) -> int:
    global size
    load_factor = load()
    if load_factor > 0.75:
        size = resize(size)
    hash_index: int = hashing(key)
    if table[hash_index] is not None:
        for pair in table[hash_index]:
            if pair[0] == key:
                pair[1] = value
                return size
        table[hash_index].append([key, value])
    else:
        table[hash_index] = [[key, value]]
    return size
#Если коэффициент загрузки таблицы превышает 0.75, то размер таблицы увеличивается вдвое.
#Затем происходит хэширование ключа, и если в указанном индексе уже есть элементы, то происходит поиск по ключам и, если такой ключ уже существует, его значение обновляется. 
#В противном случае новая пара ключ-значение добавляется в таблицу.
def get_value(key: str) -> str:
    hash_index: int = hashing(key)
    if table[hash_index] is not None:
        for pair in table[hash_index]:
            if pair[0] == key:
                return pair[1]
    return None
#функциz для получения значения по ключу из таблицы хэширования.
#вычисляет хэш-индекс для данного ключа, затем проверяет, существует ли элемент с таким индексом в таблице. 
#Если элемент существует, он проверяет все пары ключ-значение в этом элементе и возвращает значение, связанное с заданным ключом.
#Иначе возвращает значение None 
def del_value(key: str) -> None:
    hash_index: int = hashing(key)
    if table[hash_index] is None:
        return None
    for i in range(0, len(table[hash_index])):
        if table[hash_index][i][0] == key:
            table[hash_index].pop(i)
            if len(table[hash_index]) == 0:
                table[hash_index] = None
            return
#Если элемент существует, она проверяет все пары ключ-значение в этом элементе и удаляет пару с заданным ключом. 
#Если элемент с таким индексом не существует или нет пары с заданным ключом, функция возвращает значение None.

def load() -> float:
    filled_buckets = len([bucket for bucket in table if bucket is not None])
    fill_ratio = filled_buckets / float(size)
    return fill_ratio

def main():
    global size
    while True:
        print("\033[31m" + "1. Добавить значение")
        print("2. Удалить значение")
        print("3. Получить значение")
        print("4. Коэффициент заполнения")
        print("5. Вывести таблицу")
        print("6. Выход" + "\033[0m")

        choice = input("\033[32m" + "Введите ваш выбор: " + "\033[0m")

        if choice == '1':
            key = input("\033[32m" + "Введите ключ: " + "\033[0m")
            value = input("\033[32m" + "Введите значение: " + "\033[0m")
            size = set_value(key, value)

        elif choice == '2':
            key = input("\033[32m" + "Введите ключ: " + "\033[0m")
            del_value(key)

        elif choice == '3':
            key = input("\033[32m" + "Введите ключ: " + "\033[0m")
            print(get_value(key))

        elif choice == '4':
            print("Table size:", size)
            for i in range(size):
                if table[i] is not None:
                    print(chr(0x25A0), end="")
                else:
                    print(chr(0x25A1), end="")
            print("\n", load())

        elif choice == '5':
            print(table)

        elif choice == '6':
            break

        else:
            print("\033[33m" + "Неверный выбор. Попробуйте еще раз." + "\033[0m")