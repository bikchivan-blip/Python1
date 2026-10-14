initial_tuple = (4, 7, 2, 9, 5, 8, 3, 11)
print('Початковий кортеж:', initial_tuple)

min_val = min(initial_tuple)
print(f'Мінімальний елемент кортежу: {min_val}')

new_elements = ()
for i in range(len(initial_tuple)):
  element = initial_tuple[i]
  if element % 2 != 0 and i % 2 == 0:
    new_elements += (min_val,)
  else:
    new_elements += (element,)

print('Новий кортеж після заміни:', new_elements)