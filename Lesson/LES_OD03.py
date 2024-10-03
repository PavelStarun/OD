# Существует несколько популярных алгоритмов сортировки:
#
# Пузырьковая сортировка (Bubble Sort);
# Сортировка выбором (Selection Sort);
# Сортировка вставками (Insertion Sort);
# Быстрая сортировка (Quick Sort);
# Сортировка слиянием (Merge Sort).

#######################################################################

mas = [5, 7, 4, 3, 8, 2]
n = 6

for run in range(n - 1):
    for i in range(n - 1 - run):
        if mas[i] > mas[i + 1]:
            mas[i], mas[i + 1] = mas[i + 1], mas[i]

print(mas)

#######################################################################

def quick_sort(s):
    if len(s) <= 1:
        return s

    element = s[0]
    left = list(filter(lambda i: i < element, s))
    center = [i for i in s if i == element]
    right = list(filter(lambda i: i > element, s))

    return quick_sort(left) + center + quick_sort(right)


print(quick_sort([5, 2, 9, 0, 1, 5, 3]))

#######################################################################

a = [-3, 5, 0, -8, 1, 10]


def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


selection_sort(a)
print(a)

#######################################################################

a = [-3, 5, 0, -8, 1, 10]


def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


insert_sort(a)
print(a)
