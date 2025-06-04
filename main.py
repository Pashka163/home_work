# Задача 1

# with open('input.txt') as f_in, open('output.txt', 'w') as f_out:
#     text = f_in.read()
#     long_words = [word for word in text.split() if len(word) >= 7]
#     f_out.write(' '.join(long_words))

# Задача 2

# with open('input.txt', 'r', encoding='utf-8') as source:
#     with open('output.txt', 'w', encoding='utf-8') as target:
#         for line in source:
#             target.write(line)

# Задача 3

# with open('input.txt', 'r', encoding='utf-8') as f:
#     lines = f.readlines()
# with open('output.txt', 'w', encoding='utf-8') as f:
#     f.writelines(reversed(lines))

# Задача 4

# with open('input.txt', 'r') as f:
#     lines = f.readlines()
#
# last_no_comma = -1
# for i, line in enumerate(lines):
#     if ',' not in line:
#         last_no_comma = i
#
# pos = last_no_comma + 1 if last_no_comma != -1 else len(lines)
#
# lines.insert(pos, '************\n')
#
# with open('output.txt', 'w') as f:
#     f.writelines(lines)

# Задача 5
#
# char = input("Введите символ: ").lower()
#
# count = 0
# with open('файла.txt', 'r', encoding='utf-8') as file:
#     for line in file:
#         words = line.split()
#         for word in words:
#             if word.lower().startswith(char):
#                 count += 1
#
# print(f"Количество слов {count}")

# Задача 6

# with open('input.txt', 'r') as f_in, open('output.txt', 'w') as f_out:
#     for line in f_in:
#         new_line = line.replace('*', 'temp').replace('&', '*').replace('temp', '&')
#         f_out.write(new_line)

# Задача 7

# lines = ["Первая строка", "Вторая строка", "Третья строка"]
#
# with open('output.txt', 'w', encoding='utf-8') as file:
#     for line in lines:
#         file.write(line + '\n')

# Задача 8

# lines = ["Первая строка", "Вторая строка", "Третья строка"]
#
# with open('output.txt', 'w', encoding='utf-8') as file:
#     file.write('\n'.join(lines))

# Задача 9

# with open('файл.txt', 'r', encoding='utf-8') as file:
#     content = file.read()
#     sumbl = len(content)
#     print(f"Количество символов: {sumbl}")

# Задача 10

# with open('файл.txt', 'r', encoding='utf-8') as file:
#     lines = file.readlines()
#     num_lines = len(lines)
#     print(f"Количество строк в файле: {num_lines}")