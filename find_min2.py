def find_min2(array):
    if len(array) < 2:
        return None

    min1 = float('inf')
    min2 = float('inf')

    for num in array:
        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2 and num != min1:
            min2 = num

    return min2 if min2 != float('inf') else None

array = [3, 1, 4, 3, 5, 9, 3, 6, 5]
second_min = find_min2(array)
print(second_min)