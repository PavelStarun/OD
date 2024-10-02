class Graph:
    def __init__(self):
        self.graph = {}

    # Добавление рёбер между городами
    def add_edge(self, city1, city2):
        if city1 not in self.graph:
            self.graph[city1] = []
        if city2 not in self.graph:
            self.graph[city2] = []

        self.graph[city1].append(city2)
        self.graph[city2].append(city1)  # Так как это неориентированный граф

    # Поиск кратчайшего пути с помощью BFS
    def find_shortest_path(self, start, end):
        visited = set()  # Множество для отслеживания посещённых городов
        queue = [[start]]  # Очередь для хранения путей

        # Если начальный и конечный город совпадают
        if start == end:
            return [start]

        while queue:
            path = queue.pop(0)  # Извлекаем первый путь из очереди
            city = path[-1]  # Последний город в пути

            if city not in visited:
                neighbors = self.graph[city]  # Все соседи текущего города

                # Проходим по всем соседям
                for neighbor in neighbors:
                    new_path = list(path)  # Копируем текущий путь
                    new_path.append(neighbor)  # Добавляем соседа в путь
                    queue.append(new_path)  # Добавляем новый путь в очередь

                    # Если нашли целевой город
                    if neighbor == end:
                        return new_path

                visited.add(city)  # Отмечаем город как посещённый

        return None  # Если пути не существует

    # Печать графа для наглядности
    def print_graph(self):
        for city in self.graph:
            print(city, "связан с", ", ".join(self.graph[city]))


# Пример использования программы
if __name__ == "__main__":
    # Создаём граф (нашу карту)
    g = Graph()

    # Добавляем маршруты между городами
    g.add_edge("Москва", "Санкт-Петербург")
    g.add_edge("Москва", "Нижний Новгород")
    g.add_edge("Москва", "Казань")
    g.add_edge("Санкт-Петербург", "Вологда")
    g.add_edge("Нижний Новгород", "Казань")
    g.add_edge("Казань", "Уфа")
    g.add_edge("Уфа", "Екатеринбург")
    g.add_edge("Екатеринбург", "Тюмень")

    # Вывод карты городов
    print("Карта городов:")
    g.print_graph()

    # Навигация между двумя городами
    print("\nПоиск кратчайшего пути:")
    start_city = input("Введите начальный город: ")
    end_city = input("Введите конечный город: ")

    path = g.find_shortest_path(start_city, end_city)

    if path:
        print(f"Кратчайший маршрут между {start_city} и {end_city}: {' -> '.join(path)}")
    else:
        print(f"Маршрут между {start_city} и {end_city} не найден.")
