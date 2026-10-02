text = input("Введіть рядок: ")

count = 0
found = False

for char in text:
  if char == ":":
    found = True
    break
  count += 1

if found:
  print(f"Кількість символів до першої двокрапки: {count}")
else:
  print("Двокрапку в рядку не знайдено.")