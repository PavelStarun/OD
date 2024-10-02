# Палиндром — это слово или фраза, которые одинаково читаются слева направо и справа налево.
# Создаем функцию для проверки палиндрома.
# Для начало приводим все к нижнему регистру.
# Исключаем символы, не являющиеся буквами.
# Сравниваем первый символ с последним.
# Если они совпадают, то возвращаем True.
# Если они не совпадают, то возвращаем False.

import re
def is_palindrome(word):
    word = word.lower()
    word = s = re.sub(r'[^a-z]', '', word)
    if word[0] == word[-1]:
        return True
    else:
        return False


print(is_palindrome("Bob"))
print(is_palindrome("Able was I ere I saw Elba"))
print(is_palindrome("Madam, I'm Adam"))
print(is_palindrome("Hello, world!"))