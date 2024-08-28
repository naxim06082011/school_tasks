a = int(input('секунды'))
b = 60
w = a / b
f = a // 3600 
s = int(input('какой ответ вывести,1 или 2'))
if(s == 1):
    print(w)
else:
    print(f)
