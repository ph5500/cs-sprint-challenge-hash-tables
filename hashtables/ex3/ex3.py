def intersection(arrays):
    cache = {}
    result = []
    # print arrays
    for array in arrays:
        for i in array:
            if i not in cache:
                cache[i] = i
            elif i not in result:
                result.append(i)
                
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3, 5, 6, 4])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3 , 7, 9, 5])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3 , 0, 8, 5])

    print(intersection(arrays))
