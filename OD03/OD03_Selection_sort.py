# Функция для сортировки выбором (Selection Sort)
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j][1] < arr[min_index][1]:  # Сравниваем доходы (второй элемент в кортеже)
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# Основная программа
if __name__ == "__main__":
    # Словарь с доходами за 12 месяцев
    incomes = {
        "Январь": 45000,
        "Февраль": 42000,
        "Март": 43000,
        "Апрель": 41000,
        "Май": 48000,
        "Июнь": 46000,
        "Июль": 47000,
        "Август": 44000,
        "Сентябрь": 45500,
        "Октябрь": 43000,
        "Ноябрь": 49000,
        "Декабрь": 51000
    }

    # Преобразуем словарь в список кортежей (месяц, доход)
    income_list = list(incomes.items())

    # Сортировка доходов по возрастанию с использованием сортировки выбором
    sorted_incomes = selection_sort(income_list)

    # Вывод исходных данных
    print("Исходные данные (месяц: доход):")
    for month, income in incomes.items():
        print(f"{month}: {income} руб.")

    # Вывод отсортированных данных
    print("\nОтсортированные данные (по возрастанию доходов):")
    for month, income in sorted_incomes:
        print(f"{month}: {income} руб.")
