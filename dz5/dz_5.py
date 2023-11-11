def poisk( lst,n):
    low = 0 
    high = len(lst) - 1
    result = None 
    while low <= high:
        mid = (low +  high) // 2
        if lst[mid] == n:
           result = mid
           high = mid - 1
        elif lst[mid] > n:
            high = mid - 1
        else:
            low = mid + 1
    return result
