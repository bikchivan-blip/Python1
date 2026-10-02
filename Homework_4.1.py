text = input("Введіть рядок: ")

index = text.find(":")

if index != -1:
  print(f"Кількість символів до першої двокрапки: {index}")
else:
  print("Двокрапку в рядку не знайдено.")