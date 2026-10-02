text = input("Введіть рядок із зайвими пробілами: ")

result = ""
in_space = True 

for char in text:
    if char != " ":
        result += char
        in_space = False
    else:
        if not in_space:
            result += " "
            in_space = True

if len(result) > 0 and result[-1] == " ":
    result = result[:-1]

print("Результат після видалення зайвих пробілів:")
print(f'"{result}"')