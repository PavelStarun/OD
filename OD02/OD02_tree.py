class TreeNode:
    def __init__(self, word):
        self.word = word
        self.left = None
        self.right = None


# Функция для добавления слова в бинарное дерево
def insert_word(root, word):
    if root is None:
        return TreeNode(word)
    else:
        if word < root.word:
            root.left = insert_word(root.left, word)
        else:
            root.right = insert_word(root.right, word)
    return root


# Функция для поиска слова в бинарном дереве
def search_word(root, word):
    if root is None or root.word == word:
        return root

    if word < root.word:
        return search_word(root.left, word)

    return search_word(root.right, word)


# Функция для индексирования текста (построение дерева поиска из списка слов)
def index_text(text):
    words = text.split()  # Разбиваем текст на слова
    root = None
    for word in words:
        root = insert_word(root, word.lower())
    return root


# Главная функция для интерактивного поиска
def main():
    text = """
    Дерево поиска — это структура данных, которая позволяет эффективно искать элементы по ключам. 
    В бинарном дереве поиска каждый узел имеет ключ, и для любого узла все ключи в его левом поддереве меньше, 
    чем ключ узла, а все ключи в правом поддереве больше.
    """

    # Индексация текста (строим дерево поиска слов)
    print("Индексация текста...")
    root = index_text(text)

    while True:
        word_to_search = input("\nВведите слово для поиска (или 'exit' для выхода): ").lower()

        if word_to_search == 'exit':
            print("Выход из программы.")
            break

        # Поиск слова в дереве
        result = search_word(root, word_to_search)
        if result:
            print(f"Слово '{word_to_search}' найдено в тексте.")
        else:
            print(f"Слово '{word_to_search}' не найдено в тексте.")


# Запуск программы
if __name__ == "__main__":
    main()
