def detect_language(text):
    # Набор символов для разных языков
    russian_alphabet = set("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
    english_alphabet = set("abcdefghijklmnopqrstuvwxyz")

    # Преобразуем текст в нижний регистр
    text = text.lower()

    # Определяем, какие символы встречаются в тексте
    text_set = set(text)

    # Проверяем пересечение с алфавитами
    is_russian = any(char in russian_alphabet for char in text_set)
    is_english = any(char in english_alphabet for char in text_set)

    # Определяем язык
    if is_russian and is_english:
        return "Смешанный язык"
    elif is_russian:
        return "Русский язык"
    elif is_english:
        return "Английский язык"
    else:
        return "Неопределённый язык"


# Пример использования
text = input("Введите текст: ")
result = detect_language(text)
print(f"Определённый язык: {result}")
