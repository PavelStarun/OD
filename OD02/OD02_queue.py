class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)  # Добавляем элемент в начало списка (в конец очереди)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()  # Извлекаем первый элемент (первого в очереди)
        else:
            return None  # Если очередь пустая, возвращаем None

    def size(self):
        return len(self.items)


def serve_customers():
    queue = Queue()

    queue.enqueue("Клиент 1")
    queue.enqueue("Клиент 2")
    queue.enqueue("Клиент 3")
    queue.enqueue("Клиент 4")

    print(f"Количество клиентов в очереди: {queue.size()}")

    while not queue.is_empty():
        current_customer = queue.dequeue()
        print(f"Обслуживается: {current_customer}")
        print(f"Оставшиеся клиенты в очереди: {queue.items}")

    print("Все клиенты обслужены.")


serve_customers()
