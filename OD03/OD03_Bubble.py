# Функция для сортировки студентов по оценкам (пузырьковая сортировка)
def bubble_sort_grades(students):
    student_list = list(students.items())
    n = len(student_list)

    for run in range(n - 1):
        for i in range(n - 1 - run):
            if student_list[i][1] > student_list[i + 1][1]:
                student_list[i], student_list[i + 1] = student_list[i + 1], student_list[i]

    return dict(student_list)


# Функция для сортировки студентов по именам (пузырьковая сортировка)
def bubble_sort_names(students):
    student_list = list(students.items())
    n = len(student_list)

    for run in range(n - 1):
        for i in range(n - 1 - run):
            if student_list[i][0] > student_list[i + 1][0]:
                student_list[i], student_list[i + 1] = student_list[i + 1], student_list[i]

    return dict(student_list)



if __name__ == "__main__":
    students = {
        "Жанна": 8.5,
        "Борис": 9.0,
        "Дарья": 7.8,
        "Галина": 9.2,
        "Егор": 5.4,
        "Дмитрий": 7.5,
        "Александр": 7.7,
        "Евгения": 9.1,
        "Анна": 9.3,
    }

    print("Исходные данные:")
    for name, grade in students.items():
        print(f"{name}: {grade}")

    print("\nВыберите, как отсортировать студентов:")
    print("1 - По оценкам")
    print("2 - По именам")
    choice = input("Введите 1 или 2: ")

    if choice == "1":
        sorted_students = bubble_sort_grades(students)
        print("\nРезультаты студентов после сортировки по оценкам:")
    elif choice == "2":
        sorted_students = bubble_sort_names(students)
        print("\nРезультаты студентов после сортировки по именам:")
    else:
        print("Неверный выбор!")
        exit()

    # Вывод результатов сортировки
    for name, grade in sorted_students.items():
        print(f"{name}: {grade}")
