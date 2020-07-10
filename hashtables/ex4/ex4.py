def has_negatives(a):
    pos = []
    cache = {}
    result = []
    
    for num in a:
        if num > 0:
            pos.append(num)
        else:
            cache[-num] = -num
            
    for i in pos:
        if i in cache:
            result.append(i)
            
    return result
    
    




    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
