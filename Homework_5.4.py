import random

n = 10

matrix = [[random.randint(1, 99) for _ in range(n)] for _ in range(n)]

print('Початкова матриця 10x10:')
for row in matrix:
  print([f'{x:2d}' for x in row])

odd_count = 0
for i in range(n):
  for j in range(n):
    if matrix[i][j] % 2 != 0:
      odd_count += 1

print(f'\n1. Кількість непарних елементів матриці: {odd_count}')

for i in range(n):
  for j in range(n):
    if i > j:
      matrix[i][j] = odd_count

print(
    '\n2. Матриця після заміни елементів під головною діагоналлю на число'
    f' {odd_count}:'
)
for row in matrix:
  print([f'{x:3d}' for x in row])

for i in range(n):
  for j in range(n // 2):
    matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j]

print('\n3. Матриця після повороту навколо вертикальної осі:')
for row in matrix:
  print([f'{x:3d}' for x in row])