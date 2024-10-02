class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)


class DrawingManager:
    def __init__(self):
        self.actions = []  # Список действий
        self.history = Stack()  # Стек для хранения истории действий

    def draw(self, action):
        self.actions.append(action)
        self.history.push(action)
        print(f"Нарисовано: {action}")


    def undo(self):
        if not self.history.is_empty():
            last_action = self.history.pop()
            self.actions.remove(last_action)
            print(f"Отменено действие: {last_action}")
        else:
            print("Нет действий для отмены.")


    def show_drawing(self):
        if self.actions:
            print(f"Текущие нарисованные элементы: {self.actions}")
        else:
            print("Ничего не нарисовано.")

manager = DrawingManager()


manager.draw("Круг")
manager.draw("Линия")
manager.draw("Круг")
manager.draw("Капот")
manager.show_drawing()
manager.undo()
manager.draw("Крыша")
manager.undo()
manager.draw("Дверь")
manager.draw("Фары")
manager.show_drawing()

stack = Stack()

print(stack.items)

stack.push(101)
stack.push(200)
stack.push(404)

print(stack.items)
stack.pop()
print(stack.items)
stack.peek()
print(stack.peek())
stack.size()
print(stack.size())
