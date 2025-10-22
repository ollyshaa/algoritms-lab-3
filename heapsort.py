# Лічильники для процедури Sink(A, 0, n)
sink_comparisons = 0
sink_swaps = 0
sink_calls = 0

def swap(arr, i, j):
    """Міняє місцями два елементи в масиві."""
    global sink_swaps
    arr[i], arr[j] = arr[j], arr[i]
    sink_swaps += 1

def sink(arr, i, n):
    """
    Процедура 'занурення' елемента вниз по купі.
    """
    global sink_comparisons, sink_swaps, sink_calls
    sink_calls += 1

    k = i
    while True:
        j = 2 * k + 1

        sink_comparisons += 1
        if j >= n:
            break

        sink_comparisons += 1
        if j + 1 < n:
            sink_comparisons += 1
            if arr[j + 1] > arr[j]:
                j += 1

        sink_comparisons += 1
        if arr[k] >= arr[j]:
            break
        else:
            swap(arr, k, j)
            k = j

def heapsort_with_sink_counters(arr):
    """
    Алгоритм пірамідального сортування з підрахунком операцій Sink(A, 0, n).
    """
    global sink_comparisons, sink_swaps, sink_calls
    n = len(arr)

    sink_comparisons = 0
    sink_swaps = 0
    sink_calls = 0

    print(f"Початковий масив: {arr}\n")

    # Фаза 1: Побудова максимальної купи
    print("--- Фаза 1: Побудова максимальної купи ---")
    for i in range(n // 2 - 1, -1, -1):
        print(f"Занурюємо елемент з індексу {i}: {arr[i]}")
        sink(arr, i, n)
    print(f"Масив після побудови купи: {arr}\n")

    # Фаза 2: Сортування - тут використовуємо Sink(A, 0, n)
    print("--- Фаза 2: Сортування (використання Sink(A, 0, n)) ---")

    phase2_sink_comparisons = 0
    phase2_sink_swaps = 0
    phase2_sink_calls = 0

    for i in range(n - 1, 0, -1):
        print(f"Крок {n - i}: Міняємо корінь ({arr[0]}) та останній елемент ({arr[i]})")
        swap(arr, 0, i)

        # Фіксуємо стан лічильників перед викликом Sink(A, 0, n)
        before_comparisons = sink_comparisons
        before_swaps = sink_swaps
        before_calls = sink_calls

        print(f"Виклик Sink(A, 0, {i})")
        sink(arr, 0, i)

        call_comparisons = sink_comparisons - before_comparisons
        call_swaps = sink_swaps - before_swaps
        call_calls = sink_calls - before_calls

        phase2_sink_comparisons += call_comparisons
        phase2_sink_swaps += call_swaps
        phase2_sink_calls += 1

        print(f"  Порівнянь у цьому виклику: {call_comparisons}")
        print(f"  Обмінів у цьому виклику: {call_swaps}")
        print(f"Масив: {arr}\n")

    print(f"Відсортований масив: {arr}")


    print("\n=== СТАТИСТИКА ДЛЯ SINK(A, 0, n) У ФАЗІ СОРТУВАННЯ ===")
    print(f"Кількість викликів Sink(A, 0, n): {phase2_sink_calls}")
    print(f"Загальна кількість порівнянь: {phase2_sink_comparisons}")
    print(f"Загальна кількість обмінів: {phase2_sink_swaps}")

    return arr

print("=== МОДЕЛЮВАННЯ ДЛЯ ВАРІАНТУ 25 ===")
A = [11, 42, 67, 55, 65, 78, 25, 50, 69]
sorted_A = heapsort_with_sink_counters(A)