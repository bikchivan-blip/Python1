import string

raw_text = input("Введіть текст: ")

cleaned_text = ""
punctuation_marks = string.punctuation + "–—«»"

for char in raw_text:
    if char in punctuation_marks:
        cleaned_text += " "
    else:
        cleaned_text += char
words = cleaned_text.lower().split()

unique_once_words = []
for word in words:
    if words.count(word) == 1:
        unique_once_words.append(word)

# 4. Об'єднуємо слова у новий рядок
result_string = " ".join(unique_once_words)

print("\n--- Результат Завдання 3.2 ---")
print("Слова, які трапляються у тексті по одному разу:")
print(f'"{result_string}"')