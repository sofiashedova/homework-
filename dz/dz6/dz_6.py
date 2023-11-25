size: int = 1
table: [] = [None] * size 
def hash_function(key):
    return (sum(ord(c) for c in key)) % size 

def set_value(hash_table, key, value):
    index = hash_function(key)
    if hash_table[index] is None:
        hash_table[index] = [(key, value)]
    else:
        for i in range(len(hash_table[index])):
            if hash_table[index][i][0] == key:
                hash_table[index][i] = (key, value)
                return
        hash_table[index].append((key, value))

def get_value(hash_table, key):
    index = hash_function(key)
    if hash_table[index] is not None:
        for item in hash_table[index]:
            if item[0] == key:
                return item[1]
    return None

def del_value(hash_table, key):
    index = hash_function(key)
    if hash_table[index] is not None:
        for i in range(len(hash_table[index])):
            if hash_table[index][i][0] == key:
                del hash_table[index][i]
                return

def load_factor(hash_table):
    filled_slots = sum(1 for slot in hash_table if slot is not None)
    return filled_slots / len(hash_table)

