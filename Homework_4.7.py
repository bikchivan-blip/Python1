text = input("Введіть речення: ")

words = text.split()
reversed_words = [word[::-1] for word in words]
result = " ".join(reversed_words)

print("\nРезультат реверсу слів:")
print(result)