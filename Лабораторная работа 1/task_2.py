# TODO Найдите количество книг, которое можно разместить на дискете
memory_disk = 1024 ** 2 * 1.44  # Переводим объем памяти в байты
pages = 100
rows = 50
symbols = 25
memory_symbol = 4
memory_book = memory_symbol * symbols * rows * pages

count_book = int(memory_disk // memory_book)
print("Количество книг, помещающихся на дискету:", count_book)
