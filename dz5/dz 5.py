def poisk( lst, n):
    low = 0 
    high = len(lst) - 1
    mid = (low + high) // 2
    while low <= high:
        num = n
        if num == n:
            mid = mid - 1 
            return mid 
        if num > n:
            high = mid - 1
        else:
            low = mid + 1
    return None