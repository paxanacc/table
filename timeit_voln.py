import timeit

def count_vertices(edges):
    """Подсчет количества вершин в графе."""
    vertices = set()
    for edge in edges:
        vertices.add(edge[0])
        vertices.add(edge[1])
    return len(vertices)


def get_vertices(edges):
    """Получение списка вершин из списка ребер."""
    vertices = set()
    for edge in edges:
        vertices.add(edge[0])
        vertices.add(edge[1])
    return list(vertices)


def wave_algorithm(edges, start, end):
    """Реализация волнового алгоритма."""
    vertices = get_vertices(edges)
    num_vertices = count_vertices(edges)

    # Инициализация массива пройденных вершин
    visited = {v: 0 for v in vertices}
    visited[start] = 1

    # Инициализация массива предков для восстановления пути
    parent = {v: None for v in vertices}

    # Флаг для проверки, найдена ли конечная вершина
    found = False

    # Шаг волнового алгоритма
    step = 1

    while True:
        # Флаг для проверки, были ли найдены новые вершины на текущем шаге
        new_vertices_found = False

        # Проходим по всем вершинам, которые были посещены на предыдущем шаге
        for v in vertices:
            if visited[v] == step:
                # Проходим по всем соседям текущей вершины
                for edge in edges:
                    if edge[0] == v and visited[edge[1]] == 0:
                        visited[edge[1]] = step + 1
                        parent[edge[1]] = v
                        new_vertices_found = True
                    if edge[1] == v and visited[edge[0]] == 0:
                        visited[edge[0]] = step + 1
                        parent[edge[0]] = v
                        new_vertices_found = True

        # Если конечная вершина найдена, выходим из цикла
        if visited[end] != 0:
            found = True
            break

        # Если новые вершины не найдены, выходим из цикла
        if not new_vertices_found:
            break

        step += 1

    # Восстановление пути
    if found:
        path = recover_path(parent, end)
        return path, visited
    else:
        return None, visited


def recover_path(parent, end):
    """Восстановление пути от конечной вершины до начальной."""
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()
    return path


# Пример использования
edges = [(1, 2), (2, 3), (2, 4), (4, 5), (1, 6), (6, 7), (4, 5)]
start = 1
end = 5

# Измерение времени выполнения всего алгоритма
time_taken = timeit.timeit(lambda: wave_algorithm(edges, start, end), number=1000)
print(f"Время выполнения алгоритма (1000 запусков): {time_taken:.6f} секунд")

# Выполнение одного запуска для отображения результата
path, visited = wave_algorithm(edges, start, end)
if path:
    print(f"Кратчайший путь от {start} до {end}: {path}")
else:
    print(f"Путь от {start} до {end} не найден")

print("Шаги посещения вершин:", visited)