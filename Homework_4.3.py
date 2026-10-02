text = input("Введіть рядок із зайвими пробілами: ")

words = text.split()
result = " ".join(words)

print("Результат після видалення зайвих пробілів:")
print(f'"{result}"')