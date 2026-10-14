import random

n = int(input('Введіть кількість елементів списку: '))
numbers = [random.randint(1, 50) for _ in range(n)]
print('Початковий список:', numbers)

if len(numbers) > 0:
  average_val = sum(numbers) / len(numbers)
  print(f'Середнє арифметичне елементів списку: {average_val:.2f}')
else:
  print('Список порожній.')

min_val = min(numbers)
print(f'Мінімальний елемент початкового списку: {min_val}')

modified_numbers = list(numbers) 
replaced_indices = []

for i in range(len(modified_numbers)):
  if modified_numbers[i] % 2 != 0: 
    modified_numbers[i] = min_val
    replaced_indices.append(i)  

print('Змінений список:', modified_numbers)
print('Індекси замінених непарних елементів:', replaced_indices)