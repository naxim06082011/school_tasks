a = int(input('введите 1 число'))
b = int(input('введите 2 число'))
c = int(input('введите 3 число'))
if a > b and a > c:
    print('1 число самое большое')
elif b > a and b > c:
    print('2 число самое большое')
elif c > a and c > b:
    print('3 число самое большое')
else:
    print('некоторые из чисел равны')
