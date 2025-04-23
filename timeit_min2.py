import timeit

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
stmt = 'find_min2(array)'

# Код для замера времени
iterations = 1000  # Количество повторений для более точного измерения

time_taken = timeit.timeit(lambda: find_min2(array), number=iterations)

print(f"Время выполнения find_min2({array}) {iterations} раз: {time_taken} секунд")
print(f"Среднее время выполнения: {time_taken / iterations} секунд")