x1 = int(input('введите номер столбца'))
x2 = int(input('введите номер клетки'))
y1 = int(input('введите номер столбца'))
y2 = int(input('введите номер клетки'))
color1 = (x1 + y1) % 2
color2 = (x2 + y2) % 2
if color1 == color2:
    print('YES')
else:
    print('NO')


