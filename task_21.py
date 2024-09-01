# Задача 21
book_size = int(input("Введите размер книги в Кб: "))
symbol_size = int(input("Введите размер символа в бит: 1"))
bits_in_one_bytes = 8 # число бит в 1 байте
bytes_in_kilobytes = 1024 # число байт в Кб

symbol_count = book_size * bytes_in_kilobytes * bits_in_one_bytes / symbol_size
print(symbol_count)


