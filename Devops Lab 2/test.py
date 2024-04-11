import uuid
import pyfiglet

# Список слов
words = ["apple", "banana", "cherry", "orange", "grape"]

# Генерируем уникальный идентификатор (UUID)
unique_id = str(uuid.uuid4())

# Выбираем слово на основе случайной части UUID
random_word_index = int(unique_id[:8], 16) % len(words)
random_word = words[random_word_index]

# Используем pyfiglet для стилизации слова
ascii_art = pyfiglet.figlet_format(random_word)

# Выводим стилизованное слово
print(ascii_art)
